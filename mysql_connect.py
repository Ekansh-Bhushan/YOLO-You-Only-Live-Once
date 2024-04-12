import mysql
import mysql.connector
from dotenv import main
import os

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
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS Test (
            attribute VARCHAR(50),
            value VARCHAR(100)
        )""")
        print("Table 'Test' created successfully")
        
        # Inserting attributes and values
        attributes_values = [
            ('Red Blood Cell Count (RBC)', '4.5-6.0 million cells/mcL (male)'),
            ('Red Blood Cell Count (RBC)', '4.0-5.5 million cells/mcL (female)'),
            ('White Blood Cell Count (WBC)', '4,500-11,000 cells/mcL'),
            ('Hemoglobin (Hgb)', '13.5-17.5 g/dL (male)'),
            ('Hemoglobin (Hgb)', '12.0-15.5 g/dL (female)'),
            ('Hematocrit (Hct)', '40%-50% (male)'),
            ('Hematocrit (Hct)', '36%-46% (female)'),
            ('Platelet Count', '150,000-400,000/mcL'),
            ('Glucose', '70-100 mg/dL (fasting)'),
            ('Sodium', '135-145 mEq/L'),
            ('Potassium', '3.5-5.0 mEq/L'),
            ('Total Protein', '6.0-8.0 g/dL'),
            ('Total Cholesterol', 'Less than 200 mg/dL'),
            ('Alanine Aminotransferase (ALT)', '7-56 units/L'),
            ('Aspartate Aminotransferase (AST)', '10-40 units/L'),
            ('Alkaline Phosphatase (ALP)', '44-147 units/L'),
            ('Total Bilirubin', '0.3-1.2 mg/dL'),
            ('Creatinine', '0.6-1.3 mg/dL (male)'),
            ('Creatinine', '0.5-1.1 mg/dL (female)'),
            ('Blood Urea Nitrogen (BUN)', '7-20 mg/dL'),
            ('Thyroid-Stimulating Hormone (TSH)', '0.4-4.0 mIU/L'),
            ('Free Thyroxine (T4)', '0.8-1.8 ng/dL'),
            ('Prothrombin Time (PT)', '11-13.5 seconds'),
            ('International Normalized Ratio (INR)', '0.8-1.2'),
            ('C-Reactive Protein (CRP)', 'Less than 1.0 mg/dL'),
            ('ABO Blood Group', 'A, B, AB, O'),
            ('Rh Factor', 'Positive (+) or Negative (-)'),
            ('Vitamin D', '30-100 ng/mL'),
            ('Vitamin B12', '200-900 pg/mL'),
            ('Iron', '60-170 mcg/dL'),
            ('Testosterone', '300-1,000 ng/dL (male)'),
            ('Estradiol', '10-40 pg/mL (premenopausal female)'),
            ('Progesterone', '0.1-0.8 ng/mL (follicular phase)')
        ]
        for attribute, value in attributes_values:
            cursor.execute("INSERT INTO Test (attribute, value) VALUES (%s, %s)", (attribute, value))
        print("Attributes and values inserted successfully into the 'Test' table")

    except mysql.connector.Error as e:
        print(f"Error creating tables: {e}")
    finally:
        cursor.close()


connection = connect_to_mysql()
if connection:
    create_database(connection, "health_care")
    create_tables(connection, "health_care")
    connection.close()
