'''import psycopg2, psycopg2.extras, os
from psycopg2.extras import RealDictCursor

db_details = "dbname='stackoverflow'  user='postgres'  host='localhost'  password='root'"
conn = psycopg2.connect(db_details)
cur = conn.cursor(cursor_factory=RealDictCursor)

from .databas.db import Database

def migrate():

    queries = [
        """CREATE TABLE IF NOT EXISTS tbl_users(
        id serial PRIMARY KEY,
        name varchar,
        email varchar UNIQUE,
        password varchar
        )""",

         """CREATE TABLE IF NOT EXISTS tbl_questions(
        id serial PRIMARY KEY,
        question varchar,
        date_posted TIMESTAMP,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES tbl_users(id)
    )""",

    """CREATE TABLE IF NOT EXISTS tbl_answers(
        id serial PRIMARY KEY,
        answer varchar,
        date_posted TIMESTAMP,
        question_id INT,
        FOREIGN KEY (question_id) REFERENCES tbl_questions(id)
    )"""
    ]

    for query in queries:
        cur.execute(query)
        conn.commit()

def drop_tables():
    cur.execute("DROP TABLE tbl_answers;")
    cur.execute("DROP TABLE tbl_questions;")
    cur.execute("DROP TABLE tbl_users;")
    conn.commit()
'''
