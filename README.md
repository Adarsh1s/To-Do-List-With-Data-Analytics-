# To-Do List with Data Analytics

## Overview
A collaborative To-Do List web app with data analytics using Django, PostgreSQL, and Streamlit.

## Features
- Task management with Django backend
- PostgreSQL database for secure and scalable storage
- Streamlit UI for an interactive frontend
- Data analytics with Pandas and Matplotlib

## Project Structure
```
todo_list_analytics/
│── backend/                   # Django backend
│   ├── backend/               # Django project settings
│   ├── tasks/                 # Django app for tasks
│   ├── manage.py
│── frontend/                  # Streamlit frontend
│   ├── app.py
│── venv/                      # Virtual environment
│── requirements.txt
│── .gitignore
│── README.md
```

## Prerequisites
- Python 3.13.2
- PostgreSQL 17.4 installed
- Git installed

## Setup Guide

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/todo_list_analytics.git
cd todo_list_analytics
```

### 2. Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database
1. Create a PostgreSQL database.
2. Update `backend/settings.py` with database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 5. Apply Database Migrations
```sh
cd backend
python manage.py migrate
```

### 6. Run Django Development Server
```sh
python manage.py runserver
```

### 7. Start Streamlit Frontend
```sh
cd ../frontend
streamlit run app.py
```

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to your branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

---

### `requirements.txt`
```
django
djangorestframework
psycopg2
streamlit
pandas
matplotlib
```

## Basic Django Commands
### Create a New Django Project
```sh
django-admin startproject projectname
```
### Create a New Django App
```sh
python manage.py startapp appname
```
### Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
### Create Superuser
```sh
python manage.py createsuperuser
```
### Run Django Shell
```sh
python manage.py shell
```

## Basic PostgreSQL Commands
### Login to PostgreSQL
```sh
psql -U postgres
```
### Create a New Database
```sql
CREATE DATABASE database_name;
```
### List Databases
```sql
\l
```
### Connect to a Database
```sql
\c database_name;
```
### Create a New User
```sql
CREATE USER username WITH PASSWORD 'password';
```
### Grant Privileges
```sql
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```
### Exit PostgreSQL
```sh
\q
```

## Basic Streamlit Commands
### Run Streamlit App
```sh
streamlit run app.py
```
### Show Text
```python
import streamlit as st
st.write("Hello, Streamlit!")
```
### Create a Button
```python
if st.button("Click Me"):
    st.write("Button Clicked!")
```
### Create a Text Input
```python
user_input = st.text_input("Enter something:")
st.write("You entered:", user_input)
```
### Create a Chart
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
st.line_chart(data)
```



