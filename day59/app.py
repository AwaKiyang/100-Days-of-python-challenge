from flask import Flask, render_template  # Import Flask class and render_template function for rendering HTML templates

import os  # Import os module to access environment variables

app = Flask(__name__)  # Initialize a Flask application instance with the current module name

text = ['alicia', ' patrick', 'pablo']  # Create a list of names to pass to templates

@app.route('/')  # Define a route for the root URL (homepage)
def homepage():  # Function to handle requests to the homepage
    # Render index.html template and pass the names list as a variable to the template
    return render_template("index.html", names=text)

@app.route('/greet/<name>')  # Define a route that accepts a dynamic name parameter in the URL
def greet(name):  # Function to handle personalized greeting requests with the provided name
    # Render hello.html template and pass the name parameter as username variable to the template
    return render_template('hello.html', username=name)

if __name__ == '__main__':  # Check if the script is run directly (not imported)
    # Retrieve PORT from environment variables, use 5000 as default if not set
    port = int(os.environ.get("PORT", 5000))
    # Start the Flask development server in debug mode on all network interfaces (0.0.0.0) at the specified port
    app.run(debug=True, host='0.0.0.0', port=port)