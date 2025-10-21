from sqlalchemy import (Column, String, Text)
from sqlalchemy.orm import relationship
from app.db.sqlalchemy_base import Base
from app.db.base_table import BaseTableMixin


class Companies(BaseTableMixin, Base):
    __tablename__ = 'companies'

    company_name = Column(String(255), nullable=False)
    company_registration_number = Column(String(18), nullable=False)
    address = Column(Text)

    user = relationship('Users', back_populates='company')
