# FastAPI Food Delivery Application

This project is a FastAPI application designed for managing users and their food delivery orders. It utilizes SQLAlchemy for ORM and SQLite as the database.

## Features

- User registration and authentication using API tokens.
- Create, retrieve, and manage food delivery orders.
- Secure access to user and order data.
- Simple and intuitive API endpoints.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **SQLAlchemy**: An ORM for database interactions.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **SQLite**: A lightweight database for development and testing.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fastapi-gp
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI application:

   ```bash
   uvicorn app:app --reload
   ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### User Endpoints

- **Create User**

  - `POST /create_user`
  - Request Body: `{"name": "string", "email": "string"}`
  - Response: User details with API token.

- **Get User**
  - `GET /user/{user_id}`
  - Response: User details.

### Order Endpoints

- **Create Order**

  - `POST /create_order`
  - Request Body: Order details.
  - Response: Created order details.

- **Get User Orders**

  - `GET /user/{user_id}/orders`
  - Response: List of orders for the specified user.

- **Get Order**
  - `GET /order/{order_id}`
  - Response: Order details.

## Database

The application uses SQLite for data storage. The database file is named `database.db` and is created automatically upon running the application.
