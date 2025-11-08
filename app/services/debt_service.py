from sqlalchemy.orm import Session
from app.models import Debts
from app.schemas import DebtCreate, DebtRead, CompanyDebtRead
from uuid import uuid4, UUID


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


def get_company_debts(db: Session, company_id: UUID) -> list[CompanyDebtRead]:
    debts = db.query(Debts).filter(company_id == Debts.company_id).all()

    result: list[CompanyDebtRead] = []
    for debt in debts:
        result.append(
            CompanyDebtRead(
                id=debt.id,
                debt_value=debt.debt_value,
                debt_status=debt.debt_status,
                debtor_id=debt.debtor_id,
                created_at=debt.created_at,
                company_name=debt.company.company_name,
                debtor_name=debt.debtor.debtor_name,
                debtor_cpf=debt.debtor.debtor_cpf
            )
        )

    return result
