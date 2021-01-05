from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User  

class LoginForm(FlaskForm):
	username = StringField('아이디', validators=[DataRequired()])
	password = PasswordField('암호', validators=[DataRequired()])
	remember_me = BooleanField('기억하기')
	submit = SubmitField('로그인')

class RegistrationForm(FlaskForm):
	username = StringField('아이디', validators=[DataRequired()])
	email = StringField('이메일', validators=[DataRequired(), Email()])
	password = PasswordField ('비밀번호', validators=[DataRequired()])
	password2 = PasswordField('비밀번호 다시 입력', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('등록')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('다른 아이디를 사용해주세요.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('다른 이메일 주소를 사용해주세요.')
