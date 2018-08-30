
from flask import request, jsonify, abort, make_response, json
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from werkzeug.security import generate_password_hash, check_password_hash
#from passlib.handlers.bcrypt import bcrypt
#import datetime
from datetime import datetime
from app.helpers import insert_user, get_user, login_user, post_question, get_questions, get_question, edit_question, delete_question
from app.models.models import User, Questions, Answers
from . import main_blueprint as main
from app.instance.config import app_config




@main.route('/api/v2/auth/signup', methods=['POST'])
def signup_user():
    if request.json and request.json['email']:

        user = get_user(request.json['email'])
        if user is not None:
            return jsonify({'message': "Email is linked to a registered user."})

        user = User(name = request.json.get("name"),
                    email = request.json.get("email"),
                    password = generate_password_hash(request.json.get("password")))

        if user == " ./?><{!@#$%^&*(":
            return jsonify({'message': 'Insert Your Credentials to Register'})
    
        user.insertUser()
        return jsonify({'message': 'User registered', 'User': user.__dict__})

        
    return abort(400)

@main.route('/api/v2/auth/login', methods=['POST'])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    user = get_user(email)
    if user is None:
        return jsonify({"message": "Email not found"}), 404
    elif not check_password_hash(user[3], password):

        return jsonify({'message': "Incorrect password"}), 400
    else:
        token = create_access_token(identity=request.json.get('email'), )
 
    return jsonify({'message': 'Logged in successfully', 'token': token})
    return make_response('This account does not exist'), 401


@main.route('/api/v2/questions', methods=['POST'])
@jwt_required
def question():

    email = get_jwt_identity()
    user = get_user(email)
    # post a single question
    question = Questions(
        question = request.json.get("question"),
        date_posted = datetime.now(),
        user_id = user[0])
    question.post_question()
    return jsonify({'Questions': question.__dict__}), 201

@main.route('/api/v2/questions', methods=['GET'])
@jwt_required
def view_all_questions():
    email = get_jwt_identity()
    user = get_user(email)
   #view all questions
    questions = get_questions(user[3])
    if questions is None:
    # retrieve all questions
        return jsonify({'message': 'No questions found'})
    return jsonify({'Questions': questions}), 200

@main.route('/api/v2/questions/<int:id>', methods=['GET'])
@jwt_required
def single_question(id):
    email = get_jwt_identity()
    user = get_user(email)

    # retrive a question by it's ID
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question not available'})

    return jsonify({'Questions': question}), 200

@main.route('/api/v2/questions/<int:id>', methods=['PUT'])
@jwt_required
def modify_question(id):
    email = get_jwt_identity()
    user = get_user(email)
    # Edit a specific question
    edit = get_question(id)
    if edit is None:
        return jsonify({'message': 'Question not available'})
    edit['question'] = request.json.get('question'),
    edit['date_posted'] = datetime.now()
    edit_question(id, edit)
    return jsonify({'Questions': edit}), 200

@main.route('/api/v2/questions/<int:id>', methods=['DELETE'])
@jwt_required
def remove_question(id):
    email = get_jwt_identity()
    user = get_user(email)
    # Delete a specific question
    question = get_question(id)
    if question is None:
        return jsonify({'message': 'Question not available'})
    delete_question(id)
    return jsonify({'message': 'Question has been deleted!'}), 200

@main.route('/api/v2/questions/<int:id>/answers', methods=['POST'])
@jwt_required
def answer_question(id):
    # retrive a answer by it's ID
    email = get_jwt_identity()
    question = get_question(id)
    # Answer a specific answer
    answers = Answers(
        answer = request.json.get("answer"),
        date_posted = datetime.now(),
        question_id = (question[0]))
    
    answers.postAnswer()
    return jsonify({'Answers': answers.__dict__}), 201




@main.route('/api/v2/auth/logout', methods=['POST'])
@jwt_required
def logout():
    # Log out a sign in user
    return jsonify({'message': 'Logged out successfully!'})
