## Concert Backend - FastAPI 

### Purpose

This backend application will serve as the 

### Installation

1. Create Folder
    - `mkdir concert_api`
    - `cd concert_api`
1. Create Environment
    - `python3 -m venv venv`
    - `source venv/bin/activate`
1. Install python modules
    - `pip install fastapi sqlalchemy databases python-jose passlib uvicorn psycopg2 sqlalchemy_utils python-multipart`
1. Create postgres database
    - create database named `concerts`
    - `python3 init_database.py`
1. Launch application
    - `uvicorn main:app --reload`
1. 