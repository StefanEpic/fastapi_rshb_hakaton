from sqlalchemy import select

from models.game import Location, Dialog, Image
from utils.repository import SQLAlchemyRepository

from db.db import async_session_maker


class LocationRepository(SQLAlchemyRepository):
    model = Location


class DialogRepository(SQLAlchemyRepository):
    model = Dialog

    async def get_dialog(self, location_number: int, gender: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(
                self.model.location.has(Location.number == location_number), self.model.gender == gender)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res


class ImageRepository(SQLAlchemyRepository):
    model = Image

    async def get_image(self, location_number: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.location.has(Location.number == location_number))
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
