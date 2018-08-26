import psycopg2
import psycopg2.extras
import os
from app.app import db

conn = db.conn
cur = db.cursor


def insert_user(users):
    cur.execute("INSERT INTO USERS(name, email, password) values(%s,%s,%s) returning id",(
        users.name,
        users.email,
        users.password))
    conn.commit()
    return cur.fetchone().get('id')


def get_user(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    if user is None:
        return None
    conn.commit()
    return user
    

def post_question(questions):
    cur.execute("INSERT INTO questions (question, date_posted, user_id) values(%s,now(),%s) returning id",(
        questions.question,
        questions.user_id))
    conn.commit()
    return cur.fetchone().get('id')

def get_questions(user_id):
    cur.execute("SELECT * FROM QUESTIONS WHERE user_id =%s",(user_id,))
    questions = cur.fetchall()
    rows = []
    for row in questions:
        rows.append(dict(row))
    if rows is None:
        return None
    conn.commit()
    return rows
    

def get_question(id):
    cur.execute("SELECT * FROM QUESTIONS WHERE id = %s", (id,))
    questions = cur.fetchone()
    if questions is None:
        return None
    conn.commit()
    return questions

def edit_question(id, question):
    cur.execute("UPDATE questions SET question = %s, date_posted = %s WHERE id = %s", (
        question['question'],
        question['date_posted'],
        id))
    conn.commit()

def delete_question(id):
    cur.execute("DELETE FROM questions WHERE id = %s", (id,))
    conn.commit()

def answer_question(answers):
    cur.execute("INSERT INTO ANSWERS (answer, date_posted, status, question_id) values(%s,%s,%s,%s) returning id",(
        answers.answer,
        answers.date_posted,
        'pending',
        answers.question_id))
    conn.commit()
    return cur.fetchone().get('id')

# def get_answer(id):
#     cur.execute("SELECT * FROM ANSWERS WHERE id = %s", (id,))
#     answers = cur.fetchone()
#     if answers is None:
#         return None
#     conn.commit()
#     return answers

# def get_answers(user_id):
#     cur.execute("SELECT * FROM ANSWERS WHERE user_id =%s",(user_id,))
#     answers = cur.fetchall()
#     rows = []
#     for row in answers:
#         rows.append(dict(row))
#     if rows is None:
#         return None
#     conn.commit()
#     return rows

# def mark_answer(id, answers):
#     cur.execute("UPDATE ANSWERS SET status = %s WHERE id = %s", (
#         answers['status'],
#         answers['id']))
#     conn.commit()


def drop_everything(self):
    self.cur.execute("DROP TABLE users;")
    self.cur.execute("DROP TABLE questions;")
    self.cur.execute("DROP TABLE answers;")
    self.conn.commit()