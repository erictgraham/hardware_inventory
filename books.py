import os
import sqlite3
import qrcode


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
        qrcode BLOB
    )
''')

# Get the highest existing id value
c.execute("SELECT MAX(id) FROM books")
highest_id = c.fetchone()[0]

# Assign the highest existing id value if not already assigned
if highest_id is None:
    highest_id = 0

# Increment the highest_id for the next book
highest_id += 1

id = highest_id

# Prompt the user for book information
title = input("What is the book's title? ")
author = input("Who is/are the author(s)? ")
year = int(input("When was the book published (YYYY)? "))
pages = int(input("How many pages is the book? "))
#state = input("What is the state of the book? ")
#if state == "Checked Out":
#    return_date = input("When is the book due to be returned? ")
#elif state == "Overdue":
#    overdue_days = int(input("How many days overdue is the book? "))
#last_read_by = input("Who last read the book? ")
#last_read_date = input("When did they last read it? ")

# Generate the QR code
qrcode_data = f"Book ID: {id}\nTitle: {title}\nAuthor: {author}"
qr = qrcode.QRCode()
qr.add_data(qrcode_data)
qr.make(fit=True)
qrcode_image = qr.make_image()

# Save the QR code image
# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the relative path to the QR code image
qrcode_path = os.path.join(current_dir, "img", "qr", f"{title}.png")
qrcode_image.save(qrcode_path)

# Insert the book into the database
c.execute("INSERT INTO books (id, title, author, published_date, page_length, qrcode) VALUES (?, ?, ?, ?, ?, ?)", (id, title, author, year, pages, qrcode_path))

# Commit the changes and close the connection
conn.commit()
conn.close()
print(f"Book '{title}' added to the library with ID {id}.")