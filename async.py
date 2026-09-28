import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(10)
    return{
        "message" : "async response generation after 10 secs"
    }