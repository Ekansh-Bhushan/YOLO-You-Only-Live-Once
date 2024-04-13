from flask import Flask, render_template,request
from beem import Hive
from flask_mysqldb import MySQL
import os
from beem.account import Account
from random import choice as r_c

app = Flask(__name__)
hive = Hive()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'manu1234'
app.config['MYSQL_DB'] = 'users_db'
# app.config['MYSQL_DB'] = 'doctors_db'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        # dob1=request.form['dob1']
        active_key = os.getenv('HIVE_ACTIVE_KEY')

        try:
            # account = hive.get_account(username)
            account = Account(username, blockchain_instance=hive)

            # Performing the blockchain transaction
            tx = account.transfer(to='maanit', amount=1.0, asset='HBD', memo='This is a test transfer', key=active_key)

            # Inserting data into MySQL database
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users_db(username, firstname, lastname, phone, email) VALUES (%s, %s, %s, %s, %s)",
                        (username, firstname, lastname, phone, email))
            mysql.connection.commit()
            cur.close()

            return "success"
        except Exception as e:
            return str(e)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)