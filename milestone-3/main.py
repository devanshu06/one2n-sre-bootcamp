import os
import logging
from flask import Flask, request
import mysql.connector
from mysql.connector import pooling, Error
from dotenv import load_dotenv
import db_queries

def setup_environment_and_logging():
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_USER = os.environ["DATABASE_USER"]
    DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    DATABASE_NAME = os.environ["DATABASE_NAME"]
    FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
    FLASK_PORT = int(os.environ.get("FLASK_PORT", 5000))
    DEBUG_MODE = os.environ.get("DEBUG_MODE", "False").lower() == 'true'

    logging.info(f"DB Host: {DATABASE_HOST}")
    logging.info(f"DB User: {DATABASE_USER}")
    # logging.info(f"DB Password: {DATABASE_PASSWORD}")
    logging.info(f"DB Name: {DATABASE_NAME}")

    if DEBUG_MODE:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    return DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, FLASK_HOST, FLASK_PORT, DEBUG_MODE

DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, FLASK_HOST, FLASK_PORT, DEBUG_MODE = setup_environment_and_logging()

app = Flask(__name__)

def initialize_database():
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
        cursor.close()
        connection.close()

    dbconfig = {
        "host": DATABASE_HOST,
        "user": DATABASE_USER,
        "password": DATABASE_PASSWORD,
        "database": DATABASE_NAME,
    }

    return pooling.MySQLConnectionPool(pool_name="mypool",
                                       pool_size=10,
                                       pool_reset_session=True,
                                       **dbconfig)

connection_pool = initialize_database()

def get_db_connection():
    try:
        connection = connection_pool.get_connection()
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
    data = request.get_json()
    if "name" not in data:
        return {"error": "name field is required"}, 400
    name = data["name"]
    try:
        cursor = connection.cursor()
        cursor.execute(db_queries.INSERT_STUDENT, (name,))
        connection.commit()
        cursor.execute("SELECT LAST_INSERT_ID()")
        student_id = cursor.fetchone()[0]
        return {"id": student_id, "message": f"Student {name} created."}, 201
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500


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


@app.put('/api/v1/updatestudent/<int:num>')
def updatestudentbyid(num):
    connection = get_db_connection()
    if not connection:
        return {"error": "Database connection failed"}, 500
    data = request.get_json()
    if "name" not in data:
        return {"error": "Name field is required"}, 400
    new_name = data["name"]
    try:
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


if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=DEBUG_MODE)
