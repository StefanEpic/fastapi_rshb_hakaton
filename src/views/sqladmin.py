from sqladmin import ModelView

from models.game import Location, Dialog, Image


class LocationAdmin(ModelView, model=Location):
    column_list = [Location.id, Location.number, Location.title, Location.about]


class DialogAdmin(ModelView, model=Dialog):
    column_list = [Dialog.id, Dialog.location, Dialog.number, Dialog.gender, Dialog.text]


class ImageAdmin(ModelView, model=Image):
    column_list = [Image.id, Image.location, Image.title, Image.data]
