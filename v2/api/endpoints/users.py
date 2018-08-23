"""
Users endpoint
"""
from flask import jsonify
from flask_bcrypt import Bcrypt
from api.api.database.models import ()
import re


class signUp(Resource):
    def signUp(user_name, email, password):
        # encrypt password
        hidden_password = Bcrypt().generate_password_hash(password).decode()
        query = (INSERT * INTO tbl_users('user_name', 'email', 'hidden_password'))

        return run_query(query, inputs=[user_name, email, password])




class login(Resource):
    def validate_email(email):
        """Method confirms email is correct"""
        check_email = re.compile(r'^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if check_email.match(email) else False

    def validate_password(password):
        """Method confirms that password is correct"""
        return Bcrypt().check_password_hash(self.password, password)

   def user_login(email, password):

       if validate_email(email) ==True & validate_password(password):
           query = "SELECT * FROM tbl_users WHERE email = %s;"
           all_members = get_query(query, email)

           for user_email in all_members:
               if user_email['email'] == email:
                   return user_email


