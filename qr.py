import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Create a table to store the books
c.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        published_date TEXT,
        page_length INTEGER,
        qrcode TEXT,
        last_read_by TEXT,
        last_read_date TEXT
    )
''')

# Get the lowest available id value
c.execute("SELECT MIN(id) FROM books")
lowest_id = c.fetchone()[0]

# Assign the lowest available id value if not already assigned
if lowest_id is None:
    lowest_id = 0

# Increment the lowest_id for the next book
lowest_id += 1

id = lowest_id

# Prompt the user for book information
title = input("What is the book's title? ")
author = input("Who is/are the author(s)? ")
year = int(input("When was the book published (YYYY)? "))
pages = int(input("How many pages is the book? "))
last_read_by = input("Who last read the book? ")
last_read_date = input("When did they last read it? ")
qrcode = input("Provide the QR code path for the book: ")

# Insert the book into the database
c.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, title, author, year, pages, qrcode, last_read_by, last_read_date))

# Commit the changes and close the connection
conn.commit()
conn.close()
