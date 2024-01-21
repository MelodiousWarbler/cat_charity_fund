from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator
from pydantic.schema import datetime

MINIMUM_LENGHT = 1
MAXIMUM_LENGTH = 100

PROJECT_DESCRIPTION_EMPTY = 'Описание проекта не может быть пустым'
PROJECT_NAME_EMPTY = 'Имя проекта не может быть пустым'


class CharityProjectBase(BaseModel):
    name: str = Field(min_length=MINIMUM_LENGHT, max_length=MAXIMUM_LENGTH)
    description: str = Field(min_length=MINIMUM_LENGHT)
    full_amount: PositiveInt


class CharityProjectCreate(CharityProjectBase):
    @validator('name')
    def name_not_null(cls, value: str) -> str:
        if not value:
            raise ValueError(PROJECT_NAME_EMPTY)
        return value

    @validator('description')
    def description_not_null(cls, value: str) -> str:
        if not value:
            raise ValueError(PROJECT_DESCRIPTION_EMPTY)
        return value


class CharityProjectData(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(
        None, min_length=MINIMUM_LENGHT, max_length=MAXIMUM_LENGTH
    )
    description: Optional[str] = Field(None, min_length=MINIMUM_LENGHT)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid
