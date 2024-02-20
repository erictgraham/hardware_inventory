import sqlite3
from datetime import datetime, timedelta

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Check if the member exists in the members table
first_name = input("What is the first name of the person wanting to checkout a book? ")
last_name = input("What is their last name? ")

cursor.execute("SELECT * FROM members WHERE first_name = ? AND last_name = ?", (first_name, last_name))
member = cursor.fetchone()

if member:
    member_id = member[0]  # Assuming the member_id is the first column in the members table
    # Continue with the rest of the code
    # ...
else:
    print("Sorry, the member does not exist.")

book_title = input("What book is being checked out? ")

# Check if the book exists in the books table
cursor.execute("SELECT * FROM books WHERE title = ?", (book_title,))
book = cursor.fetchone()

if book:
    book_id = book[0]  # Assuming the book_id is the first column in the books table
    # Continue with the rest of the code
    # Check if the book is available
    # Add a foreign key constraint to the logs table
    cursor.execute("PRAGMA foreign_keys = ON")

    # Modify the SQL query to use the correct column name
    cursor.execute("SELECT * FROM logs WHERE book_id = ? AND return_date IS NULL", (book_id,))
    row = cursor.fetchone()

    if row:
        print("Sorry, the book is already checked out.")
    else:
        # Get the current date and calculate the due date
        current_date = datetime.now().date()
        due_date = current_date + timedelta(days=30)

        # Insert the checkout record into the logs table
        cursor.execute("INSERT INTO logs (member_id, book_id, checkout_date, due_date) VALUES (?, ?, ?, ?)",
                       (member_id, book_id, current_date, due_date))

        # Update the book state to "Checked Out"
        cursor.execute("UPDATE books SET state = ? WHERE title = ?", ("Checked Out", book_title))

        conn.commit()

        print("Book checked out successfully.")

    # Close the database connection
    conn.close()