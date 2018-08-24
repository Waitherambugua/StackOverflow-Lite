# StackOverflow-Lite


[![Build Status](https://travis-ci.org/Waitherambugua/StackOverflow-Lite.svg?branch=database_tests)](https://travis-ci.org/Waitherambugua/StackOverflow-Lite)

StackOverflow is a web aplication that allows usere to view and upload questions.

Project Overview
StackOverflowLite is a platform where people can ask questions and provide answers.

Required Features
A user can create an account and log in
A user can post questions
A user can delete the questions they post
A user can post answers
A user can view the answers to the questions
A user can accept answer out of all answers to his/her questions as the preferred answer.

**UI Templates**
Home Page
User Registration
User Login
User Profile Page
Post a question page
View a single questions and answers page
View questions and answers page
StackOverFlowLite Complete UI template on gh-pages
[a link](https://waitherambugua@github.io) link
Getting started
The following instructions will get a copy of StackOverFlowLite up and running on your machine for development and testing purposes

*Requirements*
StackOverFlowLite will require the following:

A computer running on any distribution of Unix or Mac or Windows OS
Installation
Clone the repository to your local machine
$ git clone https://github.com/waitherambugua/StackOverflow-Lite.git
Navigate to the directory
$ cd StackOverflowLite/UI
Open the file
$ pen index.html file with a browser of your choice
Create API endpoints
Getting started
The following instructions will get a copy of StackOverFlowLite up and running on your machine for development and testing purposes

**The API**
**Requirements**
StackOverFlowLite will require the following:

A computer running on any distribution of Windows OS or get some help from your administrator on how to install the application if on another OS
Python 3.5 or higher
Pip
Git
Virtualenv
Installation

To clone and run this application, you will need Git installed on your computer. From your command line:

# Clone this repository to your local machine
$ git clone https://github.com/waitherambugua/StackOverflow-Lite.git

# Navigate to the folder that contains the app
$ cd StackOverflow-Lite

# Create a virtual environment and activate it
$ virtualenv -p python3 venv

# Activate the virtual environment
$ source venv/bin/activate

# Install the requirements
$ pip install -r requirements.txt

# Launch the application
$ python3 run.py

### Run the tests
$ nosetests --with-coverage
API endpoints
Users Endpoints
Method |	Endpoint                                        |	Functionality
----------------------------------------------------------------------------------
POST	 | /StackOverFlowLite/api/v1/auth/register          |	Creates a user account

POST   |	/StackOverFlowLite/api/v1/auth/login            |	Logs in a user

POST   |	/StackOverFlowLite/api/v1/auth/logout           |	Logs out a user

PUT    |	/StackOverFlowLite/api/v1/auth/reset-password   |	Reset a password for a logged user

DELETE |	/StackOverFlowLite/api/v1/questions/question-ID	| Delete a request of a logged in user

Questions Endpoints

Method |	Endpoint                                              |	Functionality
----------------------------------------------------------------------------------
POST	 |/StackOverFlowLite/api/v2/questions                     |	Add a question

POST	 |/StackOverFlowLite/api/v2/questions/question-ID/answers |	Add an answer

GET	   |/StackOverFlowLite/api/v2/questions                     |	Lists all questions

GET    |	/StackOverFlowLite/api/v2/questions/questionID        |	List a question

PUT    |	/StackOverFlowLite/api/v2/questions/questionID        |	Edit a question 

DELETE |	/StackOverFlowLite/api/v2/questions/questionID        |	Delete a question

Answers Endpoints
Method|	Endpoint                                                      | Functionality
----------------------------------------------------------------------------------
POST	|/StackOverFlowLite/api/v2/questions/question-ID/answers        |	Add an answer

GET	  |/StackOverFlowLite/api/v2/questions/questionID/answers        	| Lists all answers

PUT	  |/StackOverFlowLite/api/v2/questions/questionID/answer/answerID | Edit an answer


StackOverFlowLite hosted on Heroku

stackoverflowlite on heroku

**Build with**
HTML, CSS, Javascript
Flask RESTful API

**How to Contribute**
Fork repository to your github account
Create a branch
Make changes
Create a pull request


Contributors Linda Mbugua

Gh-pages: https://waitherambugua.github.io
Heroku API link: https://mstackoverflowlite.herokuapp.com/
