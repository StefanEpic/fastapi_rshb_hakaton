from .repository import LocationRepository, DialogRepository, ImageRepository
from .services import LocationService, DialogService, ImageService


def location_service():
    return LocationService(LocationRepository)


def dialog_service():
    return DialogService(DialogRepository)


def image_service():
    return ImageService(ImageRepository)
