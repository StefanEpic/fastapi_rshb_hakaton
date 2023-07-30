from typing import Optional

from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class LocationSchema(TunedModel):
    number: int
    title: str
    about: Optional[str] = None


class DialogSchema(TunedModel):
    number: int
    text: str


class ImageSchema(TunedModel):
    title: str
    source: str
