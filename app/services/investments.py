from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def not_empty_object(model, session: AsyncSession):
    object = await session.execute(
        select(model).where(model.fully_invested.is_(False))
    )
    return object.scalars().all()


def update_object(object, invested_add):
    object.invested_amount += invested_add
    if object.invested_amount >= object.full_amount:
        object.invested_amount = object.full_amount
        object.fully_invested = True
        object.close_date = datetime.now()
    return object


def update_project_and_donation(
    donation,
    charity_project
):
    remain_project = (
        charity_project.full_amount -
        charity_project.invested_amount
    )
    remain_donation = donation.full_amount - donation.invested_amount
    charity_project = update_object(
        charity_project, remain_donation
    )
    donation = update_object(
        donation, remain_project
    )
    return donation, charity_project


async def invest(session: AsyncSession):
    donations = await not_empty_object(Donation, session)
    charity_projects = await not_empty_object(CharityProject, session)
    for donation in donations:
        for charity_project in charity_projects:
            donation, charity_project = update_project_and_donation(
                donation, charity_project
            )
            session.add(donation)
            session.add(charity_project)
    return session
