from typing import Optional

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Location(Base):
    __tablename__ = "location"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column(unique=True)
    about: Mapped[Optional[str]]


class Dialog(Base):
    __tablename__ = "dialog"

    id: Mapped[int] = mapped_column(primary_key=True)
    location = mapped_column(ForeignKey("location.number"))
    number: Mapped[int]
    gender: Mapped[str] = mapped_column(String(1))
    text: Mapped[Optional[str]]


class Image(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    location = mapped_column(ForeignKey("location.number"))
    title: Mapped[str] = mapped_column(unique=True)
    data: Mapped[str]
