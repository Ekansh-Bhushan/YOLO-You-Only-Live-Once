import mysql.connector
import os
from random import choice, shuffle
from faker import Faker
from dotenv import load_dotenv

load_dotenv()
SQL_PASSWORD = "manu1234"
SQLpassword = os.getenv(SQL_PASSWORD)

specialties = [
    "Cardiologist",
    "Dermatologist",
    "Endocrinologist",
    "Gastroenterologist",
    "Neurologist",
    "Oncologist",
    "Orthopedic",
    "Pediatrician",
    "Psychiatrist",
    "Pulmonologist",
    "Rheumatologist",
    "Ophthalmologist",
    "Urologist",
    "Obstetrician-Gynecologist",
    "Trichologist",
    "Radiologist",
]

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="manu1234"
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
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS doctors (
               id INT AUTO_INCREMENT PRIMARY KEY,
               username VARCHAR(255),
               firstname VARCHAR(255),
               lastname VARCHAR(255),
               phone VARCHAR(10),
               email VARCHAR(255),
               specialty VARCHAR(255)
               )"""
        )
        print("Table 'doctors' created successfully")
    except mysql.connector.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        cursor.close()

def generate_sample_doctor(fake, specialties):
    return (
        fake.user_name(),
        fake.first_name(),
        fake.last_name(),
        fake.phone_number()[:10],  # Limit phone number length
        fake.email(),
        specialties.pop(),  # Get and remove the last specialty from the list
    )

def insert_sample_doctors(connection, db_name, num_doctors=5):
    cursor = connection.cursor()
    try:
        fake = Faker()
        cursor.execute(f"USE {db_name}")
        shuffle(specialties)  # Shuffle the list of specialties
        for _ in range(num_doctors):
            doctor = generate_sample_doctor(fake, specialties)
            cursor.execute(
                """INSERT INTO doctors (username, firstname, lastname, phone, email, specialty)
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                doctor,
            )
        connection.commit()
        print(f"{num_doctors} sample doctors inserted successfully")
    except mysql.connector.Error as e:
        print(f"Error inserting sample doctors: {e}")
        connection.rollback()
    finally:
        cursor.close()

connection = connect_to_mysql()
if connection:
    create_database(connection, "healthCare")
    create_tables(connection, "healthCare")
    insert_sample_doctors(connection, "healthCare", num_doctors=16)
    connection.close()
