from typing import Optional

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base

from schemas.game import LocationSchema, DialogSchema, ImageSchema


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)
    about: Mapped[Optional[str]]

    def to_read_model(self) -> LocationSchema:
        return LocationSchema(
            number=self.number,
            title=self.title,
            about=self.about if self.about else None
        )


class Dialog(Base):
    __tablename__ = "dialog"

    id: Mapped[int] = mapped_column(primary_key=True)
    location = mapped_column(ForeignKey("location.number"))
    number: Mapped[int]
    gender: Mapped[str] = mapped_column(String(1))
    text: Mapped[Optional[str]]

    def to_read_model(self) -> DialogSchema:
        return DialogSchema(
            number=self.number,
            text=self.text
        )


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    location = mapped_column(ForeignKey("location.number"))
    title: Mapped[str] = mapped_column(unique=True)
    data: Mapped[str]

    def to_read_model(self) -> ImageSchema:
        return ImageSchema(
            title=self.title,
            data=self.data
        )
