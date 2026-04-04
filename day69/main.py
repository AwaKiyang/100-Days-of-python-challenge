from datetime import date  # Import date class for handling dates
from flask import Flask, abort, render_template, redirect, url_for, flash  # Import Flask components for web app
from flask_bootstrap import Bootstrap5  # Import Bootstrap for styling
from flask_ckeditor import CKEditor  # Import CKEditor for rich text editing
from flask_gravatar import Gravatar  # Commented out: Import for Gravatar (user avatars)
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required  # Import Flask-Login for user authentication
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database ORM
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column  # Import SQLAlchemy ORM components
from sqlalchemy import Integer, String, Text, ForeignKey  # Import SQLAlchemy data types
from functools import wraps  # Import wraps for decorators
from werkzeug.security import generate_password_hash, check_password_hash  # Import for password hashing
import os  # Import os for environment variables
# Import your forms from the forms.py
from forms import CreatePostForm, Createregisterform, CreateLoginForm, CreatecommentForm  # Import custom forms
# Add additional imports

app = Flask(__name__)  # Create Flask application instance
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Set secret key for session security
ckeditor = CKEditor(app)  # Initialize CKEditor for the app
Bootstrap5(app)  # Initialize Bootstrap for the app

# TODO: Configure Flask-Login
# Initialize Flask-Login manager
login_manager = LoginManager()  # Create LoginManager instance
login_manager.init_app(app)  # Bind login manager to Flask app

# Define callback to load user from database by user_id
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(Users, user_id)  # Load user by ID from database

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CREATE DATABASE
class Base(DeclarativeBase):  # Define base class for SQLAlchemy models
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'  # Configure SQLite database URI
db = SQLAlchemy(model_class=Base)  # Create SQLAlchemy instance with custom base
db.init_app(app)  # Bind database to Flask app


# CONFIGURE TABLES
class BlogPost(db.Model):  # Define BlogPost model
    __tablename__ = "blog_posts"  # Set table name
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key ID
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Unique title
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)  # Subtitle
    date: Mapped[str] = mapped_column(String(250), nullable=False)  # Date string
    body: Mapped[str] = mapped_column(Text, nullable=False)  # Post body text
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # Image URL
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to Users
    comments = db.relationship("Comments", backref="parent_post", lazy=True)


# TODO: Create a User table for all your registered users. 
class Users(UserMixin, db.Model):
    __tablename__ = "users"  # Define Users model inheriting from UserMixin
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key ID
    email: Mapped[str]= mapped_column(String(100), unique=True, nullable=False)  # Unique email
    password: Mapped[str] = mapped_column(String(1000), nullable=False)  # Hashed password
    name: Mapped[str] = mapped_column(String(250), nullable=False)  # User name
    posts = db.relationship("BlogPost", backref="author", lazy=True)  # Relationship to BlogPost
    comments = db.relationship("Comments", backref="comment_author", lazy=True )

#
class Comments(db.Model):
    __tablename__ = 'comments' 
    id : Mapped[int]= mapped_column(Integer, primary_key=True)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('blog_posts.id'), nullable=False)
#



with app.app_context():  # Create database tables within app context
    db.create_all() 
    

#Create admin-only decorator
def admin_only(f):  # Decorator to restrict access to admin (user ID 1)
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:  # Check if user is authenticated and is admin
            return abort(403)  # Return forbidden error
        #Otherwise continue with the route function
        return f(*args, **kwargs)  # Execute original function        
    return decorated_function


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['GET', 'POST'])  # Route for user registration
def register():
    registerform = Createregisterform()  # Instantiate registration form

    if registerform.validate_on_submit():  # If form is submitted and valid
        user = db.session.execute(db.select(Users).where(Users.email == registerform.email.data)).scalar()  # Check if email exists
        try:
            if user is None:  # If user doesn't exist
                new_user = Users(  # Create new user
                    email = registerform.email.data,
                    name = registerform.name.data,
                    password = generate_password_hash(password=registerform.password.data, method='scrypt', salt_length=8)  # Hash password
                )
                db.session.add(new_user)  # Add to session
                db.session.commit()  # Commit to database
                login_user(new_user)  # Log in the new user
                return redirect(url_for('get_all_posts'))  # Redirect to home
            else:
                flash(message='User email already exist login instead')  # Flash message for existing email
                return redirect(url_for('login'))  # Redirect to login
        except Exception as e:  # Catch any exceptions
            pass

    return render_template("register.html", form=registerform, islogged_in = current_user.is_authenticated)  # Render registration template


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=['GET','POST'])  # Route for user login
def login():
    login_form = CreateLoginForm()  # Instantiate login form

    if login_form.validate_on_submit():  # If form is submitted and valid
        user = db.session.execute(db.select(Users).where(Users.email == login_form.email.data)).scalar()  # Find user by email

        if user is not None:  # If user exists
            try:
                if check_password_hash(pwhash=user.password, password=login_form.password.data):  # Check password
                    login_user(user)  # Log in user
                    return redirect(url_for('get_all_posts'))  # Redirect to home
                else:
                    # Flash message if password is incorrect
                    flash(message='Password incorrect')  # Flash incorrect password message   
                    return redirect(url_for('login'))  # Redirect to login
            except Exception as e:  # Catch exceptions
                pass
        else:
            # Flash message if email doesn't exist
            flash(message='The email does\'nt exist please try again')  # Flash non-existent email message
            return redirect(url_for('login'))  # Redirect to login

    return render_template("login.html", form=login_form, islogged_in = current_user.is_authenticated)  # Render login template


@app.route('/logout')  # Route for logout
def logout():
    logout_user()  # Log out current user
    return redirect(url_for('get_all_posts'))  # Redirect to home

@app.route('/')  # Route for home page
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))  # Query all blog posts
    posts = result.scalars().all()  # Get all posts
    return render_template("index.html", all_posts=posts, islogged_in = current_user.is_authenticated, user= current_user)  # Render index template


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['GET','POST'])  # Route to show individual post
def show_post(post_id):
    comment_form = CreatecommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)  # Get post by ID or 404
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comments(
                comment = comment_form.comment.data,
                comment_author = current_user,
                parent_post = requested_post
            )
            db.session.add(new_comment)
            db.session.commit()
        else:
            flash('login before giving comments')
            return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, islogged_in = current_user.is_authenticated, user = current_user, form=comment_form)  # Render post template


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])  # Route for creating new post (admin only)
@login_required  # Require login
def add_new_post():
    form = CreatePostForm()  # Instantiate post form
    if form.validate_on_submit():  # If form is valid
        new_post = BlogPost(  # Create new post
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,  # Set author to current user
            date=date.today().strftime("%B %d, %Y")  # Set current date
        )
        db.session.add(new_post)  # Add to session
        db.session.commit()  # Commit to database
        return redirect(url_for("get_all_posts"))  # Redirect to home
    return render_template("make-post.html", form=form, islogged_in = current_user.is_authenticated)  # Render make-post template


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])  # Route for editing post (admin only)
@admin_only  # Require admin
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)  # Get post by ID
    edit_form = CreatePostForm(  # Instantiate form with existing data
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        #author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():  # If form is valid
        post.title = edit_form.title.data  # Update title
        post.subtitle = edit_form.subtitle.data  # Update subtitle
        post.img_url = edit_form.img_url.data  # Update image URL
        #post.author = current_user
        post.body = edit_form.body.data  # Update body
        db.session.commit()  # Commit changes
        return redirect(url_for("show_post", post_id=post.id))  # Redirect to post
    return render_template("make-post.html", form=edit_form, is_edit=True, islogged_in = current_user.is_authenticated)  # Render edit template


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")  # Route for deleting post (admin only)
@admin_only  # Require admin
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)  # Get post by ID
    db.session.delete(post_to_delete)  # Delete post
    db.session.commit()  # Commit deletion
    return redirect(url_for('get_all_posts'))  # Redirect to home

@app.route('/delete_comment/<int:comment_id>')
def delete_comment(comment_id):
    comment = db.get_or_404(Comments, comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('get_all_post'))


@app.route("/about")  # Route for about page
def about():
 # Get current user
    return render_template("about.html", islogged_in = current_user.is_authenticated)  # Render about template


@app.route("/contact")  # Route for contact page
def contact():
    return render_template("contact.html", islogged_in = current_user.is_authenticated)  # Render contact template


# Main entry point
if __name__ == '__main__':  # If script is run directly
    # Get port number from environment variable or use 5000 as default
    port = int(os.environ.get("PORT", 5000))  # Get port from env or default
    # Run Flask app in debug mode on all interfaces with specified port
    app.run(debug=True, host='0.0.0.0', port=port)  # Run the app
