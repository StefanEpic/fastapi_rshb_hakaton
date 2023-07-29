from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import GameService
from services.game import LocationService, DialogService, ImageService

router = APIRouter(
    prefix="",
    tags=["Game"],
)


@router.get('/')
async def get_locations(location_service: Annotated[LocationService, Depends(GameService.location_service)]):
    locations = await location_service.get_locations()
    return locations


@router.get('/dialog')
async def get_dialogs(location_number: int,
                      gender: str,
                      dialog_service: Annotated[DialogService, Depends(GameService.dialog_service)]):
    dialogs = await dialog_service.get_dialogs(location_number, gender)
    return dialogs


@router.get('/image')
async def get_images(location_number: int,
                     image_service: Annotated[ImageService, Depends(GameService.image_service)]):
    images = await image_service.get_images(location_number)
    return images
