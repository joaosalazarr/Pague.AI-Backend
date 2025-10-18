from sqlalchemy import (Column, String, Integer, Float, Double, Boolean, Date, DateTime, Text, Numeric, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.base_table import BaseTableMixin


class Debtors(BaseTableMixin, Base):
    __tablename__ = 'debtors'

    debtor_name = Column(String(255), nullable=False)
    contact = Column(String(255), nullable=False)
