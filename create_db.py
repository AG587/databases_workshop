from psycopg2 import connect, OperationalError, DatabaseError

CONFIG = {
    "user": "postgres",
    "password": "coderslab",
    "host": "localhost"
}

def create_db():
    connection = None
    try:
        connection = connect(**CONFIG)
        with connection:
            with connection.cursor as cursor:
                try:
                    sql_code = "CREATE DATABASE workshop_db;"
                    cursor.execute(sql_code)
                except DatabaseError:
                    message = "Database already exists."
    except OperationalError as err:
        message = f"An error ocurred: {err}."
    else:
        connection.close()
        message = "Database succesfully created."

    return message



