import mysql
import mysql.connector
from dotenv import main

main.load_dotenv()

SQLpassword = os.getenv("SQL_PASSWORD")

# Function to connect to MySQL server
def connect_to_mysql():
    try:
       
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=SQLpassword
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        return None

def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print(f"Database '{db_name}' created successfully")
    except mysql.connector.Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()


def create_tables(connection, db_name):
    cursor = connection.cursor()
    try:
       
        cursor.execute(f"USE {db_name}")
        cursor.execute("""CREATE TABLE IF NOT EXISTS patients (
            patient_id INT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            contact_number VARCHAR(20)
        )""")
        print("Table 'patients' created successfully")

        
        cursor.execute("""CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            specialization VARCHAR(100),
            contact_number VARCHAR(20),
            patient_id INT,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )""")
        print("Table 'doctors' created successfully")

        cursor.execute("""CREATE TABLE IF NOT EXISTS diseases (
            disease_id INT PRIMARY KEY,
            disease_name VARCHAR(100) UNIQUE NOT NULL,
            specialization VARCHAR(100)
        )""")
        print("Table 'diseases' created successfully")
    except mysql.connector.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        cursor.close()


connection = connect_to_mysql()
if connection:
    create_database(connection, "health_care")
    create_tables(connection, "health_care")
    connection.close()
