from fastapi import FastAPI

from game.router import router_game
from database import engine, Base

app = FastAPI(
    title="Future Farm (API for RSHB hakaton game)"
)

app.include_router(router_game)


@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
