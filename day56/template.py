from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')    #this is how you render html file

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 