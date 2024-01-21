from typing import Optional

from pydantic import BaseModel, Extra, PositiveInt
from pydantic.schema import datetime


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationView(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationData(DonationView):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
