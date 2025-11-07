from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import Users
from app.core.security import get_password_hash
from app.schemas import UserCreate, UserRead
from uuid import uuid4

def create_user(db: Session, user_input: UserCreate) -> UserRead:
    existing_user = db.query(Users).filter(user_input.email == Users.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Um usuário com esse E-mail já foi criado')

    new_user = Users(
        id=uuid4(),
        user_name=user_input.user_name,
        email=user_input.email,
        password_hash=get_password_hash(user_input.password),
        role=user_input.role,
        company_id=user_input.company_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserRead.model_validate(new_user)
