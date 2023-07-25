from typing import Optional

from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class SchemaLocation(TunedModel):
    number: int
    title: str
    about: Optional[str] = None


class SchemaDialog(TunedModel):
    number: int
    text: str


class SchemaImage(TunedModel):
    title: str
    data: str
