from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master.db'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName =  db.Column(db.String(200), nullable=False)
    lName =  db.Column(db.String(200), nullable=False)
    pn =  db.Column(db.String(200), nullable=False)
    email =  db.Column(db.String(200), nullable=False)
    password =  db.Column(db.String(200), nullable=False)
    confirm = db.Column(db.String(200), nullable=False)
    boilerBucks = db.Column(db.Integer, primary_key = False)
    def __repr__(self):
        return self.id

class Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport =  db.Column(db.String(200), nullable=False)
    prediction =  db.Column(db.String(200), nullable=False)
    betAmount = db.Column(db.Integer, primary_key=False)
    payout =  db.Column(db.Integer, primary_key=False)
    email =  db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return self.id    


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sport =  db.Column(db.String(200), nullable=False)
    team1 =  db.Column(db.String(200), nullable=False)
    team2 = db.Column(db.String(200), nullable=False)
    isDone =  db.Column(db.String(200), nullable=False)
    winner =  db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return self.id

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_pass = request.form['password']
        result = db.session.query(Users).all()
        for x in result: 
            if (x.email == user_email):
                if (len(user_email) > 0 and len(user_pass) > 0):
                    if (x.password == user_pass):
                        return redirect('/index')
                    else:
                        return render_template('incorrect_login.html')
                else:
                    return redirect('/incorrect_login')
        return redirect('/incorrect_login')
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
        task_boilerBucks = random.randrange(300,3000)

        new_task = Users(fName=task_fName, lName = task_lName, pn = task_pn, email = task_email, password = task_password, confirm = task_confirm, boilerBucks = task_boilerBucks)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue creating your account.'

    else:
        return render_template('signup.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/index')
def index():
    ran = [1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1]
    tasks = Users.query.order_by(Users.boilerBucks.desc()).all()
    return render_template('index.html',tasks=tasks,ran=ran)

@app.route('/nfl')
def nfl():
    return render_template('nfl.html')

@app.route('/incorrect_login', methods = ['GET', 'POST'])
def incorrect_login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_pass = request.form['password']
        result = db.session.query(Users).all()
        for x in result: 
            if (x.email == user_email):
                if (len(user_email) > 0 and len(user_pass) > 0):
                    if (x.password == user_pass):
                        return redirect('/')
                    else:
                        return redirect('/incorrect_login')
                else:
                    return redirect('/incorrect_login')
    return render_template('incorrect_login.html')
@app.route('/nba')
def nba():
    return render_template('nba.html')

@app.route('/premier')
def premier():
    return render_template('premier.html')


if __name__ == '__main__':
    app.run(debug=True)