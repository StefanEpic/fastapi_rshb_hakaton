from abc import ABC, abstractmethod
from sqlalchemy import select

from database import async_session_maker

from .models import Location, Dialog, Image


class AbstractRepository(ABC):
    @abstractmethod
    async def get_list():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_list(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res


class LocationRepository(SQLAlchemyRepository):
    model = Location


class DialogRepository(SQLAlchemyRepository):
    model = Dialog

    async def get_dialog(self, location_number: int, gender: str):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.location == location_number, self.model.gender == gender)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res


class ImageRepository(SQLAlchemyRepository):
    model = Image

    async def get_image(self, location_number: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.location == location_number)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res
