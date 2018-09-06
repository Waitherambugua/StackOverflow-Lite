import pytest
import json
import os
import user.model



def test_new_user():
    
    user = User('newuser@gmail.com', 'WelcometoAndela')
    assert new_user.email == 'newuser@gmail.com'
    assert new_user.hashed_password != 'WelcometoAndela'
    assert not new_user.authenticated
    assert new_user.role == 'user'


def post_json(client, url, json_dict):
	return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    return json.loads(response.data.decode('utf8'))

def test_dummy(client):
    response = client.get('/')
    assert b'Each month, over 50 million developers come to StackOverflow-Lite to learn, share their knowledge, and build their careers.' in response.data


