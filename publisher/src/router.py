from fastapi import APIRouter, Request
import nats
import asyncio
from .messaging import msg

router = APIRouter()


@router.post("/autoincrement")
async def root():
    await msg.connect()
    ack = await msg.js.publish("FILE", f'{{"logId": "{msg.i}"}}'.encode())
    msg.i +=1 
    print('id добавлен', msg.i, ack)
    await msg.close()

@router.post("/{id}")
async def root(id: str):
    await msg.connect()
    ack = await msg.js.publish("FILE", f'{{"logId": "{id}"}}'.encode())
    print('id добавлен', id, ack)
    await msg.close()
    