import sqlite3

# Prompt the user for input
first_name = input("What is the user's first name? ")
last_name = input("What is the user's last name? ")

#Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the members table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        member_activation_date DATE  -- Set datatype as DATE
    )
''')
# Get the current date
import datetime
member_activation_date = datetime.date.today()

# Insert the user into the members table
cursor.execute('''
    INSERT INTO members (first_name, last_name, member_activation_date)
    VALUES (?, ?, ?)
''', (first_name, last_name, member_activation_date))

# Commit the changes and close the connection
conn.commit()
conn.close()
