import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('library.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table to store the books
cursor.execute('''
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

# Save the changes and close the connection
conn.commit()
conn.close()
