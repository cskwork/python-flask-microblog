from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm
#add for login
from flask_login import current_user, login_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    #Fake user not req. because current_user is used 
    #user = {'username': 'Danny'}
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
    return render_template('index.html', title='Home Page', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #Add for user login
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        #Add for user login
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('사용자ID 또는 암호가 맞지 않습니다')
            return redirect(url_for('login'))
        #Register User as logged in
        login_user(user, remember=form.remember.data)
        #Req for login_required
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        """
        #Remove fake login
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
        """
    return render_template('login.html', tittle='로그인', form=form)    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.setPassword(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('등록되었습니다!')
        return redirect(url_for('login'))
    return render_template('register.html', title='회원가입', form=form)












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
