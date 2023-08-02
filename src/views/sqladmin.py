import os

from sqladmin import ModelView
from sqlalchemy import update

from db.db import SITE, async_session_maker
from models.game import Location, Dialog, Image


class LocationAdmin(ModelView, model=Location):
    column_list = [Location.number, Location.title, Location.about]
    form_columns = [Location.number, Location.title, Location.about]
    column_details_list = [Location.number, Location.title, Location.about, Location.dialogs, Location.images]
    can_export = False
    icon = "fa-solid fa-map-location-dot"


class DialogAdmin(ModelView, model=Dialog):
    column_list = [Dialog.location, Dialog.number, Dialog.gender, Dialog.text]
    form_columns = "__all__"
    column_details_list = [Dialog.location, Dialog.number, Dialog.gender, Dialog.text]
    can_export = False
    icon = "fa-solid fa-comment-dots"


class ImageAdmin(ModelView, model=Image):
    column_list = [Image.location, Image.title, Image.source, Image.url]
    form_columns = [Image.location, Image.title, Image.source]
    column_details_list = [Image.location, Image.title, Image.source, Image.url]
    can_export = False
    icon = "fa-solid fa-image"

    async def after_model_change(
            self, data: dict, model=Image, is_created=True
    ) -> None:
        async with async_session_maker() as session:
            filename = model.source.filename
            url = SITE + filename
            stmt = update(Image).where(Image.id == model.id).values(url=url)
            res = await session.execute(stmt)
            await session.commit()
            return res

    async def on_model_delete(self, model=Image) -> None:
        os.remove(model.source)
