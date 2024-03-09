from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

from configDB import engine



class Base(AsyncAttrs, DeclarativeBase):
    pass


class SwapiPeople(Base):
    __tablename__ = "people"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    height: Mapped[str] = mapped_column(String)
    mass: Mapped[str] = mapped_column(String)
    hair_color: Mapped[str] = mapped_column(String)
    skin_color: Mapped[str] = mapped_column(String)
    eye_color: Mapped[str] = mapped_column(String)
    birth_year: Mapped[str] = mapped_column(String)
    gender: Mapped[str] = mapped_column(String)
    homeworld: Mapped[str] = mapped_column(String)
    films: Mapped[str] = mapped_column(String)
    species: Mapped[str] = mapped_column(String)
    vehicles: Mapped[str] = mapped_column(String)
    starships: Mapped[str] = mapped_column(String)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all) 
        
          