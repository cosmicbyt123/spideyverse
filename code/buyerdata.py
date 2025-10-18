import sqlite3

DB_FILE = 'buyer.db'

def init_db2():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    address TEXT,
                    pincode TEXT,
                    state TEXT,
                    mobile TEXT,
                    door_number TEXT,
                    shopname TEXT,
                    
                    )''')
    conn.commit()
    conn.close()

def save_user2(data):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (username, address, pincode, state, mobile, door_number, color) VALUES (?, ?, ?, ?, ?, ?, ?)",
        data
    )
    conn.commit()
    conn.close()
