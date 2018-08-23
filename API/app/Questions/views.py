
import json
from datetime import datetime
from flask import request, jsonify, abort
from . import Questions


@questions.route('/api/v1/questions/', methods=['POST', 'GET'])
def get_questions():
    """This function handles request to the questions resource"""
    if request.method == 'GET':
        # return all questions in the db
        response = jsonify(data['questions'])
        response.status_code = 200
    else:
        # POST request: Returns a new question with its id
        question_id = int(data["questions"][-1]['id']) + 1
        req_data = json.loads(request.data.decode('utf-8').replace("'", '"'))
        question = req_data['question']
        posted_by = req_data['namr']
        date = '{:%B %d, %Y}'.format(datetime.now())
        new_question = {
            "id": question_id,
            "text": question_text,
            "posted_by": posted_by,
            "date": date,
            "answers": []
        }
        data['questions'].append(new_question)
        response = jsonify(new_question)
        response.status_code = 201

    return response


@app.route('api/v1/questions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def question(id, **kwargs):
     # GET request: Retrieve a question using it's ID
        question = Questions.query.filter_by(id=id).first()
        if not :
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            question.delete()
            return {
            "message": "Question {} deleted successfully".format(.id) 
         }, 200
         #PUT request: Delete a question
        elif request.method == 'PUT':
            name = str(request.data.get('name', ''))
            question.name = name
            question.save()
            response = jsonify({
                'id': question.id,
                'name': question.name,
                'date_created': question.date_created,
                'date_modified': question.date_modified
            })
            response.status_code = 200
            return response
        else:
            # GET request: Retrieve a question
            response = jsonify({
                'id': question.id,
                'name': question.name,
                'date_created': question.date_created,
                'date_modified': question.date_modified
            })
            response.status_code = 200
            return response

    return app