"""
Scrapes the top 100 movie titles from Empire Online's archived webpage and writes them to a text file.
Steps:
1. Sends a GET request to the specified archived URL.
2. Parses the HTML response using BeautifulSoup.
3. Extracts all movie titles from <h3> elements with class "title".
4. Reverses the list to maintain the correct ranking order.
5. Writes each movie title to 'movies.txt', one per line.
Exceptions:
- Any file writing errors are caught and printed.

"""
from bs4 import BeautifulSoup # librabry used for web scraping
import requests  # Import the requests library to handle HTTP requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")  # Send a GET request to the specified URL
web_reponse = response.text  # Get the HTML content of the response

movie_soup = BeautifulSoup(web_reponse, "html.parser")  # Parse the HTML content using BeautifulSoup

titles = movie_soup.find_all(name="h3", class_="title")  # Find all <h3> elements with class 'title' (movie titles)
titles_list = [movie.get_text() for movie in titles]  # Extract the text from each title element and store in a list
titles_list.reverse()  # Reverse the list to maintain the correct ranking order

try:
    with open("movies.txt", mode="w", encoding="utf-8") as file:  # Open 'movies.txt' for writing with UTF-8 encoding
        for movie_title in titles_list:  # Iterate over each movie title in the list
            file.write(f'{movie_title}\n')  # Write the movie title to the file, followed by a newline
except Exception as e:  # Catch any exceptions that occur during file writing
    print(e)  # Print the exception message
    