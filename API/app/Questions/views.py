
import json
from datetime import datetime
from flask import request, jsonify, abort
from . import Questions

@app.route('/questions/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def question(id, **kwargs):
     # GET request: Retrieve a buckelist using it's ID
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