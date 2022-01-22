from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName =  db.Column(db.String(200), nullable=False)
    lName =  db.Column(db.String(200), nullable=False)
    pn =  db.Column(db.String(200), nullable=False)
    email =  db.Column(db.String(200), nullable=False)

    password =  db.Column(db.String(200), nullable=False)
    confirm = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.id

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup',methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        task_fName = request.form['fName']
        task_lName = request.form['lName']
        task_pn = request.form['pn']
        task_email = request.form['email']
        task_password = request.form['password']
        task_confirm = request.form['confirm']

        new_task = Todo(fName=task_fName, lName = task_lName, pn = task_pn, email = task_email, password = task_password, confirm = task_confirm)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/login')
        except:
            return 'There was an issue creating your account.'

    else:
        return render_template('signup.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nfl')
def nfl():
    return render_template('nfl.html')

if __name__ == '__main__':
    app.run(debug=True)