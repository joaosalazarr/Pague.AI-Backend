from sqlalchemy import (Column, Float, DateTime, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.sqlalchemy_base import Base
from app.db.base_table import BaseTableMixin


class Transactions(BaseTableMixin, Base):
    __tablename__ = 'transactions'

    debt_id = Column(UUID(as_uuid=True), ForeignKey('debts.id'), nullable=False)
    paid_amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)

    debt = relationship('Debts', back_populates='transactions')
