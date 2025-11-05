from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.auth_service import authenticate_user
from app.schemas import *

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/login', response_model=dict, status_code=201)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Realiza o Login do usuário e retorna um token JWT.
    :param user: Obtenção do usuário usando o Pydantic
    :param db: Sessão do banco de dados
    :return: JWT
    """
    return authenticate_user(db=db, email=user.email, password=user.password)


