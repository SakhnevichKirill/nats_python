import os
import asyncio
import time
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.router import router
from src.messaging import msg

    
class Server:
    def __init__(self):
        self.app = FastAPI()
        self.set_routes()

    def set_routes(self):
        self.app.include_router(router)
    
    async def test_messaging(self):
        await msg.connect()
        await msg.close()
        print("Connection tested")

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.test_messaging())
        uvicorn.run(self.app, host="0.0.0.0", port=9005, log_level="info")



server = Server()

if __name__ == "__main__":
    server.run()