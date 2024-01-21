from sqlalchemy import Column, String, Text

from app.models.base import ProjectDonationBase

NAME_MAXIMUM_LENGTH = 100


class CharityProject(ProjectDonationBase):
    name = Column(String(NAME_MAXIMUM_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
