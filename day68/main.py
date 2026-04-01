
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory    # Import Flask components for web routing, templates, and request handling
from werkzeug.security import generate_password_hash, check_password_hash   # Import security functions for password hashing and verification
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy ORM for database operations
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column   # Import SQLAlchemy type hints and decorators
from sqlalchemy import Integer, String  # Import SQLAlchemy data types
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user  # Import Flask-Login components for user authentication
import os   # Import os module for environment variables

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here' # Set secret key for session management


# CREATE DATABASE
# Define base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Configure SQLAlchemy database URI pointing to SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'    
db = SQLAlchemy(model_class=Base)   # Initialize SQLAlchemy database instance with custom base class
db.init_app(app)    # Bind SQLAlchemy instance to Flask app

# Initialize Flask-Login manager
login_manager = LoginManager()  
login_manager.init_app(app) # Bind login manager to Flask app

# Define callback to load user from database by user_id
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
# Define User model class inheriting from UserMixin (for authentication) and db.Model
class User(UserMixin, db.Model):
    """
    Define User model class inheriting from UserMixin (for authentication) and db.Model
    """
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True) # Define id column as primary key
    email: Mapped[str] = mapped_column(String(100), unique=True) # Define email column as unique string
    password: Mapped[str] = mapped_column(String(100)) # Define password column as string
    name: Mapped[str] = mapped_column(String(1000)) # Define name column as string


# Create all database tables within application context
with app.app_context():
    db.create_all()


# Route for home page
@app.route('/')
def home():
    """
    HOME route
    """
    # Render home template with user authentication status
    return render_template("index.html", logged_in = current_user.is_authenticated)


# Route for user registration (GET and POST methods)
@app.route('/register', methods=['GET','POST'])
def register():
    """
    Route for user registration (GET and POST methods)
    """
    # Check if form was submitted
    if request.method == 'POST':
        try:
            # Query database for existing user with same email
            user = db.session.execute(db.select(User).where(User.email == request.form.get('email'))).scalar()

            # Check if user doesn't exist
            if user is None:
                # Create new user with form data
                user = User(
                    
                    email = request.form.get('email'), # Set email from form
                    password =  generate_password_hash(password=request.form.get('password'), salt_length=8, method='scrypt') , # Hash password with scrypt method
                    name = request.form.get('name') # Set name from form
                )
                
                db.session.add(user) # Add user to session
                db.session.commit() # Commit changes to database

                login_user(user) # Log in the new user
                return redirect(url_for('secrets')) # Redirect to secrets page
            else:
                # Flash message if email already exists
                flash(message='You\'ve already sign up with this email login instead')
                return redirect(url_for('login')) # Redirect to login page
        except Exception as e:
            # Silently catch any exceptions during registration
            pass

    # Render registration template with authentication status
    return render_template("register.html", logged_in = current_user.is_authenticated)


# Route for user login (GET and POST methods)
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    # Route for user login (GET and POST methods)
    """
    # Check if form was submitted
    if request.method == "POST":
        
        email = request.form.get('email') # Get email from form
        password = request.form.get('password') # Get password from form

        # Query database for user with matching email
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        # Check if user exists
        if user is not None:
            try:
                # Verify password hash matches input password
                if check_password_hash(pwhash= user.password, password=password):
                    # Log in the user
                    login_user(user) 
                    return redirect(url_for('secrets')) # Redirect to secrets page
                else:
                    # Flash message if password is incorrect
                    flash(message='Password incorrect')   
                    return redirect(url_for('login'))  # Redirect to login page
            except Exception as e:
                # Render login template with error flag if exception occurs
                return render_template('login.html', notexist = True)     
        else:
            # Flash message if email doesn't exist
            flash(message='The email does\'nt exist please try again')
            return redirect(url_for('login')) # Redirect to login page

    # Render login template with authentication status
    return render_template("login.html", logged_in = current_user.is_authenticated)


# Route for secrets page (requires authentication)
@app.route('/secrets')
@login_required # Decorator to require user login for this route
def secrets():
    """
    # Route for secrets page (requires authentication)
    """
    # Print current user's name to console
    print(current_user.name)
    # Render secrets template with current user and authentication status
    return render_template("secrets.html", name = current_user , logged_in = current_user.is_authenticated)


# Route for user logout
@app.route('/logout')
def logout():
    '''
    # Route for user logout
    '''
    logout_user() #  Log out the current user
    # Redirect to home page
    return redirect(url_for('home'))


# Route for file download (requires authentication)
@app.route('/download')
@login_required # Decorator to require user login for this route
def download():
    """
    # Route for file download (requires authentication)
    """
    # Send cheat_sheet.pdf file from static directory as attachment
    return send_from_directory("static", 'files/cheat_sheet.pdf', as_attachment=True)

    


# Main entry point
if __name__ == '__main__':
    # Get port number from environment variable or use 5000 as default
    port = int(os.environ.get("PORT", 5000))
    # Run Flask app in debug mode on all interfaces with specified port
    app.run(debug=True, host='0.0.0.0', port=port)