from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import os
from sqlalchemy.exc import IntegrityError  #for flask error handling

# Initialize Flask application
app = Flask(__name__)

# Create declarative base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with the custom Base class
db = SQLAlchemy(model_class=Base)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"  # Configure SQLite database path
db.init_app(app)   # Initialize the Flask app with SQLAlchemy extension

# Define Books model with columns: id, title, author, and rating
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Unique book title
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # Author name
    rating: Mapped[float] = mapped_column(Float, nullable=False)  # Book rating

# Create database tables within app context
with app.app_context():
    db.create_all()

# Route to display all books sorted by title
@app.route('/')  #READ
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))  # Query all books ordered by title
    all_books = result.scalars().all()  # Extract all book objects
    return render_template('index.html', library=all_books)  # Render template with books

# Route to add a new book (GET shows form, POST adds book to database)
@app.route("/add", methods=['GET', 'POST'])   #CREATE
def add():
    if request.method == "POST":
        try:
            # Create new Books object from form data
            book = Books(
                title=request.form.get('Book_name'),
                author=request.form.get('Book_Author'),
                rating=request.form.get('rating')
            )
            db.session.add(book)  # Add book to session
            db.session.commit()  # Commit to database
            return redirect(url_for("home"))  # Redirect to home page
        except IntegrityError:
            db.session.rollback()  # Rollback on duplicate title error
            return jsonify({"error": "Book with this title already exists"}), 400
    
    return render_template('add.html')  # Show add book form for GET request

# Route to delete a book by ID
@app.route('/delete/<del_id>')  #DELETE
def delete(del_id):
    book_id = int(del_id)  # Convert string ID to integer
    # Query book by ID
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    db.session.delete(book_to_delete)  # Delete book from session
    db.session.commit()  # Commit deletion to database
    return redirect(url_for('home'))  # Redirect to home page

# Route to update a book's rating by ID
@app.route('/update/<id>', methods=['GET', 'POST'])  #UPDATE
def update(id):
    book_id = int(id)  # Convert string ID to integer
    book_to_update = db.get_or_404(Books, book_id)  # Get book or return 404 error
    
    if request.method == "POST":
        try:
            new_rating = request.form["New_rating"]  # Get new rating from form
            book_to_update.rating = f"{new_rating}"  # Update book rating
            db.session.commit()  # Commit changes to database
            return redirect(url_for('home'))  # Redirect to home page
        except Exception as e:
            db.session.rollback()  # Rollback on any error
            return jsonify({"error": f"{e}"}), 400
    
    return render_template('update.html', book=book_to_update)  # Show update form for GET request

# Entry point for running the Flask application
if __name__ == '__main__':
    # Get PORT from environment variable, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Run Flask app in debug mode, accessible from all hosts on specified port
    app.run(debug=True, host='0.0.0.0', port=port)
