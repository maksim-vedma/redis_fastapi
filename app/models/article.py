from pydantic import BaseModel

class Article(BaseModel):
    title: str
    content: str
    @staticmethod

    def key() -> str:
        return "article"

