from decimal import Decimal

from fastapi import FastAPI

from app.service import OrderService

app = FastAPI(title="Orders Service")

service = OrderService()
service.create("Mario Rossi", Decimal("49.90"))
service.create("Giulia Bianchi", Decimal("120.00"))


@app.get("/orders")
def list_orders():
    return [
        {"id": o.id, "customer": o.customer, "amount": str(o.amount)}
        for o in service.find_all()
    ]


@app.get("/health")
def health():
    return {"status": "UP"}    
