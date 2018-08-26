from unittest import TestCase
import Questions.views
import os
import json





class BaseTestCase(TestCase):

    def setUp(self):

        """Configure test enviroment."""
    
        os.environ['APP_SETTINGS'] = 'Testing'
        self.app = create_app("Testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()



class QuestionsTestCase(BaseTestCase):

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        res = self.client().post('/Questions/', data=self.questions)
        self.assertEqual(res.status_code, 201)


    def test_api_can_get_all_questions(self):
        """Test API can get a question (GET request)."""
        res = self.client().post('/Questions/', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/questions/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('', str(res.data))

    def test_api_can_get_questions_by_id(self):
        """Test API can get a single question by using it's id."""
        rv = self.client().post('/questions/', data=self.question)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/Questions/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('question', str(result.data))

    def test_questions_can_be_edited(self):
        """Test API can edit an existing question. (PUT request)"""
        rv = self.client().post(
            '/Questions/',
            data={'01': 'How do you create a list in python?'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/Questions/01',
            data={
                "01": "How do you create a list in python?"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/Questions/01')
        self.assertIn('How do you create a string in python? ', str(results.data))

    def test_question_deletion(self):
        """Test API can delete an existing question. (DELETE request)."""
        rv = self.client().post('/Questions/',
            data={'01': 'How do you create a list in python?'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/questions/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/Question/1')
        self.assertEqual(result.status_code, 404)

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()


