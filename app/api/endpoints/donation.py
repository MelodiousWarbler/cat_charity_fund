from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.constants import FULLY_INVESTED
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import (
    DonationBase, DonationData, DonationView
)
from app.services.investments import invest

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationData],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model=list[DonationView],
    dependencies=[Depends(current_user)],
)
async def get_my_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await donation_crud.get_user_donations(user=user, session=session)


@router.post(
    '/',
    response_model=DonationView,
    response_model_exclude_none=True
)
async def create_donation(
    obj_in: DonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    new_donation = await donation_crud.create(
        obj_in=obj_in,
        session=session,
        user=user,
        commit=False,
    )
    open_projects = await charity_project_crud.get_multi_by_attribute(
        FULLY_INVESTED, False, session
    )
    session.add_all(invest(new_donation, open_projects))
    await session.commit()
    await session.refresh(new_donation)
    return new_donation
