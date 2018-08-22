import os
import re
import jwt
import datetime

from app import db
from flask import jsonify
from flask_bcrypt import Bcrypt


class User(db.Model):
    """This class represents the user table."""

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    questions = db.relationship(
        'question',
        backref='users',
        lazy='dynamic'
        )

    def __init__(self, email):
        """initialization"""
        self.email = email
        self.password = ''

    @staticmethod
    def validate_email(email):
        """Method validates an email"""
        address_matcher = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if address_matcher.match(email) else False

    def create_password(self, password):
        """Method generates a hashed password"""
        self.password = Bcrypt().generate_password_hash(password).decode()

    def validate_password(self, password):
        """Method confirms that password is correct"""
        return Bcrypt().check_password_hash(self.password, password)

    def gen_token(self):
        """Generates a token"""
        token = jwt.encode({
            'id': self.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=30)
        }, os.getenv('SECRET'))
        return jsonify({'token': token.decode('UTF-8')})

    def save(self):
        """Adds a new user to the database """
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all(user_id):
        """Gets all users in a single query """
        return User.query.all()

    def delete(self):
        """Deletes an existing user from the database """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """Represents the object instance of the model whenever it queries"""
        return "<User email: {}>".format(self.email)
