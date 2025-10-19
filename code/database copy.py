import os, sqlite3

base_folder = "C:/Users/WASIM/Desktop/Hackthon/spideyverse/code/static/images/kids_wear"

conn = sqlite3.connect("women_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price TEXT,
    image_path TEXT,
    category TEXT
)
""")

for category in os.listdir(base_folder):
    cat_path = os.path.join(base_folder, category)
    if os.path.isdir(cat_path):
        for img in os.listdir(cat_path):
            if img.endswith(('.jpg', '.jpeg', '.png')):
                path = f"images/mens_wear/{category}/{img}"
                name = os.path.splitext(img)[0]
                price = "$49.99"
                cursor.execute("INSERT INTO products (name, price, image_path, category) VALUES (?, ?, ?, ?)",
                               (name, price, path, category))

conn.commit()
conn.close()
print("✅ All categories inserted automatically!")
