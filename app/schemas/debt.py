from pydantic import BaseModel
from .base_read_schema import BaseRead
from .custom_types import Monetary, ConstrainedString, CPF
from uuid import UUID
from datetime import datetime


class Debt(BaseModel):
    debtor_id: UUID
    debt_value: Monetary


class DebtCreate(Debt):
    company_id: UUID


class DebtRead(BaseRead, Debt):
    debt_status: bool


class CompanyDebtRead(DebtRead):
    created_at: datetime
    company_name: ConstrainedString
    debtor_name: ConstrainedString
    debtor_cpf: CPF
