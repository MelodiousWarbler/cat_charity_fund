from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject

PROJECT_ALREADY_EXISTS = 'Проект с таким именем уже существует!'
PROJECT_NOT_FOUND = 'Проект не найден!'
PROJECT_ALREADY_CLOSED = 'Закрытый проект нельзя редактировать!'
INVESTMENTS_EXISTS = 'В проект были внесены средства, не подлежит удалению!'
FULL_AMOUNT_INCORRECT = 'Значение суммы не может быть меньше внесённой'


async def check_name_duplicate(
    project_name: str,
    session: AsyncSession,
) -> None:
    project = await charity_project_crud.get_id_by_name(
        project_name, session
    )
    if project:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=PROJECT_ALREADY_EXISTS,
        )


async def check_project_exists(
    project_id: int,
    session: AsyncSession,
) -> CharityProject:
    project = await charity_project_crud.get(
        project_id, session
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=PROJECT_NOT_FOUND,
        )
    return project


async def access_project_update(
    project_id: int, session: AsyncSession
) -> CharityProject:
    project = await charity_project_crud.get(
        project_id, session
    )
    if project.fully_invested:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=PROJECT_ALREADY_CLOSED,
        )
    return project


async def invested_in_project(
        project_id: int,
        session: AsyncSession,
) -> None:
    project = await charity_project_crud.get(
        project_id, session
    )
    if project.invested_amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVESTMENTS_EXISTS,
        )


async def check_full_amount(
    project_id: int,
    new_full_amount: int,
    session: AsyncSession,
) -> None:
    project = await charity_project_crud.get(
        project_id, session
    )
    if new_full_amount and new_full_amount < project.invested_amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=FULL_AMOUNT_INCORRECT,
        )
