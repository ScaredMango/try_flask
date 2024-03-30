from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Optional, Email, EqualTo

from .models import Category

def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]

class NewsForm(FlaskForm):
    title = StringField("Название", validators=[
        DataRequired(message='Заголовок не может может быть пустым'),
        Length(max = 255, message='Заголовок не может может быть больше 255 символов')
                                                ])
    text = TextAreaField('Текст отзыва', validators=[DataRequired(message='Введите новость')])
    category = SelectField(choices=get_categories())
    submit = SubmitField('Добавить')

class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message='Некорректный email')])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField("Повторите пароль",
                              validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')

class CategoryForm(FlaskForm):
    title = StringField("Название категории", validators=[DataRequired()])
    submit = SubmitField('Добавить')