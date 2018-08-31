
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from .databas.db import Database

db_details = "dbname='stackoverflowlite'  user='postgres'  host='localhost'  password='root'"
conn = psycopg2.connect(db_details)
cur = conn.cursor()

def insert_user(user):
    cur.execute("INSERT INTO tbl_users(name, email, password) values(%s,%s,%s) returning id",(
        user.name,
        user.email,
        user.password))
    conn.commit()
    ret = cur.fetchone()
    return ret[0]


def get_user(email):

    cur.execute("SELECT * FROM tbl_users WHERE email = %s", (email,))
    user = cur.fetchone()
    if user is None:
        return None
    return user[2]

def login_user(email, password):
    cur.execute("SELECT * FROM tbl_users WHERE email = %s, password = %s", (email,password,))
    user = cur.fetchone()
    if user is None:
        return None
    return user


def post_question(questions):
    cur.execute("INSERT INTO tbl_questions (question, date_posted, user_id) values(%s,now(),%s) returning id",(
        questions.question,
        questions.user_id))
    conn.commit()
    id = cur.fetchone()

    return id[0]

def get_questions(user_id):
    cur.execute("SELECT * FROM tbl_questions WHERE user_id =%s",([user_id],))
    questions = cur.fetchall()
    rows = []
    for row in questions:
        rows.append(dict(row))
    if rows is None:
        return None
    conn.commit()
    return rows


def get_question(id):
    cur.execute("SELECT * FROM tbl_questions WHERE id = %s", [id])
    questions = cur.fetchone()
    if questions is None:
        return None
    conn.commit()
    return questions

def edit_question(id, question):
    cur.execute("UPDATE tbl_questions SET question = %s, date_posted = %s WHERE id = %s", (
        question['question'],
        question['date_posted'],
        id))
    conn.commit()

def delete_question(id):
    cur.execute("DELETE FROM tbl_questions WHERE id = %s", [id])
    conn.commit()

def answer_question(answers):

    cur.execute("INSERT INTO tbl_answers (answer, date_posted, question_id) values(%s,%s,%s) returning id",(\
        answers.answer,\
        answers.date_posted,\
        int(answers.question_id[3])))
    conn.commit()
    id = cur.fetchone()
    return id[0]



def drop_tables():
    cur.execute("DROP TABLE tbl_answers;")
    cur.execute("DROP TABLE tbl_questions;")
    cur.execute("DROP TABLE tbl_users;")
    conn.commit()
