import nats
from nats import NATS
import os
import asyncio
import time
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

app = FastAPI()   


@app.on_event("startup")
async def lifespan():
    global i 
    i = 0
    global nc
    nc = NATS()
    await nc.connect("localhost:4222")
    global js
    js = nc.jetstream()
    await js.add_stream(name="events", subjects=["foo"])
    yield
    

@app.get("/")
async def root():

    ack = await js.publish("foo", b'id:%d' % i)
    i+=1
    print(ack)
