import uuid
from sqlalchemy import (Column, String, Integer, Float, Double, Boolean, Date, DateTime, Text, Numeric, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Debtors(Base):
    __tablename__ = 'debtors'

    debtor_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    debtor_name = Column(String(255), nullable=False)
    contact = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
