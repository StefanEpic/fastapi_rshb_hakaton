from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic.types import List

from database import get_async_session
from .models import Location, Dialog, Image
from .schemas import SchemaLocation, SchemaDialog, SchemaImage

router_game = APIRouter(
    prefix="",
    tags=['location']
)


@router_game.get('/', response_model=List[SchemaLocation])
async def get_location(session: AsyncSession = Depends(get_async_session)):
    query = select(Location).order_by(Location.number)
    result = await session.scalars(query)
    return result.all()


@router_game.get('/dialog', response_model=List[SchemaDialog])
async def get_dialog(location_number: int, gender: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Dialog).where(Dialog.location == location_number, Dialog.gender == gender)
    result = await session.scalars(query)
    return result.all()


@router_game.get('/image', response_model=List[SchemaImage])
async def get_image(location_number: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Image).where(Image.location == location_number)
    result = await session.scalars(query)
    return result.all()
