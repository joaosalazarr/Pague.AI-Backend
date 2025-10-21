from sqlalchemy import (Column, Float, Boolean, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.sqlalchemy_base import Base
from app.db.base_table import BaseTableMixin
from app.models import Debtors, Companies


class Debts(BaseTableMixin, Base):
    __tablename__ = 'debts'

    debtor_id = Column(UUID(as_uuid=True), ForeignKey('debtors.id'), nullable=False)
    companies_id = Column(UUID(as_uuid=True), ForeignKey('companies.id'), nullable=False)
    debt_value = Column(Float, nullable=False)
    debt_status = Column(Boolean, nullable=False, default=False)

    debtor = relationship('Debtors', back_populates='debts')
    company = relationship('Companies', back_populates='debts')
