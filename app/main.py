from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers import articles
from app.db.redis import r


@asynccontextmanager
async def lifespan(app: FastAPI):
    global r
    try:
        await r.ping()
        print("Connected to Redis")
    except Exception as e:
        print("Redis connection failed:", e)

    yield

    if r:
        await r.close()
        print("Redis connection closed")

app = FastAPI(lifespan=lifespan)

app.include_router(articles.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

