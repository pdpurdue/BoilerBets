from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///master.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName =  db.Column(db.String(200), nullable=False)
    lName =  db.Column(db.String(200), nullable=False)
    pn =  db.Column(db.String(200), nullable=False)
    email =  db.Column(db.String(200), nullable=False)

    password =  db.Column(db.String(200), nullable=False)
    confirm = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.id

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_pass = request.form['password']
        result = db.session.query(User).all()
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

        new_task = User(fName=task_fName, lName = task_lName, pn = task_pn, email = task_email, password = task_password, confirm = task_confirm)

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
    return render_template('index.html')

@app.route('/nfl')
def nfl():
    return render_template('nfl.html')

@app.route('/incorrect_login', methods = ['GET', 'POST'])
def incorrect_login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_pass = request.form['password']
        result = db.session.query(User).all()
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

if __name__ == '__main__':
    app.run(debug=True)