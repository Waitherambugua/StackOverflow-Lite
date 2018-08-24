from flask import Flask, render_template, url_for, jsonify, request, abort, redirect


app = Flask(__name__)
app.config["SECRET_KEY"] = "17a0ff2d80017591818a5481f7e35e8b"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Login', methods=["GET","POST"])
def Login():
	
	error = None
	if request.method =="POST":
		if request.form['username'] != 'flaskuser' or request.form["password"] != 'flaskuser2018':
			error = "Invalid credentials. Please try again."
		else:
			return redirect(url_for("UserAccount"))
	return render_template('Login.html', error=error)

@app.route('/SignUp',methods=["GET","POST"])
def SignUp():

	form = SignUpForm()
	return render_template('SignUp.html', title="SignUp", form=form)

@app.route('/Forum',methods=["GET","POST"])
def Forum():
	return render_template('Forum.html')

@app.route('/UserAccount', methods=["GET","POST"])
def UserAccount():
	return render_template('UserAccount.html')

@app.route('/Questions', methods=["GET","POST"])
def Questions():
	return render_template('Questions.html')

@app.route('/ForumAnswers', methods=["GET","POST"])
def ForumAnswers():
	return render_template('ForumAnswers.html')




if __name__ =="__main__":
	app.run(debug=True)