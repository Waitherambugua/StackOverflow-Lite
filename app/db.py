
import psycopg2
from psycopg2.extras import RealDictCursor


class Database(object):
 
    cursor = None

    @classmethod
    def init_app(cls, app):
        db_details = "dbname='stackoverflowlite'  user='postgres'  host='localhost'  password='root'"
        cls.conn = psycopg2.connect(db_details)
        cls.cursor = cls.conn.cursor(cursor_factory=RealDictCursor)

        """ local credentials """
        cls.dbhost = '127.0.0.1'
        cls.dbname = 'stackoveflowlite'
        cls.dbuser = 'Linda'
        cls.dbpassword = 'yes'

        """ postgres credentials """
        cls.db_postgres_host = '127.0.0.1'
        cls.db_postgres_dbname = 'postgres'
        cls.db_postgres_user = 'postgres'
        cls.db_postgres_password = 'root'

        cls.tables = (
            """
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(500) NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS tbl_questions(
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                date_posted D
                content text NOT NULL,
                FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS tbl_answers(
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                content text NOT NULL,
                    FOREIGN KEY (user_id)
                    REFERENCES users (id)
                    ON UPDATE CASCADE ON DELETE CASCADE            
            )
            """
        )


        

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
                conn.close()
                


