from sqladmin import ModelView

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
    column_list = [Image.location, Image.title, Image.source]
    form_columns = "__all__"
    column_details_list = [Image.location, Image.title, Image.source]
    can_export = False
    icon = "fa-solid fa-image"
