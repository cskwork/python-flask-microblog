import os
from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#init packages
app = Flask(__name__)
app.config.from_object(Config)
#
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
#Req User to login (give Flask-login view function for logins) 
login.login_view = 'login'

#init app to load template resources
if __name__ == '__main__':
	app.run(debug=True)

#init URL(routes) for the app
from app import routes, models

  

"""
set FLASK_ENV=development
creates the application object as an instance of class Flask imported from the flask package
__name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used. 
"""