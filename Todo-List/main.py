from flask import Flask, request,url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Todo(db.Model):
    title = db.Column(db.String(100),nullable =False,primary_key=True)
    
    def __init__(self,title):
    	self.title = title


@app.route("/")
def home():
	todo = Todo.query.all()
	return render_template("demo.html", todo=todo)

@app.route('/add',methods = ['POST'])
def add():
	title = request.form.get('title')
	entry = Todo(title=title)
	db.session.add(entry)
	db.session.commit()
	return redirect("/")


@app.route('/delete/<string:todo_title>')
def delete(todo_title):
	todo=Todo.query.get(todo_title)
	if not todo:
		return redirect("/")
	db.session.delete(todo)
	db.session.commit()
	return redirect("/")

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)