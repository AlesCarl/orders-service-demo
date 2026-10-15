from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    id: int
    customer: str
    amount: Decimal
