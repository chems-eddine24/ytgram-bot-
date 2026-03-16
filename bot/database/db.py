from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from config import settings


engine = create_async_engine(settings.DB_ASYNC_URL, echo=True)
AsyncSessionlocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
metadata = MetaData()
Base = declarative_base()



