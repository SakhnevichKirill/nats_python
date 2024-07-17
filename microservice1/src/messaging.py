from nats import NATS

class Messaging:
    def __init__(self):
        # self.nc = None
        self.js = None
        self.i = 0
        self.nc = NATS()
    
    async def connect(self):
        # res = await self.nc.connect("nats://0.0.0.0:4222")
        res = await self.nc.connect("nats-server")
        print(res)
        self.js = self.nc.jetstream()
        res = await self.js.add_stream(name="events", subjects=["foo"])
        # self.nc.close()
        print(res)
        # yield
    
    async def close(self):
        await self.nc.drain()

msg = Messaging()