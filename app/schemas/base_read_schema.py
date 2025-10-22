from pydantic import BaseModel
from uuid import UUID


class BaseRead(BaseModel):
    id: UUID

    class Config:
        from_attributes: bool = True
