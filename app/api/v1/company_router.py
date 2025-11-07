from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import CompanyCreate, CompanyRead
from app.services.company_service import create_company


router = APIRouter(prefix='/companies', tags=['Companies'])


@router.post('/register', response_model=CompanyRead, status_code=201)
def register_company(company: CompanyCreate, db: Session = Depends(get_db)):
    """
    Cadastra uma nova empresa no sistema.
    """
    return create_company(db=db, company_input=company)
