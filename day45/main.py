from bs4 import BeautifulSoup
import requests
import lxml

# -------------------------------------------------------------- #
# FUNCTION: intro()
# Demonstrates how to parse a local HTML file using BeautifulSoup.
# Shows how to:
#   - Read HTML
#   - Access tags (title, a, h1)
#   - Use find() and find_all()
#   - Use CSS selectors (select, select_one)
#   - Print HTML in formatted style (prettify)
# -------------------------------------------------------------- #
def intro():
    # Read the HTML content from a local file named "website.html"
    with open('website.html') as r:
        html_info = r.read()

    # Create BeautifulSoup object using the html.parser engine
    soup = BeautifulSoup(html_info, "html.parser")

    print(soup)
    print('---------------------------#####################-------------------------')

    # Access the <title> tag and its properties
    print(soup.title)          # Entire <title> tag
    print(soup.title.name)     # Tag name: "title"
    print(soup.title.string)   # Text inside the title tag

    # Access <a> and <h1> tags
    print(soup.a)
    print(soup.h1)

    # ---------------------------------------------------------- #
    # find_all() returns ALL matching results
    # Loop through every <a> tag on the page and print:
    #   - The anchor text
    #   - The href link
    # ---------------------------------------------------------- #
    all_anchor_tags = soup.find_all(name="a")
    for tags in all_anchor_tags:
        print(tags.string)
        print(tags.get("href"))

    # ---------------------------------------------------------- #
    # find() returns only the FIRST matching element
    # Here we find <h1 id="name">...</h1>
    # ---------------------------------------------------------- #
    print(soup.find(name="h1", id="name"))

    # Find all elements that have CSS class="heading"
    print(soup.find_all(class_="heading"))

    # ---------------------------------------------------------- #
    # CSS selectors:
    #   - select_one(): returns one element
    #   - select(): returns all matching elements
    # ---------------------------------------------------------- #
    company_url = soup.select_one(selector="p a")   # <p> <a> inside
    print(company_url)

    name = soup.select_one(selector="#name")        # element with id="name"
    print(name)

    print(soup.select(selector=".heading"))         # all elements with class="heading"

    print('---------------------------#####################-------------------------')

    # Prettify prints the HTML with indentation
    print(soup.prettify())


######################_________________________________#########################0

# -------------------------------------------------------------- #
# SCRAPING HACKER NEWS (news.ycombinator.com)
# Steps:
#   - Send GET request to Hacker News
#   - Parse HTML
#   - Extract article titles
#   - Extract upvote counts
#   - Match article titles with their upvotes
# -------------------------------------------------------------- #

reponse = requests.get(url="https://news.ycombinator.com/news")
hacker_news = reponse.text

# Create BeautifulSoup object from the Hacker News HTML page
soup = BeautifulSoup(hacker_news, "html.parser")

# Extract all upvote spans (e.g., <span class="score">42 points</span>)
upvotes = soup.find_all(name="span", class_="score")

# Extract all article title lines (<span class="titleline">…</span>)
titles = soup.find_all(class_="titleline")

try:
    for title in titles:
        # Get index of the current article
        article_index = titles.index(title)

        # Extract the <a> tag inside the titleline span
        article = title.find(name="a")

        # Print article index, title text, and corresponding upvote count
        print(f'{article_index} {article.get_text()}, upvotes : {upvotes[article_index].text}')

except Exception as e:
    # Handles any mismatch errors (e.g., upvote missing)
    print(e)
