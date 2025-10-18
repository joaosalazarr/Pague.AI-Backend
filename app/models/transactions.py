import uuid
from sqlalchemy import (Column, String, Integer, Float, Double, Boolean, Date, DateTime, Text, Numeric, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Transactions(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    debt_id = Column(UUID(as_uuid=True), ForeignKey('debts.debt_id'))
    paid_amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
