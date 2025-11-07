from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import Companies
from app.schemas import CompanyCreate, CompanyRead
from uuid import uuid4


def create_company(db: Session, company_input: CompanyCreate):
    existing_company = db.query(Companies).filter(company_input.company_registration_number ==
                                                  Companies.company_registration_number).first()

    if existing_company:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Empresa com esse número de registro já cadastrada')

    new_company = Companies(
        id=uuid4(),
        company_name=company_input.company_name,
        company_registration_number=company_input.company_registration_number,
        address=company_input.address
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return CompanyRead.model_validate(new_company)
