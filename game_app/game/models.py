from sqlalchemy import Column, Integer, String, ForeignKey

from database import Base


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False, unique=True)
    title = Column(String, nullable=False, unique=True)
    about = Column(String)


class Dialog(Base):
    __tablename__ = "dialog"

    id = Column('id', Integer, primary_key=True)
    location = Column('location', Integer, ForeignKey('location.number'))
    number = Column('number', Integer, nullable=False)
    gender = Column('gender', String(1), nullable=False)
    text = Column('text', String)


class Image(Base):
    __tablename__ = "image"

    id = Column('id', Integer, primary_key=True)
    location = Column('location', Integer, ForeignKey('location.number'))
    title = Column('title', String, nullable=False, unique=True)
    data = Column('data', String, nullable=False)
