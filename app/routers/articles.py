from http import HTTPStatus
from fastapi import APIRouter
from app.db.redis import r
from uuid import uuid4

from app.models.article import Article

router = APIRouter(
    prefix="/article",
    responses={HTTPStatus.NOT_FOUND: {"description": "Not found"}},
)

@router.get("")
async def list_article():
    articles = []
    async for key in r.scan_iter(match=f"{Article.key()}:*"):
        data = await r.hgetall(key)
        articles.append({"key": key, **data})

    return articles

@router.get("/{id}")
async def read_article(id: int):
    return await r.hgetall(f"{Article.key()}:{id}")

@router.post("")
async def create_article(article: Article):
    new_id = uuid4()
    await r.hset(f"{Article.key()}:{uuid4()}", mapping=article.model_dump())
    return {"status": HTTPStatus.CREATED, "id": new_id}

@router.put("/{id}")
async def update_article(id: int, article: Article):
    await r.hset(f"{Article.key()}:{id}", mapping=article.model_dump())
    return {"status": HTTPStatus.OK}

@router.delete("/{id}")
async def delete_article(id: int):
    await r.delete(f"{Article.key()}:{id}")
    return {"status": HTTPStatus.OK, "message": "Article supprimé"}

