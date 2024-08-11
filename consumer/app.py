import nats
from nats import NATS
import os
import asyncio
import time
import random

async def main():
    nc = NATS()
    # await nc.connect("localhost:4222")
    await nc.connect("nats-server")
    js = nc.jetstream()
    await js.add_stream(name="FILE", subjects=["FILE"])
    cons = await js.add_consumer(
        "FILE",
        durable_name="ab",
        max_deliver=4,  # has to be greater than length as backoff array.
        max_waiting=15,
        backoff=[7, 10, 13],
        ack_wait=999999,  # ignored once using backoff
        max_ack_pending=13,
        filter_subject="FILE",
    )
    info = await js.consumer_info("FILE", "ab")
    print(info)    
    
    sub = await js.pull_subscribe_bind("ab", stream="FILE")
    while True:
            try:
                msgs = await sub.fetch()
                for msg in msgs:
                    print('id обработан', msg.data, msg.subject)
                    await asyncio.sleep(2)
                    await msg.ack()
            except Exception as err:
                print(err)

    await nc.close()
    
if __name__ == "__main__":
    asyncio.run(main())