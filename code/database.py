import sqlite3


def init_db3():
    with sqlite3.connect("data.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS uploads (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT,
                        image BLOB)''')
        


def save_user3(data):
    image,desc = data
    img_bytes = image.read()
    with sqlite3.connect("data.db") as conn:
        conn.execute(
            "INSERT INTO uploads (description, image) VALUES (?, ?)",
            (desc, img_bytes)
        )
        conn.commit()
   

 