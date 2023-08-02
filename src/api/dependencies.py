from repositories.game import LocationRepository, DialogRepository, ImageRepository
from services.game import LocationService, DialogService, ImageService


class GameService:
    @staticmethod
    def location_service():
        return LocationService(LocationRepository)

    @staticmethod
    def dialog_service():
        return DialogService(DialogRepository)

    @staticmethod
    def image_service():
        return ImageService(ImageRepository)
