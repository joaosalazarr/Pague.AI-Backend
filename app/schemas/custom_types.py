from pydantic import StringConstraints, Field
from typing import Annotated
from decimal import Decimal

ConstrainedString: type[str] = Annotated[str, StringConstraints(min_length=3, max_length=255)]
Monetary: type[Decimal] = Annotated[Decimal, Field(gt=0, max_digits=10, decimal_places=2)]
