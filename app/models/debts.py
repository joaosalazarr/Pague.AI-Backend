import uuid
from sqlalchemy import (Column, String, Integer, Float, Double, Boolean, Date, DateTime, Text, Numeric, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Debts(Base):
    __tablename__ = 'debts'
