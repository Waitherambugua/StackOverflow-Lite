# StackOverflow-lite      
StackOverflow-lite is a platform where people can ask questions and provide answers.

# Usage
- Home page
- Create an account 
- Login into your account
- Post a question
- Fetch all questions
- Fetch a single question
- Edit a specific question
- Delete a specific question
- Post an answer to a question

# Prerequisities
- Python 3.6 or a later version

# Installation
Downlaod / clone the project to your local computer by:
- Download the zip file of this repository.
- Unzip it and navigate into the UI directory.
<pre><code>
$ /StackOverflow-lite
</code></pre>
  

# Alternatively
Run the following command:
<pre><code> $ git clone https://github.com/waitherambugua/StackOverflow-lite.git </code></pre>
Locate StackOverflow-lite folder in your local computer.
<pre><code>$ cd StackOverflow-lite/ </code></pre>

# Virtual environment
Create a virtual environment
<pre><code> $ virtualenv venv </code></pre>
Activate the environment
<pre><code> $. venv/bin/activate </code></pre>

# Dependencies
Install package requirements to your environment
<pre><code> $ pip install -r requirements.txt </code></pre>

# Env
Create a.env file in your StackOverflow-lite root directory and add:
<pre><code>
$ . venv/bin/activate
$ source .env
</code></pre>

# Database integration
Create a Database on PostgreSQL:
- stackoverflow_lite (development DB)
- test_stackoverflow (testing DB)

# Testing
To set up testing environment
<pre><code>
$ pip install nose
$ pip install coverage
</code></pre>
To run test perform the following:
<pre><code>
$ nosetests --with-coverage
</code></pre>
# Testing API endpoints
<pre>
<table>
<tr><th>Test</th>
<th>API-endpoint</th>
<th>HTTP-Verbs</th>
</tr>
<tr>
<td>SignUp a user</td>
<td>/api/v2/auth/signup</td>
<td>POST</td>
</tr>
<tr>
<td>SignIn a user</td>
<td>/api/v2/auth/signin</td>
<td>POST</td>
</tr>
<tr>
<td>Post a question</td>
<td>/api/v2/questions</td>
<td>POST</td>
</tr>
<tr>
<td>Fetch all question</td>
<td>/api/v2/questions</td>
<td>GET</td>
</tr>
<tr>
<td>Fetch a single question</td>
<td>/api/v2/questions/question_id</td>
<td>GET</td>
</tr>
<tr>
<td>Edit a specific question</td>
<td>/api/v2/questions/question_id</td>
<td>PUT</td>
</tr>
<tr>
<td>Delete a question</td>
<td>/api/v2/questions/questions_id</td>
<td>DELETE</td>
</tr>
<tr>
<td>Post answer to a question</td>
<td>/api/v2/questions/question_id/answers</td>
<td>POST</td>
</tr>
<tr>
<td>User sign out</td>
<td>/api/v2/auth/signout</td>
<td>POST</td>
</tr>
</tr>
</table>
</pre>

#
- Hosted the API on [Heroku](https://stackoverflow-lite-v2.herokuapp.com)

# Authors
- Linda Mbugua - [waitherambugua](https://github.com/waitherambugua)