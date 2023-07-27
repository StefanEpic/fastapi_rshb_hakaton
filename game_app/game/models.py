from typing import Optional

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

from .schemas import SchemaLocation, SchemaDialog, SchemaImage


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)
    about: Mapped[Optional[str]]

    def to_read_model(self) -> SchemaLocation:
        return SchemaLocation(
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

    def to_read_model(self) -> SchemaDialog:
        return SchemaDialog(
            number=self.number,
            text=self.text
        )


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    location = mapped_column(ForeignKey("location.number"))
    title: Mapped[str] = mapped_column(unique=True)
    data: Mapped[str]

    def to_read_model(self) -> SchemaImage:
        return SchemaImage(
            title=self.title,
            data=self.data
        )
