from decimal import Decimal

from app.models import Order


class OrderService:
    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def create(self, customer: str, amount: Decimal) -> Order:
        if not customer or not customer.strip():
            raise ValueError("customer must not be empty")
        if amount <= 0:
            raise ValueError("amount must be greater than zero")
        order = Order(id=self._next_id, customer=customer, amount=amount)
        self._orders[order.id] = order
        self._next_id += 1
        return order

    def find_by_id(self, order_id: int) -> Order | None:
        return self._orders.get(order_id)

    def find_all(self) -> list[Order]:
        return list(self._orders.values())
