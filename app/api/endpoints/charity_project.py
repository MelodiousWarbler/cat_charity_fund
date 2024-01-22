from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.constants import FULLY_INVESTED
from app.api.validators import (
    access_project_update, check_name_duplicate,
    check_project_exists, check_full_amount,
    invested_in_project
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectData, CharityProjectUpdate
)
from app.services.investments import invest

router = APIRouter()


@router.get(
    '/',
    response_model=list[CharityProjectData],
    response_model_exclude_none=True
)
async def get_projects(
    session: AsyncSession = Depends(get_async_session)
):
    return await charity_project_crud.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectData,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def create_project(
    new_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(new_project.name, session)
    open_donations = await donation_crud.get_multi_by_attribute(
        FULLY_INVESTED, False, session
    )
    new_project = await charity_project_crud.create(
        new_project, session, commit=False
    )
    session.add_all(invest(new_project, open_donations))
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectData,
    dependencies=[Depends(current_superuser)]
)
async def update_project(
    new_project: CharityProjectUpdate,
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    project = await check_project_exists(project_id, session)
    await access_project_update(project_id, session)
    await check_name_duplicate(new_project.name, session)
    await check_full_amount(project_id, new_project.full_amount, session)
    updated_project = await charity_project_crud.update(
        session=session, db_obj=project, obj_in=new_project
    )
    return updated_project


@router.delete(
    '/{project_id}',
    dependencies=[Depends(current_superuser)]
)
async def delete_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    project = await check_project_exists(project_id, session)
    await invested_in_project(project_id, session)
    charity_project_crud.remove(session, project)
    return project
