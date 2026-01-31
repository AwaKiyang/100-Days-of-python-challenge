from flask import Flask, render_template, url_for  # Import necessary Flask modules
import requests  # For making HTTP requests
import os  # For accessing environment variables

app = Flask(__name__)  # Initialize the Flask application

# Fetch blog posts from the given API endpoint and parse the JSON response
blog_post_response = requests.get(url='https://api.npoint.io/ad711b60ee445eeead7e').json()

@app.route('/')  # Define the route for the home page
def home():
    # Render the index.html template and pass the blog posts to it
    return render_template("index.html", blog_post=blog_post_response)

@app.route('/blog/<id>')  # Define the route for individual blog posts
def get_blog(id):
    # Render the post.html template and pass the selected post to it
    # Convert id to int to index the blog_post_response list
    return render_template('post.html', post=blog_post_response[int(id)])

if __name__ == '__main__':
    # Get the port number from environment variable or use 5000 as default
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app in debug mode, accessible from any host
    app.run(debug=True, host='0.0.0.0', port=port)