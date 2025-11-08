"""seed initial data

Revision ID: 5f40125a0f5b
Revises: 18979853bce4
Create Date: 2025-11-07 12:00:00.000000+00:00

"""
from typing import Sequence, Union
from datetime import datetime
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "5f40125a0f5b"
down_revision: Union[str, None] = "18979853bce4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


SEED_COMPANY_ID = uuid.UUID("4ed33c8d-c50b-4c5b-9c09-145653ab9865")
SEED_USER_ID = uuid.UUID("36c3ad2a-adbd-4ab9-9fae-25d68580716b")
SEED_DEBTOR_ID = uuid.UUID("e66b07fd-f39b-41b0-bbf2-97643baca90d")
SEED_DEBT_IDS = [
    uuid.UUID("c11b9fc8-094e-4b4c-a793-845c9d8bd46e"),
    uuid.UUID("ee3401d8-9ee3-4b73-aa06-ee84bca2a681"),
    uuid.UUID("39dd1f5c-02bb-4105-9a76-fba5631c00ad"),
]

companies_table = sa.table(
    "companies",
    sa.column("id", postgresql.UUID(as_uuid=True)),
    sa.column("company_name", sa.String(length=255)),
    sa.column("company_registration_number", sa.String(length=18)),
    sa.column("address", sa.Text()),
    sa.column("created_at", sa.DateTime()),
    sa.column("updated_at", sa.DateTime()),
    sa.column("deleted_at", sa.DateTime()),
)

users_table = sa.table(
    "users",
    sa.column("id", postgresql.UUID(as_uuid=True)),
    sa.column("company_id", postgresql.UUID(as_uuid=True)),
    sa.column("user_name", sa.String(length=255)),
    sa.column("email", sa.String(length=255)),
    sa.column("password_hash", sa.String()),
    sa.column("role", sa.String(length=255)),
    sa.column("created_at", sa.DateTime()),
    sa.column("updated_at", sa.DateTime()),
    sa.column("deleted_at", sa.DateTime()),
)

debtors_table = sa.table(
    "debtors",
    sa.column("id", postgresql.UUID(as_uuid=True)),
    sa.column("debtor_name", sa.String(length=255)),
    sa.column("contact", sa.String(length=255)),
    sa.column("debtor_cpf", sa.String(length=14)),
    sa.column("created_at", sa.DateTime()),
    sa.column("updated_at", sa.DateTime()),
    sa.column("deleted_at", sa.DateTime()),
)

debts_table = sa.table(
    "debts",
    sa.column("id", postgresql.UUID(as_uuid=True)),
    sa.column("debtor_id", postgresql.UUID(as_uuid=True)),
    sa.column("company_id", postgresql.UUID(as_uuid=True)),
    sa.column("debt_value", sa.Float()),
    sa.column("debt_status", sa.Boolean()),
    sa.column("created_at", sa.DateTime()),
    sa.column("updated_at", sa.DateTime()),
    sa.column("deleted_at", sa.DateTime()),
)


def upgrade() -> None:
    _insert_seed_data()


def downgrade() -> None:
    _delete_seed_data()


def _insert_seed_data() -> None:
    now = datetime.utcnow()

    op.bulk_insert(
        companies_table,
        [
            {
                "id": SEED_COMPANY_ID,
                "company_name": "Pague.AI Demo LTDA",
                "company_registration_number": "12.345.678/0001-90",
                "address": "Av. Paulista, 1000 - Sao Paulo/SP",
                "created_at": now,
                "updated_at": now,
                "deleted_at": None,
            },
        ],
    )

    op.bulk_insert(
        users_table,
        [
            {
                "id": SEED_USER_ID,
                "company_id": SEED_COMPANY_ID,
                "user_name": "Administrador Demo",
                "email": "admin.demo@pague.ai",
                "password_hash": "$2b$12$nqXrRAxzLVifVsQnuPWaUu5ClJk5KKLKRWfoYJKoMJowkqpdXJAm.",
                "role": "ADMIN",
                "created_at": now,
                "updated_at": now,
                "deleted_at": None,
            },
        ],
    )

    op.bulk_insert(
        debtors_table,
        [
            {
                "id": SEED_DEBTOR_ID,
                "debtor_name": "Joao da Silva",
                "contact": "+55 (11) 99999-9999",
                "debtor_cpf": "123.456.789-01",
                "created_at": now,
                "updated_at": now,
                "deleted_at": None,
            },
        ],
    )

    op.bulk_insert(
        debts_table,
        [
            {
                "id": SEED_DEBT_IDS[0],
                "debtor_id": SEED_DEBTOR_ID,
                "company_id": SEED_COMPANY_ID,
                "debt_value": 2500.75,
                "debt_status": False,
                "created_at": now,
                "updated_at": now,
                "deleted_at": None,
            },
            {
                "id": SEED_DEBT_IDS[1],
                "debtor_id": SEED_DEBTOR_ID,
                "company_id": SEED_COMPANY_ID,
                "debt_value": 1800.00,
                "debt_status": True,
                "created_at": now,
                "updated_at": now,
                "deleted_at": None,
            },
            {
                "id": SEED_DEBT_IDS[2],
                "debtor_id": SEED_DEBTOR_ID,
                "company_id": SEED_COMPANY_ID,
                "debt_value": 950.50,
                "debt_status": False,
                "created_at": now,
                "updated_at": now,
                "deleted_at": None,
            },
        ],
    )


def _delete_seed_data() -> None:
    for debt_id in SEED_DEBT_IDS:
        op.execute(
            sa.text("DELETE FROM debts WHERE id = :debt_id"),
            {"debt_id": str(debt_id)},
        )

    op.execute(
        sa.text("DELETE FROM users WHERE id = :user_id"),
        {"user_id": str(SEED_USER_ID)},
    )

    op.execute(
        sa.text("DELETE FROM debtors WHERE id = :debtor_id"),
        {"debtor_id": str(SEED_DEBTOR_ID)},
    )

    op.execute(
        sa.text("DELETE FROM companies WHERE id = :company_id"),
        {"company_id": str(SEED_COMPANY_ID)},
    )
