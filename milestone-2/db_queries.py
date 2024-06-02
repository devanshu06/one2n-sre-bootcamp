CREATE_STUDENT_TABLE = (
    "CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);"
)
INSERT_STUDENT = (
    "INSERT INTO student (name) VALUES (%s);"
)
DELETE_STUDENT = (
    "DELETE FROM student WHERE id = %s;"
)
ALL_STUDENT = (
    "SELECT * from student;"
)
STUDENT_BY_ID = (
    "SELECT name from student where id = %s;"
)
UPDATE_STUDENT_BY_ID = (
    "UPDATE student set name = %s where id = %s"
)