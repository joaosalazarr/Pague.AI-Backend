from sqlalchemy.orm import Session
from app.models import Debts
from app.schemas import DebtCreate, DebtRead
from uuid import uuid4

def create_debt(db: Session, debt_input: DebtCreate) -> DebtRead:
    new_debt = Debts(
        id=uuid4(),
        debtor_id=debt_input.debtor_id,
        company_id=debt_input.company_id,
        debt_value=debt_input.debt_value
    )

    db.add(new_debt)
    db.commit()
    db.refresh(new_debt)

    return DebtRead.model_validate(new_debt)
