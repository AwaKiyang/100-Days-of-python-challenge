
from flask import Flask, render_template, url_for, redirect # Import Flask core functions for web app creation and templating
from flask_wtf import FlaskForm # Import Flask-WTF for CSRF protection on forms
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField # Import form field types
from wtforms.validators import DataRequired # Import validators for form field validation
from csv_data import csv_data # Import custom CSV data handling module
import os # Import OS module for environment variables



app = Flask(__name__)  # Initialize Flask application
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Set secret key for session encryption and CSRF protection


# Define form class for cafe information submission
class CafeForm(FlaskForm):
    """Form for adding new cafe information"""

    # Cafe name input field with required validation
    cafe = StringField(label='Cafe name', validators=[DataRequired('Input cafe name')])
    # Google Maps URL field with required validation
    location = URLField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired('Input URL')])
    # Opening time input field with required validation
    openingtime = TimeField(label='Opening Time e.g 8AM', validators=[DataRequired('Input time')])
    # Closing time input field with required validation
    closing_time = TimeField(label='Closing Time e.g 5:30PM', validators=[DataRequired('Input closing time')])
  
    coffee = SelectField(label='Coffee Rating', choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️'], default='☕️')   # Coffee rating dropdown with emoji options
    wifi = SelectField(label='Wifi Strength Rating', choices=['💪','💪💪','💪💪💪','💪💪💪💪'], default='✘')   # WiFi strength rating dropdown with emoji options
    socket = SelectField(label='Power Socket Availability', choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌'], default='✘')  # Power socket availability dropdown with emoji options
    submit = SubmitField(label='Submit')  # Submit button for form submission

# Route for home page
@app.route('/')
def home():
    """Home page route"""
    # Render and return the index template
    return render_template('index.html')

# Route to display all cafes
@app.route('/cafe')
def cafes():
    """Display all cafes from CSV data"""
    # Read cafe data from CSV file
    table_info = csv_data.data_reader()
    # Render cafes template with data
    return render_template('cafes.html', table_rows=table_info)

# Route to add new cafe (GET and POST requests)
@app.route('/add', methods=['GET', 'POST'])
def add_info():
    """Add new cafe information to CSV"""
    # Create form instance
    add_cafes = CafeForm()
    
    # Check if form is submitted and all validations pass
    if add_cafes.validate_on_submit():
        # Prepare row data from form inputs
        row = [add_cafes.cafe.data, 
               add_cafes.location.data, 
               add_cafes.openingtime.data, 
               add_cafes.closing_time.data,
               add_cafes.coffee.data,
               add_cafes.wifi.data,
               add_cafes.socket.data]
        # Write row data to CSV file
        csv_data.data_writer(row=row)
        # Redirect to add page to clear form
        return redirect(url_for("add_info"))

    # Render add template with form object
    return render_template('add.html', form=add_cafes)

# Entry point for running the Flask application
if __name__ == '__main__':
    # Get PORT from environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Run Flask app in debug mode, accessible from all hosts on specified port
    app.run(debug=True, host='0.0.0.0', port=port)
