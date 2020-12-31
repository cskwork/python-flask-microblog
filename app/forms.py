from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('아이디', validators=[DataRequired()])
	password = PasswordField('암호', validators=[DataRequired()])
	remember_me = BooleanField('기억하기')
	submit = SubmitField('로그인')