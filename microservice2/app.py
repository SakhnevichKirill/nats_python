import nats
from nats import NATS
import os
import asyncio
import time
import random

async def main():
    
    nc = NATS()
    await nc.connect("localhost:4222")
    js = nc.jetstream()
    await js.add_stream(name="events", subjects=["foo"])
    cons = await js.add_consumer(
            "events",
            durable_name="a",
            max_deliver=4,  # has to be greater than length as backoff array.
            max_waiting=5,
            backoff=[1, 2, 5],
            ack_wait=999999,  # ignored once using backoff
            max_ack_pending=6,
            filter_subject="foo",
        )
    info = await js.consumer_info("events", "a")
    print(info)    
   
    
    
    sub = await js.pull_subscribe_bind("a", stream="events")
    for i in range(15):
            brocken_id = random.randint(0,9)
            try:
                await asyncio.sleep(2)
                msgs = await sub.fetch(1, timeout=3)
                for msg in msgs:
                    #if str(brocken_id) not in msg.data.decode():
                    print('id обработан', msg.data, msg.subject)
                    msg.Ack()
                    #else:
                        #print('ошибка в обработке id', msg.data, msg.subject)
            except Exception as err:
                print(err)
                # There should be no timeout as redeliveries should happen faster.
                break
    info = await js.consumer_info("events", "a")
    print(info)    
    await nc.close()
    
if __name__ == "__main__":
    asyncio.run(main())