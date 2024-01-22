from sqlalchemy import Column, String, Text

from app.models.base import ProjectDonationBase

NAME_MAXIMUM_LENGTH = 100


class CharityProject(ProjectDonationBase):
    name = Column(String(NAME_MAXIMUM_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            super().__repr__()
            +
            f', Название проекта: {self.name}, '
            f'Описание проекта: {self.description}'
        )
