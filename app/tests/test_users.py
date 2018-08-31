import unittest
import os
import json
from app import create_app
#from app.manage import migrate, drop_tables
from app.databas.db import Database



class StackOverflow_lite_Users(unittest.TestCase):
    """This class represent Users."""

    def setUp(self):
        """Define test variables and initialize."""
        self.app = create_app(config_filename="testing")
        self.db = Database()
        self.db.init_app(self.app)
        self.checker = self.app.test_client()
        self.context = self.app.app_context()
        self.context.push()
        self.users = {'name': 'Chris Njuguna', 'email': 'yaz@gmail.com', 'password': 'yes'}
        self.default_user= {'name': 'Linda Mbugua', 'email': 'lwm@gmail.com', 'password': 'yes'}
        self.checker.post('/api/v2/auth/signup', data=json.dumps(self.users))


    def test_signup_user(self):
        """Test to register new user."""
        with self.checker:
            data = self.users
            response = self.checker.post(
                '/api/v2/auth/signup/',
                data=json.dumps(data)
            )
            print(response)

            result = json.loads(response.data.decode())
            print(result)

        self.assertEquals(result['message'],'User registered')


    def test_signin_user_with_invalid_email_password(self):
        """Test user trying to login with invalid email."""
        data = self.users
        response = self.checker.post('/api/v2/auth/signin', data=json.dumps(data))

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Email not found", "Incorrect password")


    def test_signin_user(self):

        data = self.default_user
        response = self.checker.post('/api/v2/auth/signin', data=json.dumps(data))

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Logged in successfully")


    def tearDown(self):
       self.db.drop_tables()

if __name__ ==  "__main__":
    unittest.main()
