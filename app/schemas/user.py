from pydantic import BaseModel, EmailStr
from .base_read_schema import BaseRead
from .custom_types import ConstrainedString
from uuid import UUID


class BaseUser(BaseModel):
    user_name: ConstrainedString
    role: ConstrainedString
    company_id: UUID


class UserCreate(BaseUser):
    password: str
    email: EmailStr


class UserRead(BaseUser, BaseRead):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str
