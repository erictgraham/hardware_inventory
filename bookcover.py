import requests
import os
from bs4 import BeautifulSoup
import pyautogui
import sqlite3
import requests
import os
from bs4 import BeautifulSoup
import pyautogui
import sqlite3

# Prompt the user for the QR code path
# Prompt the user for the book title
book_title = input("What book title do you want an image for? ")

# Connect to the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Execute a query to retrieve the book information
cursor.execute("SELECT title, author, published_date FROM books WHERE title = ?", (book_title,))
result = cursor.fetchone()

if result:
    # Extract the book information
    title, author, published_date = result

    # Construct the search query
    search_query = f"Book cover {title} {author} {published_date}"

    # Rest of the code...
else:
    print("Book not found in the database.")
# Perform a web search for the book cover image
search_url = f"https://www.image.google.com/search?q={search_query}&tbm=isch"

# Send a GET request to the search URL
response = requests.get(search_url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")

# Find the first image result
image_result = soup.find("img")

# Get the source URL of the image
image_url = image_result["src"]

# Download the image
image_response = requests.get(image_url)
image_path = os.path.join(os.getcwd(), "book_cover.jpg")
with open(image_path, "wb") as image_file:
    image_file.write(image_response.content)

# Display the downloaded image
# Prompt the user for the book title
book_title = input("What book title do you want an image for? ")

# Connect to the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Execute a query to retrieve the book information
cursor.execute("SELECT title, author, published_date FROM books WHERE title = ?", (book_title,))
result = cursor.fetchone()

if result:
    # Extract the book information
    title, author, published_date = result

    # Construct the search query
    search_query = f"Book cover {title} {author} {published_date}"

    # Perform a web search for the book cover image
    search_url = f"https://www.google.com/search?q={search_query}&tbm=isch"

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first image result
    image_result = soup.find("img")

    # Get the source URL of the image
    image_url = image_result["src"]

    # Download the image
    image_response = requests.get(image_url)
    image_path = os.path.join(os.getcwd(), "inventory", "img", "bookcover", f"{title.lower().replace(' ', '')}_bookcover.png")
    with open(image_path, "wb") as image_file:
        image_file.write(image_response.content)

    # Display the downloaded image
    pyautogui.alert(text="Book cover image downloaded!", title="Success", button="OK")
else:
    print("Book not found in the database.")
image_response = requests.get(image_url)
image_path = os.path.join(os.getcwd(), "book_cover.jpg")
with open(image_path, "wb") as image_file:
    image_file.write(image_response.content)

# Display the downloaded image
pyautogui.alert(text="Book cover image downloaded!", title="Success", button="OK")
print("Book not found in the database.")
search_url = f"https://www.image.google.com/search?q={search_query}&tbm=isch"
