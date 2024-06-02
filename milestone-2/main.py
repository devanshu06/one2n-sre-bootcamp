import os
import logging
from flask import Flask, request
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import db_queries

load_dotenv()

app = Flask(__name__)
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")

logging.basicConfig(level=logging.INFO)

logging.info(f"DB Host: {DATABASE_HOST}")
logging.info(f"DB User: {DATABASE_USER}")
# logging.info(f"DB Password: {DATABASE_PASSWORD}")
logging.info(f"DB Name: {DATABASE_NAME}")

def initialize_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            passwd=DATABASE_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")
        connection.database = DATABASE_NAME
        cursor.execute(db_queries.CREATE_STUDENT_TABLE)
        connection.commit()
    except Error as e:
        logging.error(f"Error initializing database: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def get_db_connection():
    try:
        initialize_database()
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            passwd=DATABASE_PASSWORD,
            database=DATABASE_NAME
        )
        return connection
    except Error as e:
        logging.error(f"Error connecting to database: {str(e)}")
        return None

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {'status': 'OK'}, 200

@app.post('/api/v1/addstudent')
def addstudent():
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}, 500
    try:
        data = request.get_json()
        if "name" not in data:
            return {"error": "name field is required"}, 400
        name = data["name"]
        cursor = connection.cursor()
        cursor.execute(db_queries.INSERT_STUDENT, (name,))
        connection.commit()
        cursor.execute("SELECT LAST_INSERT_ID()")
        student_id = cursor.fetchone()[0]
        return {"id": student_id, "message": f"Student {name} created."}, 201
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.delete('/api/v1/deletestudent/<int:num>')
def deletestudent(num):
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}, 500
    try:
        cursor = connection.cursor()
        cursor.execute(db_queries.STUDENT_BY_ID, (num,))
        student = cursor.fetchone()
        if not student:
            return {"message": f"No record found for student with id {num}."}, 404
        cursor.execute(db_queries.DELETE_STUDENT, (num,))
        connection.commit()
        return {"message": f"Student with id {num} deleted."}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.get('/api/v1/allstudent')
def allstudent():
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}, 500
    try:
        cursor = connection.cursor()
        cursor.execute(db_queries.ALL_STUDENT)
        students = cursor.fetchall()
        student_list = [{"id": student[0], "name": student[1]} for student in students]
        return {"students": student_list}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.get('/api/v1/student/<int:num>')
def studentbyid(num):
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}, 500
    try:
        cursor = connection.cursor()
        cursor.execute(db_queries.STUDENT_BY_ID, (num,))
        student = cursor.fetchone()
        if student is None:
            return {"message": f"Student with id {num} not found."}, 404
        return {"id": num, "name": student[0]}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.put('/api/v1/updatestudent/<int:num>')
def updatestudentbyid(num):
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}, 500
    try:
        data = request.get_json()
        if "name" not in data:
            return {"error": "Name field is required"}, 400
        new_name = data["name"]
        cursor = connection.cursor()
        cursor.execute(db_queries.STUDENT_BY_ID, (num,))
        student = cursor.fetchone()
        if student is None:
            return {"error": f"Student with id {num} not found."}, 404
        current_name = student[0]
        if current_name == new_name:
            return {"message": "No Change in name detected. Nothing needs to be updated."}, 200
        cursor.execute(db_queries.UPDATE_STUDENT_BY_ID, (new_name, num))
        connection.commit()
        return {"message": f"Student with id:{num} updated from {current_name} to {new_name}."}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
