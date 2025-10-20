from sqlalchemy import (Column, String, Integer, Float, Double, Boolean, Date, DateTime, Text, Numeric, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.base_table import BaseTableMixin


class Users(BaseTableMixin, Base):
    __tablename__ = 'users'

    company_id = Column(UUID(as_uuid=True), ForeignKey('companies.id'), nullable=False)
    user_name = Column(String(255))
    email = Column(String(255), nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String(255))

    company = relationship('Companies', back_populates='users')
