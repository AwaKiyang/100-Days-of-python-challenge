from flask import Flask, render_template, request, url_for, redirect  # Import Flask modules for routing and form handling
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database ORM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column   # Import ORM utilities for model definition
from sqlalchemy import Integer, String, Boolean # Import SQLAlchemy column types
from flask_ckeditor import CKEditor
import os   # Import os module for environment variables
import smtplib  # For sending emails via SMTP
from post_from import Post_form
from datetime import date

app = Flask(__name__)  # Initialize the Flask application
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

ckeditor = CKEditor()
ckeditor.init_app(app)
# CREATE DB - Define base class for all database models
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'    # Configure SQLite database URI
db = SQLAlchemy(model_class=Base) # Initialize SQLAlchemy with custom base class
db.init_app(app) # Bind SQLAlchemy instance to Flask app

# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(String, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')  # Define the route for the home page
def home():

    blog_post_data_in_db = db.session.execute(db.select(BlogPost)).scalars().all()
    # Render the index.html template and pass the blog posts to it
    return render_template("index.html", blog_post=blog_post_data_in_db)

@app.route('/blog/<id>')  # Dynamic route to display individual blog posts  #READ
def get_blog(id):
    post_id = int(id)
    # List of background images for blog posts
    queried_blog_post = db.get_or_404(BlogPost, post_id)
    # Render the post.html template with the selected blog post and background image
    return render_template('post.html', blog=queried_blog_post, background_image=queried_blog_post)

@app.route('/add_post', methods=['GET', 'POST']) #CREATE
def add_post():

    post_form = Post_form()

    if post_form.validate_on_submit():
        try:
            post = BlogPost(
                title = post_form.title.data,
                subtitle = post_form.submit.data,
                author = post_form.author.data,
                img_url = post_form.img_url.data,
                body = post_form.content.data,
                date = date.today().strftime("%B %d, %Y")
            )
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            pass
        return redirect(url_for('add_post'))


    return render_template('add_post.html', form=post_form)

@app.route('/edit/<id>', methods=['GET','POST'])   #UPDATE
def edit_post(id):
    post_id = int(id)
    post_to_update = db.get_or_404(BlogPost, post_id)

    edit_form = Post_form(
        title = post_to_update.title,
        subtitle = post_to_update.subtitle,
        img_url = post_to_update.img_url,
        author = post_to_update.author,
        content =post_to_update.body
    )
    if edit_form.validate_on_submit():
        post_to_update.title = edit_form.title.data
        post_to_update.subtitle = edit_form.subtitle.data
        post_to_update.img_url = edit_form.img_url.data
        post_to_update.author = edit_form.author.data
        post_to_update.body = edit_form.content.data
        db.session.commit()
        return redirect(url_for('get_blog',id = post_to_update.id) )

    return render_template('edit_post.html', form=edit_form, post = post_to_update )

@app.route('/delete/<id>')
def delete(id):
    post_id = int(id)
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


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