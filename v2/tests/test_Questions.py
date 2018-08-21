"""
Tests for Questions
"""
import unittest
import os
import json
from app import db, create_app


class questionTestCase(unittest.TestCase):
    """This class represents the question test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user = {'email': 'test@test.com', 'password': 'testPass'}
        self.question = {'title': 'Visit America'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def registration(self):
        """Test for User registeration"""
        return self.client().post('/auth/register/', data=self.user)

    def login(self):
        """Logins a user"""
        self.registration()
        resp = self.client().post('/auth/login/', data=self.user)
        return {'Authorization': json.loads(resp.data.decode())['token']}

    def test_create_question(self):
        """Test API can create a question"""
        resp = self.client().post(
            '/question/', headers=self.login(), data=self.question)
        self.assertEqual(resp.status_code, 201)
        self.assertIn('How do you create a list in python?', str(resp.data))

    def test_confirm_forum_creation(self):
        """Test user cannot post the same questions """
        self.client().post(
            '/question', headers=self.login(), data=self.question)
        resp = self.client().post(
            '/question/', headers=self.login(), data=self.question)
        self.assertEqual(resp.status_code, 403)
        self.assertIn('That question has been posted!', str(resp.data))

    def test_blank_title(self):
        """Test that question is not blank"""
        self.question['title'] = ''
        resp = self.client().post(
            '/question/', headers=self.login(), data=self.question)
        self.assertEqual(resp.status_code, 401)
        self.assertIn('Please write your question', str(resp.data))

    def test_get_all_questions_when_blank(self):
        """Tests if a question exists"""
        resp = self.client().get('/question/', headers=self.login())
        self.assertEqual(resp.status_code, 404)
        self.assertIn('questions not found', str(resp.data))

    def test_api_can_get_question_by_id(self):
        """Test API can get a question using it's id"""
        resp = self.client().post(
            '/question/', headers=self.login(), data=self.question)
        self.assertEqual(resp.status_code, 201)
        id = json.loads(resp.data.decode())['id']
        result = self.client().get(
            '/question/{}'.format(id), headers=self.login())
        self.assertEqual(result.status_code, 200)
        self.assertIn('How do you create a list in python?', str(result.data))

    

    def test_delete_question(self):
        """Test API can delete a question"""
        self.client().post(
            '/question/', headers=self.login(), data=self.question)
        resp = self.client().delete(
            '/question/1/', headers=self.login(), data=self.question)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('question deleted', str(resp.data))
        result = self.client().get(
            '/question/1/', headers=self.login())
        self.assertEqual(result.status_code, 403)
        self.assertIn('question Not found', str(result.data))

    def test_question_search(self):
        """Test API can serach for a question"""
        self.question['question'] = 'How do you create a list in python?'
        self.client().post(
            '/question/', headers=self.login(), data=self.question)
        resp = self.client().get(
            '/question?q=forum', headers=self.login())
        self.assertIn('How do you create a list in python?', str(resp.data))
        resp = self.client().get('/question?q=forum', headers=self.login())
        self.assertEqual(len(json.loads(resp.data.decode())['question']), 1)

    def test_question_search_for_non_existent(self):
        """Test API can search for non existing data"""
        resp = self.client().get(
            '/question?q=question20', headers=self.login(), data=self.question)
        self.assertIn('questions not found', str(resp.data))

    def test_get_questions_with_limit(self):
        """Test API can search content limit"""
        self.client().post(
            '/question', headers=self.login(), data=self.question)
        self.question['question'] = 'question written'
        self.client().post(
            '/question', headers=self.login(), data=self.question)
        resp = self.client().get(
            '/question?limit=1', headers=self.login(), data=self.question)
        self.assertEqual(len(json.loads(resp.data.decode())['question']), 1)

    def test_input_is_alphanumerhic(self):
        """Test API can search content limit with aplhabets"""
        resp = self.client().get(
            '/question?limit=test', headers=self.login(), data=self.question)
        self.assertIn(
            'Error, pass a number', json.loads(resp.data.decode()).values())

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()