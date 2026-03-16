from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from database.db import Base
from uuid import uuid4
from sqlalchemy import DateTime as datetime




class Download(Base):
    __tablename__ = "downloads"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4())
    telegram_id = Column(String, unique=True, nullable=False)
    platform = Column(String, nullable=False)
    media_type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    downloaded_at = Column(datetime(timezone=True), nullable=False)
