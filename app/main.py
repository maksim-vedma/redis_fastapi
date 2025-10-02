from fastapi import FastAPI
import redis.asyncio as redis

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.on_event("startup")
async def startup_event():
    # Check connection on startup
    try:
        await r.ping()
        print("Connected to Redis")
    except Exception as e:
        print("Redis connection failed:", e)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/ping")
async def ping():
    return await r.ping()

