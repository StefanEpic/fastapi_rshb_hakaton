from typing import Annotated

from fastapi import APIRouter, Depends

from .dependencies import location_service, dialog_service, image_service
from .services import LocationService, DialogService, ImageService

router_game = APIRouter(
    prefix="",
    tags=['location']
)


@router_game.get('/')
async def get_locations(location_service: Annotated[LocationService, Depends(location_service)]):
    locations = await location_service.get_locations()
    return locations


@router_game.get('/dialog')
async def get_dialogs(location_number: int,
                      gender: str,
                      dialog_service: Annotated[DialogService, Depends(dialog_service)]):
    dialogs = await dialog_service.get_dialogs(location_number, gender)
    return dialogs


@router_game.get('/image')
async def get_images(location_number: int,
                     image_service: Annotated[ImageService, Depends(image_service)]):
    images = await image_service.get_images(location_number)
    return images
