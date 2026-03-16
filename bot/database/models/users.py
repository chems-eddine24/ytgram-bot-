from sqlalchemy import Column, String, Integer, UUID
from sqlalchemy import DateTime as datetime
from database.db import Base
from sqlalchemy.dialects.postgresql import UUID 
from uuid import uuid4




class User(Base):

    __tablename__ = "users"
    id = Column(UUID(as_uuid=True),unique = True, primary_key=True, nullable=False, default=uuid4())
    telegram_id = Column(String, unique=True, nullable=False)
    telegram_username = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    joined_at = Column(datetime(timezone=True), nullable=False)