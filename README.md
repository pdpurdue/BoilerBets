# BoilerBets
This repo has been updated to work with Python v3.7.6 and up.
## Steps to run
1. Install virtualenv to create your virtual environment

`pip3 install virtualenv`

2. Construct your virtual environment

`virtualenv env`

3. Activate the virtual environment

`source env/bin/activate`

4. Install the dependencies

`pip install -r requirements.txt`

5. Locally run the Flask application

`python3 app.py`

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:
