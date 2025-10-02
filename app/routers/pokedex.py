from http import HTTPStatus
from fastapi import APIRouter
import httpx
import json
from app.db.redis import r

router = APIRouter(
    prefix="/pokedex",
    responses={HTTPStatus.NOT_FOUND: {"description": "Not found"}},
)

POKEAPI_URL="https://pokeapi.co/api/v2"

@router.get("/{command}/{sub}")
async def pokeapi(command: str, sub: str):
    key = f"pokedex:{command}:{sub}"
    if (await r.exists(key)):
        return json.loads(await r.get(key))

    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(f"{POKEAPI_URL}/{command}/{sub}")
            response.raise_for_status()
            data = response.json()

            await r.set(key, json.dumps(data), ex=(60 * 60 * 24))

            return {"status": HTTPStatus.OK, "data": data }
    except Exception as e:
        return {"message": "Pokedex action invalid"}
