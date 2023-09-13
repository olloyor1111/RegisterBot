import psycopg2


def create_user_table():
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="telegram_bot")

        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE Users (
                    id SERIAL PRIMARY KEY,
                    telegram_id BIGINT NOT NULL UNIQUE,
                    first_name VARCHAR(100) NOT NULL,
                    last_name VARCHAR(100) NULL,
                    username VARCHAR(100) NULL
                    );""")

        connection.commit()
        print("Table created successfully in PostgreSQL ")

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL", error)


def add_user_to_db(telegram_id, first_name, last_name, username):
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="telegram_bot")

        cursor = connection.cursor()

        sql_query = "INSERT INTO Users (telegram_id, first_name, last_name, username) VALUES (%s, %s, %s, %s);"

        cursor.execute(sql_query, (telegram_id, first_name, last_name, username))

        connection.commit()

        print("User info inserted successfully to table")

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except psycopg2.Error as error:
        print(f"Error: {error}")


def select_users_info():
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="telegram_bot")

        cursor = connection.cursor()

        sql_query = "SELECT * FROM Users;"

        cursor.execute(sql_query)
        records = cursor.fetchall()
        
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        return records
    except psycopg2.Error as error:
        print(f"Error: {error}")


def create_players_table():
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="telegram_bot")

        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE Players (
                    id SERIAL PRIMARY KEY,
                    fio VARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    status VARCHAR(100) NOT NULL,
                    choice VARCHAR(100) NOT NULL,
                    phone_number VARCHAR(100) NOT NULL UNIQUE
                    );""")

        connection.commit()
        print("Table created successfully in PostgreSQL ")

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except psycopg2.Error as error:
        print("Error while connecting to PostgreSQL", error)

def add_player_to_db(fio, age, status, choice, phone_number):
    try:
        connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database="telegram_bot")

        cursor = connection.cursor()

        sql_query = "INSERT INTO Players (fio, age, status, choice, phone_number) VALUES (%s, %s, %s, %s, %s);"

        cursor.execute(sql_query, (fio, age, status, choice, phone_number))

        connection.commit()

        print("Player info inserted successfully to table")

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    except psycopg2.Error as error:
        print(f"Error: {error}")
