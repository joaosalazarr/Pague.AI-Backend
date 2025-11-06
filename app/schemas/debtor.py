from pydantic import BaseModel
from .base_read_schema import BaseRead
from .custom_types import ConstrainedString, CPF


class Debtor(BaseModel):
    debtor_name: ConstrainedString
    contact: ConstrainedString
    debtor_cpf: CPF


class DebtorCreate(Debtor):
    pass


class DebtorRead(Debtor, BaseRead):
    pass
