# Restaurant API — Intermediate Version

A database-backed REST API for restaurant ordering, built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

---

## Features

- SQLAlchemy ORM with SQLite persistence
- Full CRUD for orders
- Menu seeding on startup
- Pydantic v2 request validation
- Dependency injection for DB sessions
- Pagination on order listing
- API versioning (`/api/v1/`)
- CORS middleware
- Global exception handling

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | SQLite (`restaurant.db`) |
| Validation | Pydantic v2 |
| Language | Python 3.10+ |

---

## Getting Started

### 1. Install dependencies

```bash
pip install fastapi sqlalchemy uvicorn
```

### 2. Run the server

```bash
uvicorn app_intermediate:app --reload
```

### 3. Open interactive docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Database

The app uses a local SQLite file (`restaurant.db`) created automatically on first run.

### Tables

**`menu`**

| Column | Type | Notes |
|---|---|---|
| `id` | Integer | Primary key |
| `name` | String | Unique, not null |
| `price` | Integer | In local currency units |

**`orders`**

| Column | Type | Notes |
|---|---|---|
| `id` | Integer | Primary key |
| `customer` | String | Not null |
| `item` | String | Must match a menu item |
| `quantity` | Integer | 1–20 |

### Seeded Menu (on first run)

| Item | Price |
|---|---|
| Burger | 250 |
| Pizza | 450 |
| Pasta | 350 |

---

## API Reference

Base URL: `/api/v1`

### Health Check

```
GET /
```

### Menu

```
GET /api/v1/menu
```

Returns all available menu items.

### Orders

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/order` | Place a new order |
| `GET` | `/api/v1/orders` | List all orders (paginated) |
| `GET` | `/api/v1/order/{id}` | Get a single order |
| `PUT` | `/api/v1/order/{id}` | Update an existing order |
| `DELETE` | `/api/v1/order/{id}` | Delete an order |

### Pagination

`GET /api/v1/orders` supports `skip` and `limit` query parameters:

```
GET /api/v1/orders?skip=0&limit=10
```

> `limit` cannot exceed 100.

---

## Request & Response Examples

### Place an Order

**Request**
```json
POST /api/v1/order
{
  "customer": "Asfaw Gedamu",
  "item": "Burger",
  "quantity": 2
}
```

**Response** `201 Created`
```json
{
  "id": 1,
  "customer": "Asfaw Gedamu",
  "item": "Burger",
  "quantity": 2
}
```

### Validation Rules

| Field | Rules |
|---|---|
| `customer` | 2–50 characters, auto title-cased |
| `item` | 2–50 characters, must exist on the menu |
| `quantity` | Integer between 1 and 20 |

---

## Error Handling

| Status | Meaning |
|---|---|
| `400` | Bad request (invalid item, limit exceeded) |
| `404` | Order not found |
| `500` | Unexpected server error |

---

## Project Structure

```
.
├── app_intermediate.py   # Main application
└── restaurant.db         # SQLite database (auto-created)
```

---

## Notes

- CORS is open (`allow_origins=["*"]`) — restrict this in production.
- Item names are matched case-insensitively against the menu.
- Customer and item names are automatically normalized (stripped and title-cased).