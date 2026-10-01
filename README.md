# Mastering FastAPI

> A hands-on FastAPI learning lab: small, focused examples that build from a first route to database-backed CRUD, authentication, file handling, middleware, and external API integrations.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/license-learning%20project-lightgrey)

## Why this repository?

FastAPI is easiest to learn by running small examples and changing them. This repository keeps each concept close to the code that demonstrates it, making it useful for:

- learning FastAPI one concept at a time;
- experimenting with request validation and response serialization;
- understanding dependency injection and middleware;
- practicing CRUD with both in-memory data and SQLite/SQLAlchemy;
- trying authentication, file uploads, web crawling, and third-party APIs.

The files are intentionally independent examples rather than one production application. Start with one file, inspect its routes, and open the generated API docs.

## What is covered?

| Topic | Example |
| --- | --- |
| First routes and async handlers | [`async.py`](./async.py), [`req_res_handling_err_basis.py`](./req_res_handling_err_basis.py) |
| Pydantic models and CRUD | [`basics.py`](./basics.py) |
| Path and query parameters | [`path_parameter_query_basic_crud.py`](./path_parameter_query_basic_crud.py) |
| Multiple parameters and request bodies | [`multiple_parameter.py`](./multiple_parameter.py) |
| Response models | [`response_model.py`](./response_model.py) |
| Dependency injection and header validation | [`dependency_injection.py`](./dependency_injection.py) |
| Custom exceptions and error handling | [`http_exception_custom.py`](./http_exception_custom.py) |
| Middleware and request timing | [`middleware.py`](./middleware.py) |
| CORS and environment-based configuration | [`cors.py`](./cors.py), [`cors_with_env.py`](./cors_with_env.py), [`config.py`](./config.py), [`env.py`](./env.py) |
| File uploads and serving files | [`fileupload.py`](./fileupload.py) |
| JWT authentication | [`jwt.py`](./jwt.py) |
| SQLAlchemy with SQLite | [`database_connection.py`](./database_connection.py), [`SqlALchemy.py`](./SqlALchemy.py), [`sqlALchemy_template_db_connection.py`](./sqlALchemy_template_db_connection.py) |
| SQLite fundamentals | [`sqllite.py`](./sqllite.py) |
| Third-party API calls | [`third_party_api_integration.py`](./third_party_api_integration.py) |
| Pagination and HTML scraping | [`pagination.py`](./pagination.py), [`web_crawling.py`](./web_crawling.py) |

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/AkshatSinghNayal/mastering-fastAPI.git
cd mastering-fastAPI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows PowerShell
```

### 3. Install the core dependency

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The repository's examples also use a few topic-specific packages. Install them when working through those examples:

```bash
pip install sqlalchemy python-dotenv python-jose[cryptography] requests beautifulsoup4
```

### 4. Run an example

Every example that exposes an `app = FastAPI()` object can be started with Uvicorn:

```bash
uvicorn basics:app --reload
```

Then visit:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI;
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) for ReDoc.

To run a different example, replace `basics` with the filename without `.py`:

```bash
uvicorn fileupload:app --reload
uvicorn database_connection:app --reload
uvicorn jwt:app --reload
```

> **Note:** `async.py` is an example module, so run it with `uvicorn async:app --reload`. Avoid importing it as a normal Python module because `async` is a Python keyword.

## Example API: in-memory TODO CRUD

[`basics.py`](./basics.py) demonstrates a complete CRUD flow using a Pydantic model and an in-memory list:

| Method | Route | Purpose |
| --- | --- | --- |
| `POST` | `/todos` | Create a TODO |
| `GET` | `/todos` | List TODOs |
| `GET` | `/todos/{id}` | Get one TODO |
| `PUT` | `/update/{id}` | Update a TODO |
| `DELETE` | `/delete/{id}` | Delete a TODO |

Example request:

```bash
curl -X POST "http://127.0.0.1:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Learn FastAPI", "description": "Build a small API", "completed": false}'
```

## Database examples

The SQLAlchemy examples use SQLite and create/use [`test.db`](./test.db). The database-backed CRUD example includes endpoints for:

- listing all records;
- creating a TODO;
- retrieving a record by ID;
- updating a record;
- deleting a record.

The database session is supplied to route handlers through FastAPI's `Depends`, which makes the examples a useful introduction to request-scoped dependencies.

## Authentication and configuration

[`jwt.py`](./jwt.py) demonstrates issuing and validating JWTs. [`config.py`](./config.py) and [`cors_with_env.py`](./cors_with_env.py) demonstrate loading configuration from environment variables.

For local experiments, create a `.env` file (it is ignored by Git):

```env
SECRET_KEY=replace-this-with-a-long-random-value
ORIGINS=http://localhost:3000
```

Do not use the sample secrets or hard-coded demo values in a real application. Rotate credentials and use a proper secret-management solution before deployment.

## Suggested learning path

1. Start with [`basics.py`](./basics.py) and inspect `/docs`.
2. Compare path/query parameters in [`path_parameter_query_basic_crud.py`](./path_parameter_query_basic_crud.py).
3. Add typed responses with [`response_model.py`](./response_model.py).
4. Learn reusable dependencies in [`dependency_injection.py`](./dependency_injection.py).
5. Move from in-memory data to SQLite in [`database_connection.py`](./database_connection.py).
6. Explore middleware, CORS, uploads, and custom errors.
7. Finish with JWTs, pagination, web crawling, and third-party API calls.

## Project layout

```text
.
├── basics.py                         # In-memory TODO CRUD
├── database_connection.py            # SQLAlchemy + SQLite CRUD
├── dependency_injection.py           # Header validation with Depends
├── fileupload.py                     # Upload and serve files
├── jwt.py                            # JWT login and protected route
├── middleware.py                     # Request middleware
├── pagination.py                     # Paginated scraped data
├── response_model.py                 # Response filtering with Pydantic
├── third_party_api_integration.py    # External API requests
├── web_crawling.py                   # HTML parsing example
├── uploads/                          # Files used by the upload example
├── requirements.txt                  # Core FastAPI dependency
└── test.db                           # Local SQLite database used by examples
```

## Notes for contributors

- Keep examples small and focused on one FastAPI concept.
- Prefer a separate file when introducing a new concept.
- Update this README when adding a new runnable example.
- Never commit real credentials, tokens, or private uploaded files.

## License

This project is intended for learning and experimentation. Add a project license before distributing it as a reusable library or application.