import uuid
from sqlalchemy import (Column, String, Integer, Float, Double, Boolean, Date, DateTime, Text, Numeric, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Charges(Base):
    __tablename__ = 'charges'

    charge_id = Column(UUID, primary_key=True, default=uuid.uuid4)
    debt_id = Column(UUID(as_uuid=True), ForeignKey('debts.debt_id'), nullable=False)
    charge_date = Column(DateTime, nullable=False)
    send_status = Column(Boolean, null=False)
    message_midst = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
