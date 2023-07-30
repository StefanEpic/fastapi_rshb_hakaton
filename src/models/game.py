from typing import Optional, List

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import ImageType
from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base

from schemas.game import LocationSchema, DialogSchema, ImageSchema


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)
    about: Mapped[Optional[str]]
    dialogs: Mapped[List["Dialog"]] = relationship(back_populates="location")
    images: Mapped[List["Image"]] = relationship(back_populates="location")

    def to_read_model(self) -> LocationSchema:
        return LocationSchema(
            number=self.number,
            title=self.title,
            about=self.about if self.about else None
        )

    def __str__(self):
        return self.title


class Dialog(Base):
    __tablename__ = "dialog"

    id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id", ondelete="CASCADE"))
    location: Mapped["Location"] = relationship(back_populates="dialogs")
    number: Mapped[int]
    gender: Mapped[str] = mapped_column(String(1))
    text: Mapped[Optional[str]]

    def to_read_model(self) -> DialogSchema:
        return DialogSchema(
            number=self.number,
            text=self.text
        )

    def __str__(self):
        return f'{self.number} / {self.gender} / {self.text[:20]}...'


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id", ondelete="CASCADE"))
    location: Mapped["Location"] = relationship(back_populates="images")
    title: Mapped[str] = mapped_column(unique=True)
    source: Mapped[str] = mapped_column(unique=True)

    def to_read_model(self) -> ImageSchema:
        return ImageSchema(
            title=self.title,
            source=self.source
        )

    def __str__(self):
        return self.title
