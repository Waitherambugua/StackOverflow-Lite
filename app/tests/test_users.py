import unittest
import os
import json


from app.manage import migrate, reset_migration
from app.app import create_app


class StackOverflow_lite_Users(unittest.TestCase):
    """This class represent Users."""

    def setUp(self):
        """Define test variables and initialize."""
        self.app = create_app("testing")
        migrate()

        self.checker = self.app.test_client()
        self.users = {'name': 'Linda Mbugua', 'email': 'waitherambugua@gmail.com', 'password': '1234'}
        self.default_user = {'name': 'Chris Mbugua', 'email': 'cnm@gmail.com', 'password': '1234'}
        self.checker.post('/api/v2/auth/signup', data=json.dumps(self.default_user))
      
    
    def test_signup_user(self):
        """Test to register new user."""
        data = self.users
        response = self.checker.post('/api/v2/auth/signup', data=json.dumps(data))

        result = json.loads(response.data.decode())

        self.assertEquals(result['message'],'New user registered')
        

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
        reset_migration()
        

if __name__ == "__main__":
    unittest.main()

    