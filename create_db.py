from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable
from models import User

CONFIG = {
    "user": "postgres",
    "password": "coderslab",
    "host": "localhost"
}

CONFIG2 = {
    "user": "postgres",
    "password": "coderslab",
    "host": "localhost",
    "database": "workshop_db"
}

sql_create_db = "CREATE DATABASE workshop_db;"
sql_create_tb_users = "CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), hashed_password VARCHAR(80));"
sql_create_tb_msg = "CREATE TABLE messages (id SERIAL PRIMARY KEY, from_id INT REFERENCES users(id), to_id INT REFERENCES users(id), creation_date TIMESTAMP);"

connection = None
try:
    connection = connect(**CONFIG)
    connection.autocommit = True
    with connection:
        with connection.cursor() as cursor:
            try:
                sql_code = sql_create_db
                cursor.execute(sql_code)
                message = "Database successfully created."
                print(message)
            except DuplicateDatabase:
                message = "Database already exists."
                print(message)
except OperationalError as err:
    message = f"An error occurred: {err}."
    print(message)
else:
    connection.close()

connection = None
try:
    connection = connect(**CONFIG2)
    connection.autocommit = True
    with connection:
        with connection.cursor() as cursor:
            try:
                sql_code = sql_create_tb_users
                cursor.execute(sql_code)
                message = "Table successfully created."
                print(message)
            except DuplicateTable:
                message = "Table already exists."
                print(message)
except OperationalError as err:
    message = f"An error occurred: {err}."
    print(message)
else:
    connection.close()

connection = None
try:
    connection = connect(**CONFIG2)
    connection.autocommit = True
    with connection:
        with connection.cursor() as cursor:
            try:
                sql_code = sql_create_tb_msg
                cursor.execute(sql_code)
                message = "Table successfully created."
                print(message)
            except DuplicateTable:
                message = "Table already exists."
                print(message)
except OperationalError as err:
    message = f"An error occurred: {err}."
    print(message)
else:
    connection.close()

u = User("Anna", "password")
u.save_user_to_db()


