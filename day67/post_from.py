from flask import Flask
from flask_wtf import FlaskForm # import Flask-WTF for CSRF protection on forms
from wtforms import StringField, URLField, SubmitField # import form feild types
from wtforms.validators import DataRequired, NumberRange, URL # Import validators for form field validation
from flask_ckeditor import CKEditorField
"""####################____________FORM_CLASS_______________#############################"""


class Post_form(FlaskForm):
    """
    Form for adding new post
    """
    title = StringField(label='Enter title', validators=[DataRequired(message='input title')])
    subtitle = StringField(label='Enter subtitle', validators=[DataRequired(message='input subtitle')])
    author = StringField(label='enter author name', validators=[DataRequired(message='Input author\'s name')])
    img_url = URLField(label='enter imagge url', validators=[DataRequired(message="input img url")])
    content = CKEditorField(label="Blog content",validators=[DataRequired(message="input content")])
    submit = SubmitField(label='submit')


