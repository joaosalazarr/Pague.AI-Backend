from sqlalchemy import (Column, String, Boolean, DateTime, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.sqlalchemy_base import Base
from app.db.base_table import BaseTableMixin


class Charges(BaseTableMixin, Base):
    __tablename__ = 'charges'

    debt_id = Column(UUID(as_uuid=True), ForeignKey('debts.id'), nullable=False)
    charge_date = Column(DateTime, nullable=False)
    send_status = Column(Boolean, nullable=False)
    message_midst = Column(String, nullable=False)

    debt = relationship('Debts', back_populates='charges')
