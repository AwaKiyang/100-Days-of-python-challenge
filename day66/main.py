
from flask import Flask, jsonify, render_template, request  # Import Flask utilities for web framework functionality
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy for database ORM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column   # Import ORM utilities for model definition
from sqlalchemy import Integer, String, Boolean # Import SQLAlchemy column types
from random import choice   # Import choice function for random selection
import os   # Import os module for environment variables


# Create Flask application instance
app = Flask(__name__)

# CREATE DB - Define base class for all database models
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'    # Configure SQLite database URI
db = SQLAlchemy(model_class=Base) # Initialize SQLAlchemy with custom base class
db.init_app(app) # Bind SQLAlchemy instance to Flask app


# Define Cafe database model/table
class Cafe(db.Model):
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Primary key column (auto-increment integer)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False) # Cafe name (unique, required)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)  # Google Maps URL
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)   # Cafe image URL
    location: Mapped[str] = mapped_column(String(250), nullable=False)  # Cafe location/address
    seats: Mapped[str] = mapped_column(String(250), nullable=False) # Number of available seats
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False) # Whether cafe has toilets
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)   # Whether cafe has WiFi
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)    # Whether cafe has power sockets
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)    # Whether calls can be taken in cafe
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)  # Coffee price (optional)


# Create all database tables within app context
with app.app_context():
    db.create_all()


"""
******************* 
Route for home page
*******************
"""
@app.route("/")
def home():
    # Render index.html template
    return render_template("index.html")

"""
**************************
Route to get a random cafe
**************************
"""
@app.route('/random')
def rand():
    
    records = db.session.execute(db.select(Cafe)).scalars().all() # Fetch all cafe records from database
    random_cafe = choice(records) # Select a random cafe from records

    # Return JSON response with random cafe data (excluding id)
    return jsonify(cafe={
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        # Group amenity properties in sub-dictionary
        "amenities": {
          "seats": random_cafe.seats,
          "has_toilet": random_cafe.has_toilet,
          "has_wifi": random_cafe.has_wifi,
          "has_sockets": random_cafe.has_sockets,
          "can_take_calls": random_cafe.can_take_calls,
          "coffee_price": random_cafe.coffee_price,
        }
        })

"""
**********************
Route to get all cafes
**********************
"""
@app.route('/all')
def all():
   
    records = db.session.execute(db.select(Cafe)).scalars().all()  # Fetch all cafe records
    all_cafes = list() # Initialize empty list to store formatted cafe data

    # Iterate through each cafe record
    for cafe in records:
        # Append formatted cafe dictionary to list
        all_cafes.append({
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        # Group amenity properties in sub-dictionary
        "amenities": {
          "seats": cafe.seats,
          "has_toilet": cafe.has_toilet,
          "has_wifi": cafe.has_wifi,
          "has_sockets": cafe.has_sockets,
          "can_take_calls": cafe.can_take_calls,
          "coffee_price": cafe.coffee_price,
        }
        })
    # Return JSON response with all cafes
    return jsonify(all_cafes)

"""
*************************************************
Route to search cafes by location (GET request)
*************************************************
"""
@app.route('/search')
def search():
    
    query_location = request.args.get("loc") # Get location query parameter from URL
    cafes_search_record = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all() # Fetch cafes matching the query location
    all_search_list = [] # Initialize empty list for search results

    # Check if any cafes were found
    if cafes_search_record:
        # Iterate through matching cafes
        for cafe in cafes_search_record:
            # Convert cafe object to dictionary
            dict = cafe.__dict__
            # Remove SQLAlchemy internal state attribute
            del dict['_sa_instance_state']
            # Add formatted cafe to results list
            all_search_list.append(dict)
        # Return list of matching cafes
        return jsonify(all_search_list)
    else:
        # Return error if no cafes found for location
        return jsonify({'error' : "location not available"})


"""
**************************************
Route to add a new cafe (POST request)
**************************************
"""
@app.route('/add', methods=['POST'])
def add():
    # Check if request method is POST
    if request.method == 'POST':
        # Try to create and add new cafe
        try:
            # Create new Cafe instance with form data
            add_cafe = Cafe(
                            # Get cafe name from form
                            name=request.form.get("name"),
                            # Get maps URL from form
                            map_url=request.form.get("map_url"),
                            # Get image URL from form
                            img_url=request.form.get("img_url"),
                            # Get location from form
                            location=request.form.get("loc"),
                            # Convert socket checkbox to boolean
                            has_sockets=bool(request.form.get("sockets")),
                            # Convert toilet checkbox to boolean
                            has_toilet=bool(request.form.get("toilet")),
                            # Convert wifi checkbox to boolean
                            has_wifi=bool(request.form.get("wifi")),
                            # Convert calls checkbox to boolean
                            can_take_calls=bool(request.form.get("calls")),
                            # Get number of seats from form
                            seats=request.form.get("seats"),
                            # Get coffee price from form
                            coffee_price=request.form.get("coffee_price"),
                            )
        # Catch any exceptions during cafe creation
        except Exception as e:
            # Return error response if creation fails
            return jsonify({'error': 'could\'nt post'})
        # Execute if no exception occurs
        else:
            # Add new cafe to database session
            db.session.add(add_cafe)
            # Commit changes to database
            db.session.commit()
            # Return success response
            return jsonify(reponse= {"status" : "suceesfully added new cafe"})
        
"""
*************************************************
Route to update cafe coffee price (PATCH request)
**************************************************
"""
@app.route('/update/<int:cafe_id>', methods = ["PATCH"])
def update(cafe_id):

    new_price = request.args.get("price")   # Get new price from query parameter
    
    # Try to fetch cafe by ID
    try:
        # Retrieve cafe or return 404 if not found
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
    # Catch attribute errors
    except AttributeError:
        # Return 404 error response
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    # Execute if cafe found
    else:
        # Update cafe price with new value
        cafe_to_update.coffee_price = new_price
        # Commit changes to database
        db.session.commit()
        # Return success response with 200 status
        return jsonify(response={"success": "Successfully updated the price."}), 200

"""
****************************************
Route to delete a cafe (DELETE request)
****************************************
"""
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    # Get API key from query parameter
    api_key = request.args.get("api-key")
    # Check if provided API key matches the secret key
    if api_key == "TopSecretAPIKey":
        # Try to fetch cafe by ID
        try:
            # Retrieve cafe or return 404 if not found
            cafe = db.get_or_404(Cafe, cafe_id)
        # Catch attribute errors
        except AttributeError:
            # Return 404 error response
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        # Execute if cafe found
        else:
            # Remove cafe from database session
            db.session.delete(cafe)
            # Commit deletion to database
            db.session.commit()
            # Return success response with 200 status
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    # Execute if API key is incorrect
    else:
        # Return 403 forbidden error response
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


"""
###################################################
Check if script is executed directly (not imported)
#####################################################
"""
if __name__ == '__main__':
    # Get PORT from environment variables, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Start Flask development server on all hosts in debug mode
    app.run(debug=True, host='0.0.0.0', port=port)
