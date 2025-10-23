from pydantic import BaseModel
from .base_read_schema import BaseRead


class Company(BaseModel):
    company_name: str
    company_registration_number: str
    address: str | None = None


class CompanyCreate(Company):
    pass


class CompanyRead(BaseRead, Company):
    pass