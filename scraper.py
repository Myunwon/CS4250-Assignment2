#-------------------------------------------------------------------------
# AUTHOR: Paul Myung
# FILENAME: scraper.py
# SPECIFICATION: Crawls the Circular Links section starting from the seed URL
#                and prints each page's <h1> text and every URL in seen.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 1 hour
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = [seed]
seen = {seed}

# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    print(soup.h1.get_text())

    # Extracting and processing hyperlinks
    links = []
    for a in soup.find_all("a", href=True):
        link = a["href"]
        if not link.startswith("http"):
            link = baseURL + link
        if link.startswith(seed):
            links.append(link)
    links.sort()

    for link in links:
        if link not in seen:
            seen.add(link)
            frontier.append(link)

# Printing all URLs in seen
for link in seen:
    print(link)