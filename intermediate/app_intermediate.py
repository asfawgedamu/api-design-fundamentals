# ============================================================
# INTERMEDIATE RESTAURANT API
# ============================================================
#
# TRAINING LEVEL : Intermediate
#
# ARCHITECTURE:
# Client → FastAPI → SQLite Database
#
# FEATURES:
# - SQLAlchemy ORM
# - SQLite Persistence
# - Menu Table
# - Orders Table
# - Full CRUD
# - Pydantic Validation
# - Dependency Injection
# - Pagination
# - API Versioning
# - CORS Middleware
# - Global Exception Handling
# ============================================================

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, Field, model_validator

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

from typing import List

# ============================================================
# DATABASE CONFIGURATION
# ============================================================

SQLALCHEMY_DATABASE_URL = "sqlite:///./restaurant.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# DATABASE MODELS
# ============================================================

class DBMenu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Integer, nullable=False)


class DBOrder(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String, nullable=False)
    item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)


# ============================================================
# CREATE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# MENU SEEDING
# ============================================================

def seed_menu():
    """
    Inserts default menu items only once.
    Prevents duplicate menu records after restart.
    """

    db = SessionLocal()

    try:
        menu_count = db.query(DBMenu).count()

        if menu_count == 0:

            default_menu = [
                DBMenu(name="Burger", price=250),
                DBMenu(name="Pizza", price=450),
                DBMenu(name="Pasta", price=350),
            ]

            db.add_all(default_menu)
            db.commit()

            print("Menu seeded successfully.")

    finally:
        db.close()


seed_menu()

# ============================================================
# PYDANTIC SCHEMAS
# ============================================================

class MenuResponse(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        from_attributes = True


class OrderBase(BaseModel):

    customer: str = Field(
        ...,
        min_length=2,
        max_length=50,
        example="Asfaw Gedamu"
    )

    item: str = Field(
        ...,
        min_length=2,
        max_length=50,
        example="Burger"
    )

    quantity: int = Field(
        ...,
        gt=0,
        le=20,
        example=2
    )

    @model_validator(mode="before")
    @classmethod
    def normalize(cls, values):

        if "customer" in values and isinstance(values["customer"], str):
            values["customer"] = values["customer"].strip().title()

        if "item" in values and isinstance(values["item"], str):
            values["item"] = values["item"].strip().title()

        return values

    model_config = {
        "json_schema_extra": {
            "example": {
                "customer": "Alice Smith",
                "item": "Burger",
                "quantity": 2
            }
        }
    }


class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True


# ============================================================
# DATABASE DEPENDENCY
# ============================================================

def get_db():
    """
    Dependency Injection for database sessions.
    Ensures sessions are always closed.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Restaurant API - Intermediate Version",
    description="Database-backed Restaurant Ordering API",
    version="2.0.0"
)

# ============================================================
# CORS MIDDLEWARE
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
# GLOBAL EXCEPTION HANDLER
# ============================================================

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": "An unexpected error occurred."
        }
    )

# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Intermediate Restaurant API Running Successfully!",
        "detail": "This is like saying the Restaurant is open!"
    }

# ============================================================
# MENU ENDPOINTS
# ============================================================

@app.get(
    "/api/v1/menu",
    response_model=List[MenuResponse]
)
def get_menu(
    db: Session = Depends(get_db)
):
    return db.query(DBMenu).all()

# ============================================================
# CREATE ORDER
# ============================================================

@app.post(
    "/api/v1/order",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order(
    order: OrderBase,
    db: Session = Depends(get_db)
):

    menu_item = (
        db.query(DBMenu)
        .filter(DBMenu.name.ilike(order.item))
        .first()
    )

    if not menu_item:
        raise HTTPException(
            status_code=400,
            detail="Item not found on the menu"
        )

    new_order = DBOrder(**order.model_dump())

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

# ============================================================
# READ ALL ORDERS
# ============================================================

@app.get(
    "/api/v1/orders",
    response_model=List[OrderResponse]
)
def get_orders(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    if limit > 100:
        raise HTTPException(
            status_code=400,
            detail="limit cannot exceed 100"
        )

    return (
        db.query(DBOrder)
        .offset(skip)
        .limit(limit)
        .all()
    )

# ============================================================
# READ SINGLE ORDER
# ============================================================

@app.get(
    "/api/v1/order/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = (
        db.query(DBOrder)
        .filter(DBOrder.id == order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail=f"Order {order_id} not found"
        )

    return order

# ============================================================
# UPDATE ORDER
# ============================================================

@app.put(
    "/api/v1/order/{order_id}",
    response_model=OrderResponse
)
def update_order(
    order_id: int,
    order: OrderBase,
    db: Session = Depends(get_db)
):

    existing_order = (
        db.query(DBOrder)
        .filter(DBOrder.id == order_id)
        .first()
    )

    if not existing_order:
        raise HTTPException(
            status_code=404,
            detail=f"Order {order_id} not found"
        )

    menu_item = (
        db.query(DBMenu)
        .filter(DBMenu.name.ilike(order.item))
        .first()
    )

    if not menu_item:
        raise HTTPException(
            status_code=400,
            detail="Item not found on the menu"
        )

    for key, value in order.model_dump().items():
        setattr(existing_order, key, value)

    db.commit()
    db.refresh(existing_order)

    return existing_order

# ============================================================
# DELETE ORDER
# ============================================================

@app.delete(
    "/api/v1/order/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    existing_order = (
        db.query(DBOrder)
        .filter(DBOrder.id == order_id)
        .first()
    )

    if not existing_order:
        raise HTTPException(
            status_code=404,
            detail=f"Order {order_id} not found"
        )

    db.delete(existing_order)
    db.commit()

    return None