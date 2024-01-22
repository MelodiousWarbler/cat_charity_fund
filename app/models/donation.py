from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import ProjectDonationBase


class Donation(ProjectDonationBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return (
            super().__repr__()
            +
            f', ID пользователя: {self.user_id}, '
            f'Комментарий: {self.comment}'
        )
