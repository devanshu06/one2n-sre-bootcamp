import os
import logging
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import db_queries

app = Flask(__name__)

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

def create_database_if_not_exists():
    try:
        connection = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            passwd=DATABASE_PASSWORD
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")
        connection.commit()
    except Error as e:
        logging.error(f"Error initializing database: {str(e)}")
    finally:
        cursor.close()
        connection.close()

DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, FLASK_HOST, FLASK_PORT, DEBUG_MODE = setup_environment_and_logging()

create_database_if_not_exists()

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # age = db.Column(db.Integer, nullable=False)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return {'status': 'OK'}, 200

@app.post('/api/v1/addstudent')
def addstudent():
    data = request.get_json()
    if "name" not in data:
        return {"error": "name field is required"}, 400
    name = data["name"]
    try:
        new_student = Student(name=name)
        db.session.add(new_student)
        db.session.commit()
        return {"id": new_student.id, "message": f"Student {name} created."}, 201
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500

@app.delete('/api/v1/deletestudent/<int:num>')
def deletestudent(num):
    try:
        student = Student.query.get(num)
        if not student:
            return {"message": f"No record found for student with id {num}."}, 404
        db.session.delete(student)
        db.session.commit()
        return {"message": f"Student with id {num} deleted."}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500

@app.get('/api/v1/allstudent')
def allstudent():
    try:
        students = Student.query.all()
        student_list = [{"id": student.id, "name": student.name} for student in students]
        return {"students": student_list}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500

@app.get('/api/v1/student/<int:num>')
def studentbyid(num):
    try:
        student = Student.query.get(num)
        if student is None:
            return {"message": f"Student with id {num} not found."}, 404
        return {"id": num, "name": student.name}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500

@app.put('/api/v1/updatestudent/<int:num>')
def updatestudentbyid(num):
    data = request.get_json()
    if "name" not in data:
        return {"error": "Name field is required"}, 400
    new_name = data["name"]
    try:
        student = Student.query.get(num)
        if student is None:
            return {"error": f"Student with id {num} not found."}, 404
        current_name = student.name
        if current_name == new_name:
            return {"message": "No Change in name detected. Nothing needs to be updated."}, 200
        student.name = new_name
        db.session.commit()
        return {"message": f"Student with id:{num} updated from {current_name} to {new_name}."}, 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=DEBUG_MODE)
