from fastapi import FastAPI

from sqladmin import Admin

from api.routers import all_routers
from api.sqladmin import authentication_backend
from api.views import all_views
from db.db import engine, Base

app = FastAPI(title="Future Farm Game API")

for router in all_routers:
    app.include_router(router)

admin = Admin(app,
              engine,
              title='Future Farm Admin Panel',
              authentication_backend=authentication_backend)

for view in all_views:
    admin.add_view(view)

@app.on_event("startup")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
