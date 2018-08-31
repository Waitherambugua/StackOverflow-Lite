import unittest
import os
import json
from app.databas.db import Database

from app import create_app

class TestStackverflowlite(unittest.TestCase):
    """This class represent Questions and answers."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_filename="testing")
        self.db = Database()
        self.db.init_app(self.app)
        self.client = self.app.test_client()
        self.questions = {'question': 'How do you create a list in python'}
        self.questions_1 = {'question': 'How do you create a dictionary in python'}
        self.answers = {'Answer': 'I do not know', 'Date posted': '14th August 2018', 'status': 'pending'}
        self.user = {'name': 'Linda Mbugua', 'email': 'waitheralmbugua@gmail.com', 'password': '1234'}


        # create an authenticated user
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user))

        # the user can login
        response = self.client.post("/api/v2/auth/signin", data=json.dumps(self.user))


    def test_postQuestion(self):
        """Test posting a question."""
        response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.questions))

        self.assertEqual(response.status_code, 201)

    def test_get_allQuestions(self):
        """Test user view all questions."""
        response = self.client.get(
            '/api/v2/questions', data=json.dumps(self.questions))

        self.assertEqual(response.status_code, 200)

    def test_view_single_question(self):
        """Test user view a single question."""
        response = self.client.get(
            '/api/v2/questions/1', data=json.dumps(self.questions))

        self.assertEqual(response.status_code, 200)

    def test_edit_question(self):
        """Test user can edit a question."""
        response = self.client.post(
            '/api/v2/questions', data=json.dumps(self.questions))
        self.assertEqual(response.status_code, 201)

        response = self.client.put(
            '/api/v2/questions/1', data=json.dumps(self.questions_1))

        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/api/v2/questions/1', data=json.dumps(self.questions))

        self.assertEqual(response.status_code, 200)

    def test_delete_question(self):
        """Test user can delete a question."""
        response = self.client.get(
            '/api/v2/questions/1', data=json.dumps(self.questions))

        self.assertEqual(response.status_code, 200)

        response = self.client.delete(
            '/api/v2/questions/1', data=json.dumps(self.questions))

        self.assertEqual(response.status_code, 200)


    def tearDown(self):
        self.db.drop_tables()

if __name__ == "__main__":
    unittest.main()
