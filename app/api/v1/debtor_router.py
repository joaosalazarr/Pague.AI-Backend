from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import DebtorCreate, DebtorRead
from app.services.debtor_service import create_debtor


router = APIRouter(prefix='/debtors', tags=['Debtors'])


@router.post('/register', response_model=DebtorRead, status_code=201)
def register_debtor(debtor: DebtorCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo devedor no sistema.
    """
    return create_debtor(db=db, debtor_input=debtor)
