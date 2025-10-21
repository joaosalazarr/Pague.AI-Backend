from sqlalchemy import (Column, String)
from sqlalchemy.orm import relationship
from app.db.sqlalchemy_base import Base
from app.db.base_table import BaseTableMixin
from app.models import Debts


class Debtors(BaseTableMixin, Base):
    __tablename__ = 'debtors'

    debtor_name = Column(String(255), nullable=False)
    contact = Column(String(255), nullable=False)

    debt = relationship('Debts', back_populates='debtors')
