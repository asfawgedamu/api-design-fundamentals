# 🍽️ Restaurant API Project: Progressive FastAPI Labs

Welcome to the **Restaurant API Project**, a hands-on, progressive lab series designed to transform developers from **API Consumers** to **Architecture-Aware Backend Engineers**. 

Using a real-world **restaurant analogy** (Customer → Client, Waiter → Endpoint, Kitchen → Service Layer, Warehouse → Database), this repository guides you step-by-step through building production-grade REST APIs using **Python**, **FastAPI**, **SQLAlchemy**, and **Pydantic**[cite: 5].

---

## 🚀 Progressive Learning Path

This project is divided into three distinct evolutionary levels[cite: 5]. Each sub-folder contains a complete standalone application and its own detailed documentation[cite: 5, 13, 16, 25]:

| Level | Directory | Port | Focus & Architecture | Key Features |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1: Basic** | [`/basic`](./basic) | `8000` | **Fundamentals**<br>In-Memory Storage[cite: 5] | • FastAPI Basics & HTTP Methods[cite: 5]<br>• JSON Payloads & OpenAPI/Swagger UI[cite: 5]<br>• Single-file app (`app_basic.py`)[cite: 5] |
| **Level 2: Intermediate** | [`/intermediate`](./intermediate) | `8001` | **Persistence**<br>Client → API → SQLite[cite: 5, 18] | • Full CRUD Operations (POST, GET, PUT, DELETE)[cite: 5, 16]<br>• Database ORM (SQLAlchemy) & Pydantic Validation[cite: 5, 18]<br>• API Versioning (`/api/v1/`), CORS, Pagination[cite: 5, 18] |
| **Level 3: Enterprise** | [`/advanced`](./advanced) | `8002` | **Enterprise Architecture**<br>Routes → Services → DB[cite: 5, 20] | • Layered Modular Architecture (`app/routes`, `app/services`)[cite: 5, 21]<br>• Security (API Keys & JWT Authentication)[cite: 5, 20]<br>• Structured Logging, Performance Middleware, & Pytest[cite: 5, 20] |

---

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.11+[cite: 5, 9]
* **Framework:** FastAPI[cite: 5]
* **ASGI Server:** Uvicorn[cite: 5]
* **ORM & Database:** SQLAlchemy & SQLite[cite: 5]
* **Validation:** Pydantic v2[cite: 5, 11]
* **Security:** Python-Jose (JWT) & Passlib (Bcrypt)[cite: 5, 23]
* **Testing:** Pytest & HTTPX[cite: 5, 23]

---

## ⚙️ Quick Start & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/asfawgedamu/api-design-fundamentals.git](https://github.com/asfawgedamu/api-design-fundamentals.git)
cd api-design-fundamentals
