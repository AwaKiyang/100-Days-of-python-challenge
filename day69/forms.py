from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class Createregisterform(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message='input name')])
    email = StringField(label='Email', validators=[Email(message='Enter valid email')])
    password = StringField(label='password', validators=[DataRequired('input password')])
    submit = SubmitField(label='Register')

# TODO: Create a LoginForm to login existing users
class CreateLoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired('enter email')])
    password = StringField(label='enter password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


# TODO: Create a CommentForm so users can leave comments below posts
class CreatecommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



