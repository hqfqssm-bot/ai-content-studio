import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    credits = Column(Integer, default=0)
    is_pro = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    generations = relationship("Generation", back_populates="user")


class Generation(Base):
    __tablename__ = "generations"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    content_type = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    result = Column(Text, nullable=True)
    tokens_used = Column(Integer, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="generations")


class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    key = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_used_at = Column(DateTime, nullable=True)
