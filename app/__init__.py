from flask import Flask
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

  

"""
set FLASK_ENV=development
creates the application object as an instance of class Flask imported from the flask package
__name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used. 
"""