from fastapi import FastAPI
import redis.asyncio as redis
from contextlib import asynccontextmanager

r: redis.Redis|None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global r
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    try:
        await r.ping()
        print("Connected to Redis")
    except Exception as e:
        print("Redis connection failed:", e)

    yield  # Application runs here

    # Shutdown
    if r:
        await r.close()
        print("Redis connection closed")

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
