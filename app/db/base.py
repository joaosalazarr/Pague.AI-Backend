from sqlalchemy.orm import declarative_base, DeclarativeBase

Base: DeclarativeBase = declarative_base()

from app.models.charges import Charges
from app.models.companies import Companies
from app.models.debtors import Debtors
from app.models.debts import Debts
from app.models.transactions import Transactions
from app.models.users import Users
