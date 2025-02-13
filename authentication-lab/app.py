from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyBlzb0mTG5Ye7yBvdQQoN4Y22Ko6q7_xZw",
  "authDomain": "mooo-f276e.firebaseapp.com",
  "projectId": "mooo-f276e",
  "storageBucket": "mooo-f276e.appspot.com",
  "messagingSenderId": "158138030076",
  "appId": "1:158138030076:web:d49819aefe97ec38258479",
  "measurementId": "G-T2N25R3Q3G",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
	error = ""

	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session ["user"] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"
	return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session["user"] = auth.create_user_with_email_and_password(email, password)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"
	return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)