import pytest
from uuid import uuid4
from decimal import Decimal
from datetime import datetime, UTC

# Importa todos os schemas
from app.schemas.user import UserCreate, UserLogin, UserRead
from app.schemas.company import CompanyCreate, CompanyRead
from app.schemas.debtor import DebtorCreate, DebtorRead
from app.schemas.debt import DebtCreate, DebtRead
from app.schemas.transaction import TransactionCreate, TransactionRead
from app.schemas.charge import ChargeCreate, ChargeRead


# --- USER ---
def test_user_create_valid():
    user = UserCreate(
        user_name="João",
        role="Dev",
        company_id=uuid4(),
        password="1234",
        email="joao@email.com",
    )
    assert user.email == "joao@email.com"
    assert user.user_name == "João"


def test_user_login_valid():
    login = UserLogin(email="test@email.com", password="123")
    assert login.email == "test@email.com"


# --- COMPANY ---
def test_company_create_valid():
    company = CompanyCreate(
        company_name="Pague.AI",
        company_registration_number="12.345.678/0001-99",
        address="Rua das Startups, 123",
    )
    assert company.company_name == "Pague.AI"


def test_company_read_valid():
    company = CompanyRead(
        id=uuid4(),
        company_name="FacensTech",
        company_registration_number="00.111.222/0001-33",
        address=None,
    )
    assert company.address is None


# --- DEBTOR ---
def test_debtor_create_valid():
    debtor = DebtorCreate(debtor_name="Cliente Inadimplente", contact="(15) 99999-9999")
    assert debtor.debtor_name.startswith("Cliente")


# --- DEBT ---
def test_debt_create_valid():
    debt = DebtCreate(
        debtor_id=uuid4(),
        debt_value=Decimal("500.00"),
        debt_status=False,
        company_id=uuid4(),
    )
    assert debt.debt_value == Decimal("500.00")


# --- TRANSACTION ---
def test_transaction_create_valid():
    transaction = TransactionCreate(
        debt_id=uuid4(),
        paid_amount=Decimal("500.00"),
    )
    assert isinstance(transaction.payment_date, datetime)
    assert transaction.paid_amount > 0


# --- CHARGE ---
def test_charge_create_valid():
    charge = ChargeCreate(
        debt_id=uuid4(),
        message_midst="Lembrete de pagamento",
        send_status=True,
    )
    assert charge.send_status is True
    assert charge.message_midst == "Lembrete de pagamento"
    assert isinstance(charge.charge_date, datetime)
