
from flask import Flask  # Import Flask class to create the web application
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy extension for Flask to manage databases
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # Import ORM tools for defining database models with type hints
from sqlalchemy import Integer, String, Float  # Import SQLAlchemy column types for defining table schemas
import os # Import os module to access environment variables

# Create a Flask application instance
app = Flask(__name__)

# Define a base class for all database models
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with the custom Base class
db = SQLAlchemy(model_class=Base)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"   # Set the database URI to use SQLite with a local database file
db.init_app(app)  # Bind the SQLAlchemy instance to the Flask app

# Define the books model/table for the database
class books(db.Model):
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Define id column as primary key with integer type
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)    # Define title column as string(max 250 chars), unique and required
    author: Mapped[str] = mapped_column(String(250), nullable= False)   # Define author column as string(max 250 chars), required
    rating: Mapped[float] = mapped_column(Float, nullable= False)   # Define rating column as float type, required

# Create an application context to execute database operations
with app.app_context():
    db.create_all()  # Create all database tables defined in the models

# Check if this script is run directly (not imported as a module)
if __name__ == '__main__':
    # Retrieve PORT from environment variables, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Start the Flask development server in debug mode on all hosts
    app.run(debug=True, host='0.0.0.0', port=port)
