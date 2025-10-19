from flask import Flask,send_file, render_template, request ,url_for,redirect,jsonify
import sqlite3
from buyerdata import init_db, save_user
from sellerdata import init_db2, save_user2
import google.generativeai as genai
from PIL import Image
import io
import google.generativeai as genai
from google.generativeai import types
from database import init_db3, save_user3

app = Flask(__name__)
import io

init_db()   
init_db2()
init_db3()

genai.configure(api_key="AIzaSyB9pF3je4dUwnyyQcbgC_krTRhU6uVlco0")










@app.route('/')
def home():
    return render_template('landingpage.html')

@app.route('/product')
def product():
    return render_template('products.html')

@app.route('/login')
def login():
    
    return render_template('login.html')


@app.route('/submituser', methods=['POST'])
def submituser():
    data = (
        request.form['username'],
        request.form['address'],
        request.form['pincode'],
        request.form['state'],
        request.form['mobile'],
        request.form['door_number'],
        request.form['color']
    )
    save_user(data)
    return redirect('/mencat')

@app.route('/submitseller', methods=['POST'])
def submitseller():
    data = (
        request.form['username'],
        request.form['address'],
        request.form['pincode'],
        request.form['state'],
        request.form['mobile'],
        request.form['door_number'],
        request.form['shopname'],
        request.form['gstnumber']
    )
    save_user2(data)
    return redirect('/sellerplat')


@app.route('/sellerplat')
def platform():
    with sqlite3.connect("data.db") as conn:
     rows = conn.execute("SELECT id, description FROM uploads").fetchall()
    return render_template('seller_platform.html', rows=rows)
    return render_template('seller_platform.html')

@app.route('/Ai', methods=['POST'])
def ai():
    return render_template('AI.html')

@app.route('/rebuyer')
def rebuyer():
    return render_template('user_real.html')

@app.route('/buyer')
def buyer():
    
    return render_template('buyer.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/mencat')
def mencat():
    return render_template('men_catgeory.html')

@app.route('/seller')
def seller():
    return render_template('sellerlogin.html')

#

@app.route('/addtodb', methods=['POST'])
def addtodb():
    desc = request.form['description']
    img = request.files['image'].read()
    with sqlite3.connect("data.db") as conn:
        conn.execute("INSERT INTO uploads (description, image) VALUES (?, ?)", (desc, img))
    return redirect('/sellerplat')


@app.route('/image/<int:id>')
def image(id):
    with sqlite3.connect("data.db") as conn:
        row = conn.execute("SELECT image, description FROM uploads WHERE id=?", (id,)).fetchone()
    if row:

        image_bytes, description = row
        return send_file(io.BytesIO(image_bytes), mimetype='image/jpeg')
    return redirect('/sellerplat')
@app.route('/product', methods=['GET'])
def get_products():

    with sqlite3.connect("data.db") as conn:
        rows = conn.execute("SELECT id, description FROM uploads").fetchall()
    products = [{'id': row[0], 'description': row[1]} for row in rows]
    print(products)
    return render_template('products.html', products=products)





if __name__ == '__main__':
    app.run(debug=True)
