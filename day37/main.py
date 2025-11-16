import requests
from datetime import datetime

# ------------------------
# User and Graph Configuration
# ------------------------
TOKEN = "sn3j49oncsjdn9dqq"  # Your Pixela token, used for authentication
USERNAME = "awapktest"        # Your Pixela username
GRAPHID = "graph3"            # ID of the graph you want to create/post to

# ------------------------
# Function: Create User
# ------------------------
def create_user():
    """
    Creates a new Pixela user account.
    
    Note:
    - This function can only be run once per username.
    - If you try to create a user with the same username, you will get a 409 Conflict error.

    Endpoint:
        POST https://pixe.la/v1/users

    Parameters:
        - token: Your authentication token
        - username: Desired Pixela username
        - agreeTermsOfService: Must be "yes"
        - notMinor: Must be "yes" if not a minor
    """
    endpoint = 'https://pixe.la/v1/users'
    params = {
        'token': TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }
    response = requests.post(endpoint, json=params)
    print(response.text)
#create_user()    

# ------------------------
# Function: Create Graph
# ------------------------
def create_graph():
    """
    Creates a new graph for the user.
    
    Note:
    - Graph IDs must be unique per user.
    - Use this function only once per graph ID.

    Endpoint:
        POST https://pixe.la/v1/users/<username>/graphs

    Graph Parameters:
        - id: Unique graph ID
        - name: Graph name
        - unit: Unit for your data (e.g., commits, hours)
        - type: "int" or "float"
        - color: Graph color (shibafu, momiji, etc.)
    """
    endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'
    params = {
        'id': GRAPHID,
        'name': "Coding Graph",
        'unit': "commit",
        'type': "float",
        'color': "shibafu"
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(endpoint, json=params, headers=headers)
    print(response.text)
#create_graph()
# ------------------------
# Function: Post Data to Graph
# ------------------------
def post_to_graph(quantity='70'):
    """
    Posts a pixel (data point) to the graph for the current day.

    Endpoint:
        POST https://pixe.la/v1/users/<username>/graphs/<graphID>

    Parameters:
        - date: Today's date in YYYYMMDD format
        - quantity: Number to post (e.g., number of commits)
    """
    today = datetime.now().strftime('%Y%m%d')  # Format: YYYYMMDD
    endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}'
    params = {
        'date': today,
        'quantity': str(quantity)
    }
    headers = {
        'X-USER-TOKEN': TOKEN
    }
    response = requests.post(endpoint, json=params, headers=headers)
    print(response.text)
#post_to_graph()
# ------------------------
# Function: Update Graph
# ------------------------
def update_graph():
    """
    Updates the graph's metadata such as name, type, unit, and color.

    Endpoint:
        PUT https://pixe.la/v1/users/<username>/graphs/<graphID>

    Parameters:
        - name: New graph name
        - unit: Unit of measurement
        - type: "int" or "float"
        - color: Graph color
    """
    endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}'
    params = {
        'name': "Coding Graph Updated",
        'unit': "commit",
        'type': "int",
        'color': "momiji"
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.put(endpoint, json=params, headers=headers)
    print(response.text)
#update_graph()
# ------------------------
# Function: Delete Pixel
# ------------------------
def delete_pixel():
    """
    Deletes today's pixel from the graph.

    Endpoint:
        DELETE https://pixe.la/v1/users/<username>/graphs/<graphID>/<date>

    Note:
        - Only the pixel for the specified date will be deleted.
        - Headers must include X-USER-TOKEN for authentication.
    """
    today = datetime.now().strftime('%Y%m%d')  # Format: YYYYMMDD
    endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/{today}'
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    data_delete = {
        'quantity' :'20'
    }
    response = requests.delete(endpoint, json=data_delete ,headers=headers)
    print(response.text)
#delete_pixel()