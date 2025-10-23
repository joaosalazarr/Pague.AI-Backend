from pydantic import BaseModel
from .base_read_schema import BaseRead
from .custom_types import ConstrainedString


class Debtor(BaseModel):
    debtor_name: ConstrainedString
    contact: ConstrainedString


class DebtorCreate(Debtor):
    pass


class DebtorRead(Debtor, BaseRead):
    pass
