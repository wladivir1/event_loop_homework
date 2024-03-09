import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker



POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER", "event")
POSTGRES_DB = os.getenv("POSTGRES_DB", "event")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5431")

PG_DSN = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(engine, expire_on_commit=False) 
