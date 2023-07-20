from fastapi import FastAPI

from game.router import router_game

app = FastAPI(
    title="Future Farm (API for RSHB hakaton game)"
)

app.include_router(router_game)
