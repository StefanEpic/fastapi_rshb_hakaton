from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic.types import List

from database import get_async_session
from .models import Location, Dialog, Image
from .schemas import SchemaLocation, SchemaDialog, SchemaImage

router_game = APIRouter(
    tags=['location']
)


@router_game.get('/', response_model=List[SchemaLocation])
async def get_location(session: AsyncSession = Depends(get_async_session)):
    query = select(Location)
    result = await session.execute(query)
    return result.all()


@router_game.get('/dialog', response_model=List[SchemaDialog])
async def get_dialog(location_number: int, gender: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Dialog).where(Dialog.c.location == location_number, Dialog.c.gender == gender)
    result = await session.execute(query)
    return result.all()


@router_game.get('/image', response_model=List[SchemaImage])
async def get_image(location_number: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Image).where(Image.c.location == location_number)
    result = await session.execute(query)
    return result.all()
