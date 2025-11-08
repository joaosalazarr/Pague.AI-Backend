from sqlalchemy.orm import Session
from app.models import Debts
from app.schemas import DebtCreate, DebtRead, CompanyDebtRead
from uuid import uuid4, UUID
from fastapi import status, HTTPException


def create_debt(db: Session, debt_input: DebtCreate) -> DebtRead:
    new_debt = Debts(
        id=uuid4(),
        company_id=debt_input.company_id,
        debt_value=debt_input.debt_value,
        debtor_name=debt_input.debtor_name,
        debtor_contact=debt_input.debtor_contact,
        debtor_cpf=debt_input.debtor_cpf
    )

    db.add(new_debt)
    db.commit()
    db.refresh(new_debt)

    return DebtRead.model_validate(new_debt)


def get_company_debts(db: Session, company_id: UUID) -> list[CompanyDebtRead]:
    debts = db.query(Debts).filter(company_id == Debts.company_id).all()

    result: list[CompanyDebtRead] = []
    for debt in debts:
        result.append(
            CompanyDebtRead(
                id=debt.id,
                debt_value=debt.debt_value,
                debt_status=debt.debt_status,
                created_at=debt.created_at,
                company_name=debt.company.company_name,
                debtor_name=debt.debtor_name,
                debtor_cpf=debt.debtor_cpf,
                debtor_contact=debt.debtor_contact
            )
        )

    return result


def delete_debt_by_id(db: Session, debt_id: UUID):
    debt = db.query(Debts).filter(debt_id == Debts.id).first()

    if not debt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Dívida não encontrada')

    db.delete(debt)
    db.commit()

    return DebtRead.model_validate(debt)
