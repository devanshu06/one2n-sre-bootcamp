
# One2n-Assignment
This folder conatins the solution for the bootcamp milestone-1 to run the code directly I have created the make file for this please check the How to run code locally section.

### Problem Statement:
Link for PS: https://one2n.notion.site/1-Create-a-simple-REST-API-Webserver-1f718301897b42f9b39a8fdff6764207

### Pre-Requisites:
To Run this Code on you local you need below things:
* python & pip >= 3.6
* mysql 5.x
* postman
* make

### How to run code locally 

To run the code in your localhost. You need python, pip and mysql installed.

```bash
# This command will check if python is installed or not 
make check_python
```
```bash
# This command will setup the venn for python 
make setup_venv
```
```bash
# This command will install the requirments using the venv
make install
```
```bash
# This command will start the flask app
make start
```

### APIs:

You can find out Postman Collection in the **one2n.postman_collection.json**

* /healthcheck - To check the healh status - [GET] Request
* /api/v1/addstudent - To add the student in the table - [POST] Request
* /api/v1/deletestudent/<id> - To delete student with the id - [DELETE] Request
* /api/v1/allstudent - To get the details of all student from the db - [GET] Request
* /api/v1/student/<id> - To get the student by his id - [GET] Request
* /api/v1/updatestudent/<id> - To updated the data of student by its id - [PUT] Request



