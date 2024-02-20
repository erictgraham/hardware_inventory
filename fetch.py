import sqlite3
from PIL import Image

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Ask the user for the book title
book_title = input("Provide the book title that you would like information on: ")

# Fetch the information for the specified book title
cursor.execute("SELECT * FROM books WHERE title=?", (book_title,))
book_data = cursor.fetchone()

# Check if the book exists in the database
if book_data:
    # Print the retrieved information from the books table
    print("Book ID:", book_data[0])
    print("Book Title:", book_data[1])
    print("Author:", book_data[2])
    print("Publication Year:", book_data[3])
    print("Page Count:", book_data[4])

    # Check if the book ID exists in the logs table
    cursor.execute("SELECT * FROM logs WHERE member_id=?", (book_data[0],))
    log_data = cursor.fetchone()

    if log_data:
        # Fetch the member information from the members table
        cursor.execute("SELECT * FROM members WHERE member_id=?", (log_data[1],))
        member_data = cursor.fetchone()

        # Print the log information along with member information
        print("Last Read by:", member_data[1], member_data[2])
        print("Last Date Read:", log_data[2])

        # Get the QR code path
        qrcode_path = book_data[5]

        # Open the QR code image
        qrcode_image = Image.open(qrcode_path)
        qrcode_image.show()
    else:
        print("Book not found in the logs.")
else:
    print("Book not found in the database.")

# Close the database connection
conn.close()
