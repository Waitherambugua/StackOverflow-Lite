from api import app
from api.database.helpers import run_query, get_query, get_just_query, run_just_query

def view_questions():
    """Get all questions"""
    # query and the user inputs
    query = ("SELECT * FROM tbl_questions;")
    # run query
    return run_just_query(query)
def view_question(id):
    """Get one question"""
    query = ("SELECT * FROM tbl_questions;")
    # run query
    return run_query(query, id)



