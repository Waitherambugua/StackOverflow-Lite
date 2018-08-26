"""
Users endpoint
"""
from .. import db, flask_bcrypt

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)



"""from flask import jsonify
from flask_bcrypt import Bcrypt
from api.database import models
import re


class signUp(Resource):
    def signUp(user_name, email, password):
        # encrypt password
        hashed_password = Bcrypt().generate_password_hash(password).decode()
        query = (u'INSERT * INTO tbl_users (user_name, email, user_password,'') VALUES(%s, %s, %s);')

        return run_query(query, inputs=(user_name, email, hashed_password))

class LogIn(Resource):
  #docstring for Class
  def __init__(self, arg):
    self.arg = arg
    # logIn(Resource):

  def validate_email(email):
    #Method confirms email is correct
    check_email = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
    return True if check_email.match(email) else False

  def validate_password(password):
    #Method confirms that password is correct
    return Bcrypt().check_password_hash(self.password, password)

  def LogIn(email, password):
    if validate_email(email) ==True & validate_password(password):
      query = "SELECT * FROM tbl_users WHERE email = %s;"
      all_members = get_query(query, email)

      for user_email in all_members:
        if user_email['email'] == email:
          return user_email


"""