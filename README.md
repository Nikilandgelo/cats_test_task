# 🌐 Project Overview
This project is a Django-based application that allows users to manage and rate cats.
The app provides a REST API for interacting with the system, enabling features like adding, editing, and deleting cats, as well as rating and filtering them based on specific criteria.
The application is fully containerized with Docker and uses PostgreSQL as its database.

## 🚀 Key Features
- 🐈 Cat Management: Easily add, edit, and delete cats.
- 🏅 User Ratings: Users can rate cats, allowing a ranking system.
- 🔎 Filtering: Filter cats by type, color, or age.
- 🐳 Dockerized Environment: Simplified deployment using Docker and Docker Compose.

## 💻 Technologies Used
- **Python 3.12**: Core language for development.
- **Django**: Backend framework for handling business logic and views.
- **Django REST Framework (DRF)**: For building the API endpoints.
- **drf-spectacular**: Used for automatic API documentation generation.
- **Docker**: For containerizing the app and its dependencies.
- **Docker Compose**: To orchestrate multi-container Docker setups (Django and PostgreSQL).

## 🛠️ Setup Instructions
### 📋 Prerequisites

- `Docker` and `Docker Compose` installed on your machine.
- A `.env` file in the root directory containing the following environment variables:
    
    ```env
    POSTGRES_USER=<your_user>
    POSTGRES_PASSWORD=<your_password>
    POSTGRES_DB=<your_database>
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    
    SECRET_KEY=<your_secret_key>
    ```
### 🚀 Running the Application
1. Clone the repository:

    ```bash
    git clone https://github.com/Nikilandgelo/cats_test_task.git
    cd cats_test_task
    ```
2. Start the services using `Docker Compose`:

   ```bash
      
    docker-compose up -d --build
     
    ```
    This command will build and start the `PostgreSQL` and **Django application** containers.
3. Access the running services:
   - `PostgreSQL`: Available on port `6666`
   - `Django`: Access the app at `http://localhost:8000`

## 📜 Usage
To load test data, use the following management command:
```bash
 
docker compose exec app python manage.py TestData -fn "test_data.json"
 
```

## 📖 API Documentation
The API documentation for all available endpoints can be accessed via `SwaggerHub`:
- https://app.swaggerhub.com/apis-docs/NIKILANDGELO/CatsTestTaskApi/1.0.0#/

## 📚 Documentation Resources
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/en/latest/index.html)
