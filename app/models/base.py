import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base


class ProjectDonationBase(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint('full_amount > 0'),
        CheckConstraint('invested_amount <= full_amount'),
    )

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.datetime.now)
    close_date = Column(DateTime, default=None)

    def __repr__(self):
        return (
            f'Общая сумма: {self.full_amount}, '
            f'Инвестировано: {self.invested_amount}, '
            f'Полностью проинвестировано: {self.fully_invested}, '
            f'Дата создания: {self.create_date}, '
            f'Дата закрытия: {self.close_date}'
        )
