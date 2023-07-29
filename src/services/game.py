from utils.repository import AbstractRepository


class LocationService:
    def __init__(self, location_repo: AbstractRepository):
        self.location_repo: AbstractRepository = location_repo()

    async def get_locations(self):
        locations = await self.location_repo.get_list()
        return locations


class DialogService:
    def __init__(self, dialog_repo: AbstractRepository):
        self.dialog_repo: AbstractRepository = dialog_repo()

    async def get_dialogs(self, location_number: int, gender: str):
        dialogs = await self.dialog_repo.get_dialog(location_number, gender)
        return dialogs


class ImageService:
    def __init__(self, image_repo: AbstractRepository):
        self.image_repo: AbstractRepository = image_repo()

    async def get_images(self, location_number: int):
        images = await self.image_repo.get_image(location_number)
        return images
