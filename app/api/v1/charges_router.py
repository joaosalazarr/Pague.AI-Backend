from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import ChargeCreate, ChargeRead
from app.services.charges_service import create_charge


router = APIRouter(prefix='/charges', tags=['Charges'])


@router.post('/register', response_model=ChargeRead, status_code=201)
def register_charge(charge: ChargeCreate, db: Session = Depends(get_db)):
    """
    Cadastra uma nova cobrança no sistema.
    """
    return create_charge(db=db, charge_input=charge)
