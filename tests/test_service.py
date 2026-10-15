from decimal import Decimal

import pytest

from app.service import OrderService


def test_ids_are_incremental():
    service = OrderService()
    first = service.create("Mario", Decimal("10"))
    second = service.create("Anna", Decimal("20"))
    assert (first.id, second.id) == (1, 2)


def test_empty_customer_rejected():
    with pytest.raises(ValueError):
        OrderService().create("  ", Decimal("10"))


@pytest.mark.parametrize("amount", [Decimal("0"), Decimal("-5")])
def test_non_positive_amount_rejected(amount):
    with pytest.raises(ValueError):
        OrderService().create("Mario", amount)


def test_find_by_id():
    service = OrderService()
    order = service.create("Mario", Decimal("10"))
    assert service.find_by_id(order.id) == order
    assert service.find_by_id(999) is None


def test_find_all():
    service = OrderService()
    service.create("Mario", Decimal("10"))
    assert len(service.find_all()) == 1
