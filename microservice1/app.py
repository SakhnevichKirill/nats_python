import nats
from nats import NATS
import os
import asyncio
import time

async def main():
    
    nc = NATS()
    await nc.connect("localhost:4222")

    js = nc.jetstream()

    await js.add_stream(name="events", subjects=["foo"])
    
    for i in range(0, 10):
        ack = await js.publish("foo", b'id:%d' % i)
        await asyncio.sleep(1)
        print(ack)
if __name__ == "__main__":
    asyncio.run(main())