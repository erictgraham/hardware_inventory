import sqlite3

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
    # Print the retrieved information
    print("Book Title:", book_data[1])
    print("Author:", book_data[2])
    print("Publication Year:", book_data[3])
    print("Page Count", book_data[4])
    print("Last Read by", book_data[6])
    print("Last Date Read", book_data[7])
else:
    print("Book not found in the database.")

# Close the database connection
conn.close()
