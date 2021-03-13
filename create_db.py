from psycopg2 import connect, OperationalError, DatabaseError

CONFIG = {
    "user": "postgres",
    "password": "coderslab",
    "host": "localhost"
}

sql_create_db = "CREATE DATABASE workshop_db;"
sql_create_tb_users = "CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), hashed_password VARCHAR(80);"
sql_create_tb_msg = "CREATE TABLE messages (id SERIAL PRIMARY KEY, from_id INT REFERENCES users(id), to_id INT REFERENCES users(id), creation_date TIMESTAMP);"

connection = None
try:
    connection = connect(**CONFIG)
    with connection:
        with connection.cursor() as cursor:
            try:
                sql_code = sql_create_db
                cursor.execute(sql_code)
            except DatabaseError:
                message = "Database already exists."
                print(message)
except OperationalError as err:
    message = f"An error ocurred: {err}."
    print(message)
else:
    connection.close()
    message = "Database succesfully created."
    print(message)

connection = None
try:
    connection = connect(**CONFIG)
    with connection:
        with connection.cursor() as cursor:
            try:
                sql_code = sql_create_tb_users
                cursor.execute(sql_code)
            except DatabaseError:
                message = "Table already exists."
                print(message)
except OperationalError as err:
    message = f"An error ocurred: {err}."
    print(message)
else:
    connection.close()
    message = "Table succesfully created."
    print(message)
pass

connection = None
try:
    connection = connect(**CONFIG)
    with connection:
        with connection.cursor() as cursor:
            try:
                sql_code = sql_create_tb_msg
                cursor.execute(sql_code)
            except DatabaseError:
                message = "Table already exists."
                print(message)
except OperationalError as err:
    message = f"An error ocurred: {err}."
    print(message)
else:
    connection.close()
    message = "Table succesfully created."
    print(message)

