

class questions(db.Model):
    """This class represents the questionlist table."""

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    items = db.relationship(
        'Item',
        backref='questions',
        lazy='dynamic',
        cascade="all,delete",
        )

    def __init__(self, title, user_id):
        """initialization."""
        self.title = title
        self.user_id = user_id

    def new_item(self):
        """Adds a new question to the database """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all(user_id):
        """Gets all questions in a single query """
        return questionlist.query.all(user_id=user_id)

    def delete(self):
        """Deletes an existing question from the database """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Represents the object instance of the model whenever it queries"""
        return "<questions: {}>".format(self.title)


class Item(db.Model):
    """This class represents the questions table."""

   
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __init__(self, name, question_id):
        """initialization."""
        self.name = name
        self.question_id = question_id

    def save(self):
        """Adds a new question to the database """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all(question_id):
        """Gets all questions in a single query """
        return Item.query.all(question_id=question_id)

    def delete(self):
        """Deletes an existing questions from the database """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Represents the object instance of the model whenever it queries"""
        return "<Item: {}>".format(self.name)