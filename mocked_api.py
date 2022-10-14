import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_world")
def hello_world():
    time.sleep(2)
    return "Hello World"


@app.get("/hello_world_async")
async def hello_world_async():
    await asyncio.sleep(2)
    return "Hello World"

