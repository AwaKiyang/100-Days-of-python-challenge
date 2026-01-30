from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello, wolrd</h1>' \
    '<p>This is a paragraph.</p>' \
    '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjZzNDg3M2VlZnUyYzIxbWs1djZpaGk0MmYzZXhhdWp2cW00bjlydiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZNegC7wFpuQT7nurZ0/giphy.gif">'

number_to_guess = 5
@app.route('/game/<int:number>')
def game(number):
    if number > number_to_guess:
        return '<p style="color : purple" > number is high 😅😅</p>' \
        '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTZnaHRrZGg1Nzc2eXV0NjA4YzlvbHZmb3RkYmZzMHphOXEzaGtiMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/yXBqba0Zx8S4/giphy.gif">'
    elif number < number_to_guess:
        return '<p style="color : red"> number is low 😆😆</p>' \
        '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjUwczRwcHd6dGZvMDI4NjR3ODB2NW94NWZ4bWVlcmR4ODVpeDJ3YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3PAGCj08nkQvsooWUB/giphy.gif">'
    else:
        return '<p style="color : green"> perfect youre rogth on spot 😁😁</p>' \
        '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzVndnh2azU2a2Q2Y3EzNjM4Nmd5MDk1ODZxc2VjbjFkdDNmZzVybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WK7omsLop0431tZjXb/giphy.gif">'
    
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 