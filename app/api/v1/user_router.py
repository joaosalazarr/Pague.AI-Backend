from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas import UserCreate, UserRead
from app.services.user_service import create_user


router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/register', response_model=UserRead, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo usuário no sistema.
    """
    return create_user(db=db, user_input=user)
