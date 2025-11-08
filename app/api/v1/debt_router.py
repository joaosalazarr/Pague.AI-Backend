from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import DebtCreate, DebtRead, CompanyDebtRead
from app.services.debt_service import create_debt, get_company_debts
from uuid import UUID


router = APIRouter(prefix='/debts', tags=['Debts'])


@router.post('/register', response_model=DebtRead, status_code=201)
def register_debt(debt: DebtCreate, db: Session = Depends(get_db)):
    """
    Cadastra uma nova dívida no sistema.
    """
    return create_debt(db=db, debt_input=debt)


@router.get('/', response_model=list[CompanyDebtRead], status_code=200)
def company_debts(company_id: UUID, db: Session = Depends(get_db)):
    """
    Obtém as dívidas de uma empresa utilizando seu ID como parâmetro.
    """
    return get_company_debts(db=db, company_id=company_id)
