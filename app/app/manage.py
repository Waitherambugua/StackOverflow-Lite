import psycopg2, psycopg2.extras, os
from psycopg2.extras import RealDictCursor
from db import Database
from . import db

db_details = "dbname='stackoverflow'  user='postgres'  host='localhost'  password='root'"
conn = psycopg2.connect(db_details)
cur = conn.cursor(cursor_factory=RealDictCursor)



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
        status varchar,
        question_id INT,
        FOREIGN KEY (question_id) REFERENCES tbl_questions(id)
    )"""
    ]
    
    for query in queries:
        cur.execute(query)
        conn.commit()
    
 
