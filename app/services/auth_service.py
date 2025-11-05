from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.users import Users
from app.core.security import verify_password, create_acess_token
from fastapi import HTTPException, status


def authenticate_user(db: Session, email: EmailStr, password: str) -> dict:
    user: Users | None = db.query(Users).filter(email == Users.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuário não encontrado')

    if not verify_password(plain_password=password, hashed_password=user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Senha incorreta')

    token = create_acess_token({'sub': user.email, 'user_id': str(user.id)})

    return {'acess_token': token, 'token_type': 'bearer'}
