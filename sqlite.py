import sqlite3

def setup_database():
    conn = sqlite3.connect('lab_inventory.db')
    c = conn.cursor()
    
    # Create equipment table
    c.execute('''CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        barcode TEXT UNIQUE NOT NULL
    )''')
    
    # Create checkouts table
    c.execute('''CREATE TABLE IF NOT EXISTS checkouts (
        id INTEGER PRIMARY KEY,
        equipment_id INTEGER NOT NULL,
        user TEXT NOT NULL,
        checkout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        return_date TIMESTAMP,
        FOREIGN KEY(equipment_id) REFERENCES equipment(id)
    )''')
    
    conn.commit()
    conn.close()

setup_database()
