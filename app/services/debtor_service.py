from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import Debtors
from app.schemas import DebtorCreate, DebtorRead
from uuid import uuid4

def create_debtor(db: Session, debtor_input: DebtorCreate) -> DebtorRead:
    existing_debtor = db.query(Debtors).filter(debtor_input.debtor_cpf == Debtors.debtor_cpf).first()

    if existing_debtor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Um devedor com esse CPF já foi criado')

    new_debtor = Debtors(
        id=uuid4(),
        debtor_name=debtor_input.debtor_name,
        contact=debtor_input.contact,
        debtor_cpf=debtor_input.debtor_cpf
    )

    db.add(new_debtor)
    db.commit()
    db.refresh(new_debtor)

    return DebtorRead.model_validate(new_debtor)
