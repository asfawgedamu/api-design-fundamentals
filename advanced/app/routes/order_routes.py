from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas import OrderCreate
from app.schemas import OrderResponse

from app.services.order_service import create_new_order
from app.services.order_service import get_all_orders

router = APIRouter()

@router.post("/order", response_model=OrderResponse)

def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    return create_new_order(db, order)

@router.get("/orders", response_model=list[OrderResponse])

def get_orders(
    db: Session = Depends(get_db)
):

    return get_all_orders(db)