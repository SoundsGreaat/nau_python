import psycopg2
import os

from psycopg2 import sql

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def init():
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()
        print('Connected to the database\n')
        return conn, cursor
    except psycopg2.Error as e:
        print(e)
        return None, None


def close(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print('Database connection closed\n')


def create_tables(conn, cursor):
    sequence_queries = [
        'CREATE SEQUENCE students_id_seq;',
        'CREATE SEQUENCE properties_id_seq;'
    ]
    table_queries = [
        '''
        CREATE TABLE students
        (
            id  INT DEFAULT nextval('students_id_seq') PRIMARY KEY,
            FIO TEXT,
            dob DATE,
            UNIQUE (FIO, dob)
        );
        ''',
        '''
        CREATE TABLE properties
        (
            id         INT DEFAULT nextval('properties_id_seq') PRIMARY KEY,
            student_id INT REFERENCES students (id),
            property   TEXT,
            UNIQUE (student_id, property)
        );
        '''
    ]

    try:
        for query in sequence_queries + table_queries:
            cursor.execute(sql.SQL(query))
        conn.commit()
        print('Tables created successfully\n')

    except psycopg2.Error:
        conn.rollback()
        print('Таблиці вже існують\n')


def add_student(conn, cursor, student_name, dob):
    try:
        cursor.execute(
            'SELECT id FROM students WHERE FIO = %s AND dob = %s',
            (student_name, dob)
        )
        existing_student = cursor.fetchone()

        if existing_student:
            return existing_student[0]
        else:
            cursor.execute(
                'INSERT INTO students (FIO, dob) VALUES (%s, %s) RETURNING id',
                (student_name, dob)
            )
            student_id = cursor.fetchone()[0]
            return student_id
    except psycopg2.Error:
        conn.rollback()


def add_properties(conn, cursor, student_id, properties, student_name):
    for prop in properties:
        try:
            cursor.execute(
                'INSERT INTO properties (student_id, property) VALUES (%s, %s)',
                (student_id, prop)
            )
            conn.commit()
        except psycopg2.Error:
            conn.rollback()
            print(f'Властивість {prop} для студента {student_name} вже існує\n')


def get_results():
    pass


if __name__ == '__main__':
    create_tables(*init())
