from flask import Flask, render_template  # Import Flask and render_template for web app and HTML rendering
import os  # Import os for environment variable access
import random  # Import random for generating random numbers
from datetime import datetime  # Import datetime for current date and time
import requests  # Import requests for making HTTP requests

today = datetime.now()  # Get the current date and time

app = Flask(__name__)  # Create a Flask web application instance

@app.route('/')
def home():
    random_number = random.randint(1, 10)  # Generate a random number between 1 and 10
    year = today.year  # Get the current year
    return render_template('index.html', num=random_number, this_year=year)  # Render index.html with variables

@app.route('/guess/<name>')
def guess(name):
    # Get age prediction from agify API
    age_reponse = requests.get(url=f"https://api.agify.io/?name={name}").json()
    # Get gender prediction from genderize API
    gender_response = requests.get(url=f'https://api.genderize.io?name={name}').json()
    # Render guess.html with username, predicted age, and gender
    return render_template('guess.html', username=name, userage=age_reponse['age'], user_gender=gender_response['gender'])

@app.route('/blog')
def blog():
    # Get blog posts from external API
    blog_post_reponse = requests.get(url=' https://api.npoint.io/ad711b60ee445eeead7e').json()
    # Render blog.html with blog posts
    return render_template('blog.html', blog_post=blog_post_reponse)



if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 