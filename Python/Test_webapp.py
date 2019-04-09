# Download flask from the website http://flask.pocoo.org/
# Copy paste the code from there


from flask import Flask, render_template, redirect, url_for, reuest
from student import Student
students
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
if __name__ == "__main__":
	app.run()
	
	