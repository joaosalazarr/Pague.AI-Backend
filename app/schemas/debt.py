from pydantic import BaseModel
from .base_read_schema import BaseRead
from .custom_types import Monetary
from uuid import UUID


class Debt(BaseModel):
    debtor_id: UUID
    debt_value: Monetary
    debt_status: bool


class DebtCreate(Debt):
    company_id: UUID


class DebtRead(BaseRead, Debt):
    pass
