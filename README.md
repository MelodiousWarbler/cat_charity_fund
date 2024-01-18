# Проект "Благотворительный фонд поддержки котиков QRKot"

## Описание проекта

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии и библиотеки

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-green?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://fastapi.tiangolo.com/)

 - SQLAlchemy (библиотека для работы с реляционными СУБД с применением технологии ORM)
 - Pydantic (библиотека для валидации и сериализации данных)
 - Alembic (инструмент для миграции базы данных)
 - Uvicorn (высокопроизводительный ASGI сервер)

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/fluid1408/cat_charity_fund
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
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
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

Документация доступна по ссылке http://127.0.0.1:8000/docs/ после запуска проекта.

## Автор проекта

- [Яков Плакотнюк](https://github.com/MelodiousWarbler "GitHub аккаунт")
