from pydantic import BaseModel, Field
from datetime import datetime, UTC
from uuid import UUID
from .base_read_schema import BaseRead


class Charge(BaseModel):
    debt_id: UUID
    charge_date: datetime = Field(default_factory=lambda: datetime.now(UTC))
    send_status: bool = False
    message_midst: str


class ChargeCreate(Charge):
    pass


class ChargeRead(BaseRead, Charge):
    pass
