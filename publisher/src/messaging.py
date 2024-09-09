from nats import NATS

class Messaging:
    def __init__(self):
        self.js = None
        self.i = 1
        self.nc = NATS()
    
    async def connect(self):
        # res = await self.nc.connect("nats://0.0.0.0:4222")
        await self.nc.connect("nats")
        self.js = self.nc.jetstream()
        await self.js.add_stream(name="FILE", subjects=["FILE"])
    
    async def close(self):
        await self.nc.drain()

msg = Messaging()