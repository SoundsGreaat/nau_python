import psycopg2
import os

host = os.environ.get('HOST')
port = os.environ.get('PORT')
dbname = os.environ.get('DB_NAME')
user = os.environ.get('USER')
db_password = os.environ.get('DB_PASSWORD')


def init():
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=db_password)
    cursor = conn.cursor()
    return conn, cursor


def close(cursor, conn):
    cursor.close()
    conn.close()


def get_result():
    pass


def add_student(cursor, name, dob):
    pass


def add_property(cursor, student_id, property):
    pass
