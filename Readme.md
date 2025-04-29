# Task Management API

A CRUD REST API built using **FastAPI**, **PostgreSQL**, and **Docker**.  

## Features

- Create, read, update, delete tasks
- RESTful API with FastAPI
- PostgreSQL database
- Dockerized for development and deployment

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-task-api.git
cd task_management
```

### 2. Create .env file for docker compose in root directory with below env variables

POSTGRES_USER=  
POSTGRES_PASSWORD=  
POSTGRES_DB=  
DATABASE_URL=  

### 2. Create .env.app file for docker compose in root directory with below env variables

DATABASE_URL=


### Run using Docker

```bash
docker-compose up --build
```
