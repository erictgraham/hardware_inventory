import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create the Logs table
cursor.execute('''
    CREATE TABLE Logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        FOREIGN KEY (member_id) REFERENCES Members(id),
        FOREIGN KEY (book_id) REFERENCES Books(id),
        state TEXT,
        last_read_date DATE,
        return_date DATE,
        overdue_days INTEGER

    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
