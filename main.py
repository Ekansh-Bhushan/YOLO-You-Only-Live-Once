from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'manu1234'
app.config['MYSQL_DB'] = 'users_db'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users_db(name,phone,email) VALUES (%s, %s,%s)", (name,phone,email))
        mysql.connection.commit()
        cur.close()
        return "success"
    return render_template('index.html')

if __name__ == "__main__":
    
    app.run(debug=True)