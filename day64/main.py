from flask import Flask, render_template, redirect, url_for, request, jsonify # Import Flask class to create the web application
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy extension for Flask to manage databases
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column # Import ORM tools for defining database models with type hints
from sqlalchemy import Integer, String, Float  # Import SQLAlchemy column types for defining table schemas
from sqlalchemy.exc import IntegrityError  #for flask error handling


import os # Import os module to access environment variables
from movieform import Movieform

import requests #import request to get info from our api endpoint


# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Define a base class for all database models
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with the custom Base class
db = SQLAlchemy(model_class=Base)

# CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-movies-collection.db"   # Set the database URI to use SQLite with a local database file
db.init_app(app)  # Bind the SQLAlchemy instance to the Flask app


"""####################___________DB_CLASS________________#############################"""
class Movies(db.Model):
    """
        CREATE TABLE
    """
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year : Mapped[int]  = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    ranking : Mapped[int] = mapped_column(Integer, nullable=False)
    review : Mapped[str] = mapped_column(String, nullable=False)
    img_url : Mapped[str] = mapped_column(String, nullable=False)

# Create an application context to execute database operations
with app.app_context():
    db.create_all()  # Create all database tables defined in the models





@app.route("/")  #READ
def home():
    movies = db.session.execute(db.select(Movies)).scalars().all()
    return render_template("index.html", movies_list = movies)

@app.route('/add_movie', methods=['GET', 'POST'])  #CREATE
def add_movie():
    
    movie_form = Movieform()
   
    if movie_form.validate_on_submit():
        try:
            movie_tb = Movies(
                title = movie_form.title.data,
                year = movie_form.year.data,
                description = movie_form.description.data,
                rating = movie_form.rating.data,
                ranking = movie_form.ranking.data,
                review = movie_form.review.data,
                img_url = movie_form.img.data
                )
            db.session.add(movie_tb)
            db.session.commit()
            return redirect(url_for('add_movie'))
        except IntegrityError:
            db.session.rollback()  # Rollback on duplicate title error
            return jsonify({"error": "Book with this title already exists"}), 400

    return render_template('add.html', form=movie_form)

@app.route('/delete/<del_id>')  #delete
def delete(del_id):
    mov_id = int(del_id)

    movie_to_delete = db.session.execute(db.select(Movies).where(Movies.id == mov_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<upt_id>', methods=['GET', 'POST'])
def update(upt_id):
    mov_id = int(upt_id)
    movie_to_update = db.get_or_404(Movies, mov_id)

    if request.method == "POST":
        try:
            new_rating = request.form['New_rating']
            new_review = request.form.get('review')
            movie_to_update.rating = f"{new_rating}"
            movie_to_update.review = f'{new_review}'
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()  # Rollback on any error
            return jsonify({"error": f"{e}"}), 400

    return render_template('edit.html', movie=movie_to_update)






# Check if this script is run directly (not imported as a module)
if __name__ == '__main__':
    # Retrieve PORT from environment variables, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Start the Flask development server in debug mode on all hosts
    app.run(debug=True, host='0.0.0.0', port=port)
