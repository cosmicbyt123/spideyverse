from flask import Flask, render_template, request ,url_for,redirect,jsonify
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

init_db()   
init_db2()
init_db3()

genai.configure(api_key="AIzaSyB9pF3je4dUwnyyQcbgC_krTRhU6uVlco0")










@app.route('/')
def home():
    return render_template('landingpage.html')


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
    return render_template('seller_platform.html')

@app.route('/Ai', methods=['POST'])
def ai():
    return render_template('AI.html')


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

@app.route('/addtodb', methods=['POST'])
def addtodb():
    image = request.files['image']       # get uploaded file
    desc = request.form['description']   # get text field
    data = (image, desc)       
    save_user3(data)
    return redirect('/sellerplat')
def view():
    with sqlite3.connect("data.db") as conn:
        rows = conn.execute("SELECT id, description FROM uploads").fetchall()
    return render_template('seller_platform.html', rows=rows) 



if __name__ == '__main__':
    app.run(debug=True)
