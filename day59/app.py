from flask import Flask, render_template,url_for
import os

app = Flask(__name__) #initializing the flask app

text = ['alicia',' patrick', 'pablo']

@app.route('/')
def homepage():
    return render_template("index.html", names=text)

@app.route('/greet/<name>')
def greet(name):
    return render_template('hello.html', username= name)

if __name__ == '__main__':
    # Get the port number from environment variable or use 5000 as default
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app in debug mode, accessible from any host
    app.run(debug=True, host='0.0.0.0', port=port)