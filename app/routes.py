from flask import render_template 
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Danny'}
    posts = [
                {
                    'author' : {'username':'홍길동'},
                    'body' : '블로그 테스트'
                },
                {
                    'author' : {'username':'홍길동2'},
                    'body' : '블로그 테스트2'
                }
            ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    
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
