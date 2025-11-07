from sqlalchemy.orm import Session
from app.models import Charges
from app.schemas import ChargeCreate, ChargeRead
from uuid import uuid4

def create_charge(db: Session, charge_input: ChargeCreate) -> ChargeRead:
    new_charge = Charges(
        id=uuid4(),
        debt_id=charge_input.debt_id,
        charge_date=charge_input.charge_date,
        send_status=charge_input.send_status,
        message_midst=charge_input.message_midst
    )

    db.add(new_charge)
    db.commit()
    db.refresh(new_charge)

    return ChargeRead.model_validate(new_charge)
