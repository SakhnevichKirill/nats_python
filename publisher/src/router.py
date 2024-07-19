from fastapi import APIRouter, Request
import nats
import asyncio
from .messaging import msg

router = APIRouter()


@router.get("/")
async def root(req = Request):
    await msg.connect()
    ack = await msg.js.publish("foo", b'id:%d' % msg.i)
    msg.i +=1 
    print('id добавлен', msg.i, ack)
    await msg.close()
    