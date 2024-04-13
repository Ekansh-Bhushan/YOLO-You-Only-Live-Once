from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration for users database
app.config['MYSQL_USERS_HOST'] = 'localhost'
app.config['MYSQL_USERS_USER'] = 'root'
app.config['MYSQL_USERS_PASSWORD'] = 'Ekansh@04'
app.config['MYSQL_USERS_DB'] = 'users_db'


# Configuration for doctors database
# app.config['MYSQL_DOCTORS_HOST'] = 'localhost'
# app.config['MYSQL_DOCTORS_USER'] = 'root'
# app.config['MYSQL_DOCTORS_PASSWORD'] = 'manu1234'
# app.config['MYSQL_DOCTORS_DB'] = 'doctors_db'

mysql_users = MySQL(app)
# mysql_doctors = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # Access users database
        cur = mysql_users.connection.cursor()
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']

        cur.execute("INSERT INTO users_db(username, firstname, lastname, phone, email) VALUES (%s, %s, %s, %s, %s)",
                    (username, firstname, lastname, phone, email))
        mysql_users.connection.commit()
        cur.close()
        return "User registration success"
    return render_template('index.html')

# @app.route('/doctor_reg', methods=['GET', 'POST'])
# def doctors():
#     if request.method == "POST":
#         # Access doctors database
#         cur = mysql_doctors.connection.cursor()
#         username = request.form['username']
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         phone = request.form['phone']
#         email = request.form['email']
#         spec = request.form['spec']
        
#         cur.execute("INSERT INTO doctors_db(username, firstname, lastname, phone, email, spec) VALUES (%s, %s, %s, %s, %s, %s)",
#                     (username, firstname, lastname, phone, email, spec))
#         mysql_doctors.connection.commit()
#         cur.close()
#         return "Doctor registration success"
#     return render_template('doctor_reg.html')

if __name__ == "__main__":
    app.run(debug=True)
