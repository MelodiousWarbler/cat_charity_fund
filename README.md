# Проект "Благотворительный фонд поддержки котиков QRKot"

## Описание проекта

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии и библиотеки

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-blue?style=flat-square&logo=FastAPI&logoColor=3776AB&labelColor=d0d0d0)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-blue?style=flat-square&logo=SQLAlchemy&logoColor=3776AB&labelColor=d0d0d0)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-blue?style=flat-square&logo=Pydantic&logoColor=3776AB&labelColor=d0d0d0)](https://docs.pydantic.dev/latest/)
[![Alembic](https://img.shields.io/badge/Alembic-blue?style=flat-square&logo=Alembic&logoColor=3776AB&labelColor=d0d0d0)](https://alembic.sqlalchemy.org/en/latest/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-blue?style=flat-square&logo=Uvicorn&logoColor=3776AB&labelColor=d0d0d0)](https://www.uvicorn.org/)

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/MelodiousWarbler/cat_charity_fund.git
```

Создать и активировать виртуальное окружение:
```
python3 -m venv env
```

* Для Linux/macOS

    ```
    source venv/bin/activate
    ```

* Для Windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корневой директории проекта создайте файл .env и заполните его по образцу:

```
DATABASE_URL=sqlite+aiosqlite:///./cat_charity.db
SECRET=<mysecret>
```

Примените миграции:

```
alembic upgrade head
```

Запустите проект

```
uvicorn app.main:app --reload
```

Документация доступна по [ссылке](http://127.0.0.1:8000/docs/ "Документация") после запуска проекта.

## Автор проекта

- [Яков Плакотнюк](https://github.com/MelodiousWarbler "GitHub аккаунт")
