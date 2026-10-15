# Restaurant API
### Enterprise API Architecture | FastAPI

## 1. Project Overview

The Restaurant API is a database-backed RESTful application developed with FastAPI. It demonstrates enterprise-oriented backend development through modular architecture, separation of concerns, data validation, authentication, automated testing, logging, and performance monitoring.

This project is the advanced level of the API Design Fundamentals training labs. It builds on the basic and intermediate versions by organizing application code into dedicated modules for routes, business logic, database operations, security, and middleware.

## 2. Technology Stack

- **Language:** Python 3.11 or higher
- **API Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Authentication foundations:** API keys and JWT
- **Configuration:** Environment variables using python-dotenv
- **Password Hashing:** Passlib with bcrypt
- **Testing:** Pytest and HTTPX
- **Frontend:** HTML, CSS, JavaScript, and Jinja2
- **Monitoring:** Request timing middleware and Prometheus client dependency

## 3. Architecture

The application follows a layered architecture:

**API Client → Routes → Services → Database**

- `app/routes/`: Defines API endpoints and handles HTTP requests.
- `app/services/`: Contains business logic and application operations.
- `app/models.py`: Defines database models.
- `app/schemas.py`: Validates incoming data and structures responses.
- `app/database.py`: Configures the database engine and sessions.
- `app/security/`: Contains API-key verification, password hashing, and JWT utilities.
- `app/middleware/`: Provides request logging and performance monitoring.
- `app/config.py`: Loads environment-based configuration.
- `tests/`: Contains automated tests for orders, menu operations, and security.

This separation makes the application easier to understand, test, maintain, and extend.

## 4. Key Features

- RESTful API endpoints for restaurant menu and order operations.
- Create, read, update, and delete (CRUD) operations for orders.
- Persistent database storage using SQLite and SQLAlchemy.
- Request validation using Pydantic schemas.
- Pagination for order-list endpoints.
- API-key protection for the administrative endpoint.
- JWT creation and verification utilities.
- Password hashing utilities.
- Centralized exception handling.
- Request logging and response-time measurement.
- Health-check endpoint.
- Interactive API documentation through Swagger UI.
- Browser-based frontend integration.
- Automated testing with Pytest.

## 5. Prerequisites

Install the following before running the application:

- Python 3.11 or higher
- Visual Studio Code or another Python IDE
- Git (optional, for version control)

Familiarity with REST APIs, HTTP methods, JSON, Python, and relational databases is recommended.

## 6. Installation and Setup

### Step 1: Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3: Configure environment variables

Create a `.env` file in the project root:

```dotenv
SECRET_KEY=replace_with_a_secure_random_secret
API_KEY=replace_with_a_secure_random_api_key
DATABASE_URL=sqlite:///./restaurant.db
```

Generate a cryptographically secure secret key and configure a separate API key for the administrative endpoint.

**Security:** Never commit `.env` to source control. Ensure it is included in `.gitignore`. The example configuration is for local development, not a production deployment.

### Step 4: Start the application

```bash
python run.py
```

Alternatively:

```bash
python -m uvicorn app.main:app --reload --port 8002
```

### Step 5: Open the API documentation

- Swagger UI: http://127.0.0.1:8002/docs
- ReDoc: http://127.0.0.1:8002/redoc
- Health check: http://127.0.0.1:8002/health

These URLs assume the application is running locally on port 8002.

## 7. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Serve the frontend home page |
| GET | `/health` | Check application health |
| GET | `/api/v1/menu` | Retrieve menu items |
| POST | `/api/v1/order` | Create an order |
| GET | `/api/v1/orders` | Retrieve orders |
| GET | `/api/v1/order/{order_id}` | Retrieve a specific order |
| PUT | `/api/v1/order/{order_id}` | Update an order |
| DELETE | `/api/v1/order/{order_id}` | Delete an order |
| GET | `/api/v1/admin` | Access the API-key-protected administrative endpoint |

**Note:** Verify the registered routes in Swagger UI. The actual endpoint paths depend on how the routers and URL prefixes are configured.

### Example: Create an order

**Request**

```http
POST /api/v1/order
Content-Type: application/json
```

```json
{
  "customer": "Helen Tesfaye",
  "item": "Pizza",
  "quantity": 2
}
```

A successful request should return the created order with an HTTP `201 Created` status.

### Example: Retrieve orders with pagination

```http
GET /api/v1/orders?skip=0&limit=10
```

The `skip` parameter controls the number of records to skip, while `limit` controls the maximum number of records returned.

### Example: Access the administrative endpoint

```http
GET /api/v1/admin
x-api-key: YOUR_CONFIGURED_API_KEY
```

Requests with a missing or invalid API key should receive an HTTP `401 Unauthorized` response.

## 8. Automated Testing

Run the test suite from the project root:

```bash
pytest tests/ -v
```

The test modules cover menu retrieval, order operations, and administrative API-key validation.

Use Swagger UI, Postman, or SOAPUI for additional manual API testing.

## 9. Logging and Monitoring

The project includes request logging and middleware that measures processing time. The response-time middleware adds an `X-Process-Time` header to responses.

Application logs are intended to support troubleshooting and operational visibility. The project also includes a monitoring configuration directory for further monitoring integration.

## 10. Project Structure

```text
restaurant-api-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── config.py
│   ├── routes/
│   ├── services/
│   ├── middleware/
│   ├── security/
│   └── templates/
├── static/
├── tests/
├── logs/
├── monitoring/
├── .env
├── .gitignore
├── requirements.txt
├── restaurant.db
├── run.py
└── README.md
```

Some directories and files may be created during development. Confirm that the structure matches the actual project repository.

## 11. Security Considerations

- Keep secret keys and API credentials outside source code.
- Exclude `.env`, database files, logs, and generated Python files from version control where appropriate.
- Configure explicit allowed CORS origins for deployment.
- Validate all incoming requests.
- Use appropriate authentication and authorization controls.
- Do not expose internal exception details to API consumers.
- Review security configuration before exposing the service to external networks.

The included API-key and JWT utilities demonstrate security concepts. Their presence alone does not constitute a complete production authentication and authorization system.

## 12. Learning Outcomes

By completing this project, trainees should be able to:

- Design a modular FastAPI application.
- Separate routing, business logic, data access, and validation.
- Implement CRUD operations using a relational database.
- Apply environment-based configuration and basic security controls.
- Write and execute automated API tests.
- Implement logging, health checks, and request-time monitoring.
- Document and test APIs using OpenAPI-compatible tools.

## 13. Future Enhancements

Potential extensions include database migrations, role-based access control, refresh-token workflows, rate limiting, structured JSON logs, CI/CD automation, containerization, and deployment to a production-grade database and hosting environment.

## 14. License and Usage

This project was developed as part of the API Design Fundamentals training labs. Add a license and contribution guidelines if the repository will be distributed or maintained collaboratively.
