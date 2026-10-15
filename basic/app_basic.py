# ============================================================
# BASIC RESTAURANT API
# ============================================================
#
# TRAINING LEVEL : Beginner / Fundamentals
#
# PURPOSE:
# Introduces the core concepts of:
# - REST APIs
# - FastAPI framework
# - HTTP Methods
# - Request Body
# - Response Body
# - JSON Data Exchange
# - Pydantic Validation
# - Swagger/OpenAPI Documentation
#
# REAL-WORLD ANALOGY:
# Restaurant = API Application
# Customer = API Client
# Waiter = API Endpoint
# Menu = Data Resource
#
# ============================================================

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# ============================================================
# APPLICATION INITIALIZATION
# ============================================================
#
# PURPOSE:
# Creates the FastAPI application object.
#
# ANALOGY:
# This is the restaurant building.
# Every service offered by the restaurant belongs here.
#
# ============================================================

app = FastAPI(
    title="Restaurant API - Basic Version",
    description="Beginner API demonstrating REST fundamentals",
    version="1.0.0"
)

# ============================================================
# GLOBAL EXCEPTION HANDLER
# ============================================================
#
# PURPOSE:
# Prevent raw Python errors from being shown to clients.
#
# BENEFIT:
# Returns a clean JSON response whenever an unexpected
# server-side error occurs.
#
# ============================================================

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": "An unexpected error occurred. Please try again."
        }
    )

# ============================================================
# REQUEST MODEL
# ============================================================
#
# PURPOSE:
# Defines the structure of incoming JSON data.
#
# FASTAPI FEATURE:
# Automatic validation occurs before endpoint execution.
#
# EXAMPLE REQUEST JSON:
#
# {
#     "name": "Shawarma",
#     "price": 300
# }
#
# ============================================================

class MenuItem(BaseModel):

    name: str
    price: float

# ============================================================
# IN-MEMORY DATA STORE
# ============================================================
#
# PURPOSE:
# Simulates a database table.
#
# IMPORTANT:
# Data is lost when the server restarts.
#
# LEVEL 2:
# This will be replaced by PostgreSQL.
#
# ============================================================

menu = [
    {"id": 1, "name": "Burger", "price": 250},
    {"id": 2, "name": "Pizza",  "price": 450},
    {"id": 3, "name": "Pasta",  "price": 350}
]

# ============================================================
# HOME ENDPOINT
# ============================================================
#
# HTTP METHOD:
# GET
#
# URL:
# /
#
# PURPOSE:
# Confirms that the API server is running.
#
# ANALOGY:
# Customer asks:
# "Are you open today?"
#
# SAMPLE RESPONSE:
#
# {
#     "message": "Restaurant API Running Successfully"
# }
#
# ============================================================

@app.get("/")

def home():

    return {
        "message": "Restaurant API Running Successfully"
    }

# ============================================================
# GET MENU ENDPOINT
# ============================================================
#
# HTTP METHOD:
# GET
#
# URL:
# /api/v1/menu
#
# PURPOSE:
# Returns all available menu items.
#
# ANALOGY:
# Customer asks:
# "What meals are available today?"
#
# SAMPLE RESPONSE:
#
# [
#     {
#         "id": 1,
#         "name": "Burger",
#         "price": 250
#     },
#     {
#         "id": 2,
#         "name": "Pizza",
#         "price": 450
#     }
# ]
#
# ============================================================

@app.get("/api/v1/menu")

def get_menu():

    return menu

# ============================================================
# CREATE MENU ITEM ENDPOINT
# ============================================================
#
# HTTP METHOD:
# POST
#
# URL:
# /api/v1/menu
#
# PURPOSE:
# Creates a new menu item.
#
# ANALOGY:
# Restaurant manager adds a new meal
# to the restaurant menu.
#
# REQUEST BODY:
#
# {
#     "name": "Shawarma",
#     "price": 300
# }
#
# SUCCESS RESPONSE:
#
# {
#     "message": "Menu item added successfully",
#     "item": {
#         "id": 4,
#         "name": "Shawarma",
#         "price": 300
#     }
# }
#
# ============================================================

@app.post("/api/v1/menu")

def create_menu_item(item: MenuItem):

    new_item = {
        "id": len(menu) + 1,
        "name": item.name,
        "price": item.price
    }

    menu.append(new_item)

    return {
        "message": "Menu item added successfully",
        "item": new_item
    }
    
    
    # ============================================================
# GET MENU ENDPOINT
# ============================================================
#
# HTTP METHOD:
# GET
#
# URL:
# /api/v1/menu
#
# PURPOSE:
# Returns all available menu items.
#
# ANALOGY:
# Customer asks:
# "What meals are available today?"
#
# SWAGGER SUMMARY:
# Retrieve all menu items
#
# SWAGGER DESCRIPTION:
# Returns the complete restaurant menu currently
# available for customers.
#
# SAMPLE RESPONSE:
#
# [
#     {
#         "id": 1,
#         "name": "Burger",
#         "price": 250
#     },
#     {
#         "id": 2,
#         "name": "Pizza",
#         "price": 450
#     }
# ]
#
# ============================================================

@app.get(
    "/api/v1/menu",
    tags=["Menu"],
    summary="Retrieve all menu items",
    description="""
Returns the complete restaurant menu.

This endpoint demonstrates:

- HTTP GET method
- JSON responses
- Resource retrieval
- REST API fundamentals

No request body is required.
""",
    response_description="List of available menu items"
)
def get_menu():

    return menu

# ============================================================
# CREATE MENU ITEM ENDPOINT
# ============================================================
#
# HTTP METHOD:
# POST
#
# URL:
# /api/v1/menu
#
# PURPOSE:
# Creates a new menu item.
#
# ANALOGY:
# Restaurant manager adds a new meal
# to the restaurant menu.
#
# SWAGGER SUMMARY:
# Create a new menu item
#
# FastAPI automatically generates an OpenAPI specification and Swagger displays the data models it found.

# SWAGGER DESCRIPTION:
# Accepts JSON data and creates a new menu item.
#
# REQUEST BODY:
#
# {
#     "name": "Shawarma",
#     "price": 300
# }
#
# SUCCESS RESPONSE:
#
# {
#     "message": "Menu item added successfully",
#     "item": {
#         "id": 4,
#         "name": "Shawarma",
#         "price": 300
#     }
# }
#
# ============================================================

@app.post(
    "/api/v1/menu",
    tags=["Menu"],
    summary="Create a new menu item",
    description="""
Creates a new restaurant menu item.

This endpoint demonstrates:

- HTTP POST method
- Request body processing
- JSON input validation
- Resource creation
- Pydantic models

Clients must provide a JSON request body.
""",
    response_description="Newly created menu item"
)
def create_menu_item(item: MenuItem):

    new_item = {
        "id": len(menu) + 1,
        "name": item.name,
        "price": item.price
    }

    menu.append(new_item)

    return {
        "message": "Menu item added successfully",
        "item": new_item
    }
    
    
    