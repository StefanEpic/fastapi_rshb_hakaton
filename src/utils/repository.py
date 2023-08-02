from abc import ABC, abstractmethod

from sqlalchemy import select

from db.db import async_session_maker


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
