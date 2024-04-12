from flask import Flask, render_template,request
from flask_mysqldb import MySQL
from random import choice as r_c

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER1'] = 'root'
app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'manu1234'

# Configuration for users database
app.config['MYSQL_USERS_HOST'] = 'localhost'
app.config['MYSQL_USERS_DB'] = 'users_db'

# Configuration for doctors database
app.config['MYSQL_DOCTORS_HOST'] = 'localhost'
app.config['MYSQL_DOCTORS_DB'] = 'doctors_db'

mysql_users = MySQL(app)
mysql_doctors = MySQL(app)

mysql_users = MySQL(app)
mysql_doctors = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        # dob1=request.form['dob1']
        cur = mysql_users.connection.cursor() 

        cur.execute("INSERT INTO users_db(username,firstname,lastname,phone,email) VALUES (%s, %s,%s,%s,%s)", (username,firstname,lastname,phone,email,))
        mysql_users.connection.commit()
        cur.close()
        return "success"
    return render_template('index.html')

@app.route('/doctor_reg', methods=['GET', 'POST'])
def doctors():
    if request.method == "POST":
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        spec=request.form['spec']
        
        
        cur1 = mysql_doctors.connection.cursor() 
        
        cur1.execute("INSERT INTO doctors_db(username,firstname,lastname,phone,email,spec) VALUES (%s, %s,%s,%s,%s,%s)", (username,firstname,lastname,phone,email,spec))
        # SEED = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_1234567890#"

        mysql_doctors.connection.commit()
        cur1.close()
        return "success"
    return render_template('doctor_reg.html')

if __name__ == "__main__":
    app.run(debug=True)