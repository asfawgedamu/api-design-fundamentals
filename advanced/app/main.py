from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.routes.menu_routes import router as menu_router
from app.routes.order_routes import router as order_router
from app.routes.admin_routes import router as admin_router

from app.middleware.monitoring_middleware import MonitoringMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Professional Restaurant API",
    version="3.0.0"
)

app.add_middleware(MonitoringMiddleware)

app.include_router(
    menu_router,
    prefix="/api",
    tags=["Menu"]
)

app.include_router(
    order_router,
    prefix="/api",
    tags=["Orders"]
)

app.include_router(
    admin_router,
    prefix="/api",
    tags=["Admin"]
)

@app.get("/")

def home():

    return {
        "message": "Professional Restaurant API Running"
    }

@app.get("/health")

def health_check():

    return {
        "status": "healthy"
    }