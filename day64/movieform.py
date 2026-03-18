from flask_wtf import FlaskForm # Import Flask-WTF for CSRF protection on forms
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField, IntegerField, DecimalField # Import form field types
from wtforms.validators import DataRequired, Length, NumberRange, URL # Import validators for form field validation

"""####################____________FORM_CLASS_______________#############################"""
class Movieform(FlaskForm):
    """
    FORM FOR ADDING NEW MOVIES RECORDS
    """
    title = StringField(label='Movie title', validators=[DataRequired('input movie title')])
    year = IntegerField(label='release year', validators=[NumberRange(min=1000, max=9999, message='input proper year'), DataRequired('input release year')])
    description = StringField(label='description', validators=[DataRequired('input description')])
    rating = DecimalField(label='rating',places=2, validators=[DataRequired('input rating')])
    ranking = IntegerField(label='ranking', validators=[NumberRange(min=1,max=10, message='input rank from 1 to 10'), DataRequired('input ranking')])
    review = StringField(label='review', validators=[DataRequired('input review')])
    img = URLField(label='image url', validators=[URL() ,DataRequired('input image URL')])
    submit = SubmitField(label='submit')

