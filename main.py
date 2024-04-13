from flask import Flask, render_template,request

from flask_mysqldb import MySQL

from random import choice as r_c

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ekansh@04'
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

        
        

        
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users_db(username, firstname, lastname, phone, email) VALUES (%s, %s, %s, %s, %s)",
                        (username, firstname, lastname, phone, email))
        mysql.connection.commit()
        cur.close()

        return "success" 

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)