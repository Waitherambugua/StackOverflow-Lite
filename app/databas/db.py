
import psycopg2
from psycopg2.extras import RealDictCursor


class Database(object):

    cursor = None
    db_details = "dbname='stackoverflowlite'  user='postgres'  host='localhost'  password='root'"
    conn = psycopg2.connect(db_details)
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    @classmethod
    def init_app(cls, app):

        """
                local credentials
                cls.dbhost = '127.0.0.1'
                cls.dbname = 'stackoveflow'
                cls.dbuser = 'Linda'
                cls.dbpassword = 'yes'

                postgres credentials
                cls.db_postgres_host = '127.0.0.1'
                cls.db_postgres_dbname = 'postgres'
                cls.db_postgres_user = 'postgres'
                cls.db_postgres_password = 'root'
        """
        tables = [

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
            ON UPDATE CASCADE ON DELETE CASCADE
        )""",

        """CREATE TABLE IF NOT EXISTS tbl_answers(
            id serial PRIMARY KEY,
            answer varchar,
            date_posted TIMESTAMP,
            question_id INT,
            FOREIGN KEY (question_id) REFERENCES tbl_questions(id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )"""

        ]

        for query in tables:
            cls.cursor.execute(query)
            cls.conn.commit()

    @classmethod
    def drop_tables(cls):

        cls.cursor.execute("DROP TABLE tbl_answers;")
        cls.cursor.execute("DROP TABLE tbl_questions;")
        cls.cursor.execute("DROP TABLE tbl_users;")
        cls.conn.commit()


    '''@classmethod
    def create_tables(cls):
        conn = None

        try:
            # read the connection parameters
            params = "dbname='stackoverflow'  user='postgres'  host='localhost'  password='root'"
            #params = config()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(params)
            cur = conn.cursor()
            # create table one by one
            for command in cls.tables:
                cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()'''
