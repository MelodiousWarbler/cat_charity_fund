from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков QRKot'
    database_url: str = 'sqlite+aiosqlite:///./QRKot.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
