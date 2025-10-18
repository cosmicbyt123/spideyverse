from flask import Flask, render_template, request ,url_for,redirect
import sqlite3
import gemini
from buyerdata import init_db, save_user
from sellerdata import init_db2, save_user2
app = Flask(__name__)

init_db()   
init_db2()





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
    save_user2(data)
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
    return redirect('/Ai')



@app.route('/Ai')
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
    return render_template('seller.html')




if __name__ == '__main__':
    app.run(debug=True)
