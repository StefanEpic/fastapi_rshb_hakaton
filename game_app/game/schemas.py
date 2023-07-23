from pydantic import BaseModel


class SchemaLocation(BaseModel):
    number: int
    title: str
    about: str

    class Config:
        orm_mode = True


class SchemaDialog(BaseModel):
    number: int
    text: str

    class Config:
        orm_mode = True


class SchemaImage(BaseModel):
    title: str
    data: str

    class Config:
        orm_mode = True
