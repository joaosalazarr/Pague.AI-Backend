from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, UTC
from .custom_types import Monetary
from .base_read_schema import BaseRead


class Transaction(BaseModel):
    debt_id: UUID
    paid_amount: Monetary
    payment_date: datetime = Field(default_factory=lambda: datetime.now(UTC))


class TransactionCreate(Transaction):
    pass


class TransactionRead(Transaction, BaseRead):
    pass
