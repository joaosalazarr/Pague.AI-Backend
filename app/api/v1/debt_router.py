from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import DebtCreate, DebtRead
from app.services.debt_service import create_debt


router = APIRouter(prefix='/debts', tags=['Debts'])


@router.post('/register', response_model=DebtRead, status_code=201)
def register_debt(debt: DebtCreate, db: Session = Depends(get_db)):
    """
    Cadastra uma nova dívida no sistema.
    """
    return create_debt(db=db, debt_input=debt)
