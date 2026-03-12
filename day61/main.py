
from flask import Flask, render_template, redirect, url_for  # Import Flask components for web application, template rendering, redirects, and URL generation
import os  # Import os module for environment variable access
from flask_wtf import FlaskForm  # Import FlaskForm for form handling
from wtforms import StringField, PasswordField, SubmitField  # Import form fields for email, password, and submit button
from wtforms.validators import DataRequired, Email, Length, InputRequired  # Import validators for form validation (DataRequired, Email, Length, InputRequired)

# Initialize Flask application
app = Flask(__name__)

# Set secret key for session management and CSRF protection
app.secret_key = "any-string-you-want-just-keep-it-secret"

# Define custom form class for login
class MyForm(FlaskForm):
    # Email field with validators for required input and valid email format
    email = StringField('Email', validators=[InputRequired(), Email(message='thats not a valid email')])
    # Password field with validators for required input and minimum 8 characters
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, message='password to short')])
    # Submit button for form submission
    submit = SubmitField(label='Log in')

# Route for home page
@app.route("/")
def home():
    # Render and return the home page template
    return render_template('index.html')

# Route for login page accepting GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = MyForm()      # Create instance of login form
    if login_form.validate_on_submit():    # Check if form is submitted and validates successfully
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":   # Verify credentials match admin account
            return render_template("success.html") # Return success page if credentials are correct
        else:
            return render_template("denied.html")  # Return denied page if credentials are incorrect
    return render_template('login.html', form = login_form)  # Render login page with form for initial GET request or validation failure


# Entry point for Flask application
if __name__ == '__main__':
    # Retrieve PORT from environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Run Flask app in debug mode, accessible from all network interfaces
    app.run(debug=True, host='0.0.0.0', port=port)
