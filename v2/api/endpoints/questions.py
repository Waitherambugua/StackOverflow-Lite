from .database.models import Models
from flask import jsonify


class Questions(MethodView):
    """ 
    Questions
    """
   
    def get(self):
        """ 
        Fetch all questions
        """
        question = Questions.query.filter_by(id=id).first()
        response = {'questions': Models.view_questions()}
        return response, 200

    def post(self):
        """
                Post a question
        """
        question = Questions.query.filter_by(id=id).first()
        question_id = int(data["questions"][-1]['id']) + 1
        req_data = json.loads(request.data.decode('utf-8').replace("'", '"'))
        question = req_data['question']
        posted_by = req_data['name']
        date = '{:%B %d, %Y}'.format(datetime.now())
        new_question = {
            "id": question_id,
            "text": question_text,
            "posted_by": posted_by,
            "date": date

        }
        data['questions'].append(new_question)
        response = jsonify(new_question)
        response.status_code = 201

        return response




class Question(MethodView):
    """ Get single question """

    def get(self, id):
        """ 
        Fetch a specific question 
        """
        question = Questions.query.filter_by(id=id).first()
        response = jsonify({
            'id': question.id,
            'name': question.name,
            'date_created': question.date_created,
            'date_modified': question.date_modified
        })
        response.status_code = 200
        return response

        

    def delete(self, id):
        """
            Delete a question
        """

        question = Questions.query.filter_by(id=id).first()
        question.delete()
        response = {
            "message": "Question deleted successfully"
        }
        response.status_code = 200
        return response



class addAnswer(MethodView):
    """
    Add answer
    """

    def post(self, id):
        """add an answer"""
        answer = Answers.query.filter_by(id=id).first()
        answer_id = int(data["answers"][-1]['id']) + 1
        req_data = json.loads(request.data.decode('utf-8').replace("'", '"'))
        answer = req_data['answer']
        posted_by = req_data['name']
        date = '{:%B %d, %Y}'.format(datetime.now())
        new_answer = {
            "id": answer_id,
            "text": answer_text,
            "posted_by": posted_by,
            "date": date

        }
        data['answer'].append(new_answer)
        response = jsonify(new_answer)
        response.status_code = 201
        return response



class updateAnswer(MethodView):
    """
    Update answer
    """


    def put(self, id):
        """add an answer"""
        response = UserModel().decode_auth_token(auth_token)
        if int(user_id) == int(response):
            # edit answer
            new_text = json.loads(request.data.decode().replace("'", '"'))['text']
            text = answers.update_answer(new_text, answer_id)
        else:
            # it is not the same user who asked the answer
            raise Forbidden
        resp = {
            "message": "success",
            "description": "answer updated succesfully",
            "text": text
        }
        return jsonify(resp), 200
        pass

