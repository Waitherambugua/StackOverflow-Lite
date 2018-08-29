import helpers

class User(object):
    """This class represents the users for the StackOverflow-lite."""

    def __init__(self, id=0, username="", email="", password=""):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def insertUser(self):
        helpers.insert_user(self)

    def addUser(self):
        helpers.get_user(self)



class Questions(object):
    """This class represents the questions posted on the StackOverflow-lite API."""

    def __init__(self, id=0, question="", date_posted="", user_id=""):
        self.id = id
        self.question = question
        self.date_posted = date_posted
        self.user_id = user_id

    def postQuestion(self):
        self.id = helpers.post_question(self)



class Answers(object):
    """This class represents the answers posted on StackOverflow-lite API."""

    def __init__(self, id=0, answer="", date_posted="", question_id=""):
        self.id = id
        self.answer = answer
        self.date_posted = date_posted
        self.question_id = question_id
        
    def postAnswer(self):
        helpers.answer_question(self)


