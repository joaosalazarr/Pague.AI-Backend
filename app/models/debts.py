from sqlalchemy import (Column, Float, Boolean, ForeignKey, String)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.sqlalchemy_base import Base
from app.db.base_table import BaseTableMixin


class Debts(BaseTableMixin, Base):
    __tablename__ = 'debts'

    # debtor_id = Column(UUID(as_uuid=True), ForeignKey('debtors.id'), nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey('companies.id'), nullable=False)
    debt_value = Column(Float, nullable=False)
    debt_status = Column(Boolean, nullable=False, default=False)

    debtor_name = Column(String(255), nullable=False)
    debtor_contact = Column(String(255), nullable=False)
    debtor_cpf = Column(String(14), nullable=False)

    # debtor = relationship('Debtors', back_populates='debts')
    company = relationship('Companies', back_populates='debts')
    charges = relationship('Charges', back_populates='debt')
    transactions = relationship('Transactions', back_populates='debt')
