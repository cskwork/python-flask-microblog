from flask import render_template 
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Danny'}
    return render_template('index.html', title='Home', user=user)
    
"""
 @app.route decorator creates an association between the URL given as an argument and the function.

Replaced to invoke template instead of coding html directly to .py 2020.12.29 cskuk
def index():
    user = {'username': 'Danny'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, '''+user['username'] + '''!</h1>
        </body>
    </html>''' 

from flask import render_template - required

""" 
