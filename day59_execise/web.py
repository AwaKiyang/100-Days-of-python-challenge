from flask import Flask, render_template, request  # Import Flask modules for routing and form handling
import requests  # For making HTTP requests to external APIs
import os  # For accessing environment variables
import smtplib  # For sending emails via SMTP

app = Flask(__name__)  # Initialize the Flask application

# Fetch blog posts from the API endpoint and parse the JSON response
blog_post_response = requests.get(url='https://api.npoint.io/ad711b60ee445eeead7e').json()


@app.route('/')  # Define the route for the home page
def home():
    # Render the index.html template and pass the blog posts to it
    return render_template("index.html", blog_post=blog_post_response)

@app.route('/blog/<id>')  # Dynamic route to display individual blog posts
def get_blog(id):
    # List of background images for blog posts
    background = ['https://images.unsplash.com/photo-1539571711714-62cd2534f96e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Y2FjdHVzfGVufDB8fDB8fHww',
                  'https://images.unsplash.com/photo-1520350094754-f0fdcac35c1c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGJvcmVkfGVufDB8fDB8fHww',
                  'https://images.unsplash.com/photo-1543525238-54e3d131f7ca?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGZhc3Rpbmd8ZW58MHx8MHx8fDA%3D']
    
    # Render the post.html template with the selected blog post and background image
    return render_template('post.html', blog=blog_post_response[int(id)], background_image=background[int(id)])

@app.route('/about')  # Route for the about page
def about():
    header_title = 'ABOUTS'
    return render_template('about.html', title=header_title)

@app.route('/contact')  # Route for the contact page
def contact():
    header_title = 'CONTACT'
    return render_template('contact.html', title=header_title)

@app.route("/message", methods=["POST"])  # Route to handle form submissions
def send_info():
    # Extract form data from the contact form
    name = request.form.get("name")
    email = request.form.get("email")
    telephone = request.form.get("telephone")
    subject1 = request.form.get("subject")
    message = request.form.get("message")

    my_email = "awakiyang9@gmail.com"  # Sender email address
    password = os.getenv("email_password")  # Get email password from environment variable
    
    try:
        # Establish SMTP connection to Gmail
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()  # Identify the client to the SMTP server
            smtp.starttls()  # Start TLS encryption
            smtp.ehlo()  # Re-identify after starting TLS

            smtp.login(user=my_email, password=password)  # Authenticate with Gmail

            # Compose the email subject and body
            subject = subject1
            body = f'Hi My name is {name}, \nmy number is {telephone}, \nmy email is {email}, \nHere is my message {message}'

            # Format the complete message with subject and body
            message = f'Subject: {subject}\n\n {body}'
            
            # Send the email
            smtp.sendmail(from_addr=my_email, to_addrs=email, msg=message)  
            
        # Return success response
        return render_template("contact.html", msg_sent=True)
    except Exception:  # Catch any errors during email sending
        # Return failure response
        return render_template("contact.html", msg_sent=False)


if __name__ == '__main__':
    # Get the port number from environment variable or use 5000 as default
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app in debug mode, accessible from any host
    app.run(debug=True, host='0.0.0.0', port=port)