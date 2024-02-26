# Import flask for webserver & jsonify to serve data properly
# Require SQLAlchemy to connect flask/webserver to the psql database. Allows for access to db & ability to CRUD data.
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# Create flask app object
#  The __name__ variable helps Flask determine the root path for the application
app = Flask(__name__)

# Create a connection to the database school
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mr@localhost/new_school'

# Init SQLAlchemy extnesion
db = SQLAlchemy(app)

# Create a class called Students to represent the students table in the database
# When we create a class that inherits from db.Model, we are telling SQLAlchemy that this class is a table in the database.
    #When the Students.query.filter(students.age > 20).all() is executed, SQLAlchemy will generate a SQL query to retrieve all records from the 'students' table where the 'age' column is greater than 20.
    # SQLAlchemy references the 'students' table by the name of the class that represents it. In this case, the 'students' table is referenced by the 'Students' class and the 'age' column is referenced by the 'age' attribute of the 'Students' class.
class Students(db.Model): # This class represents the students table in the database
    id = db.Column(db.Integer, primary_key=True) # Columns in students table == Columns in psql Database.
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Columns in students table == Columns in psql Database.
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(25))


@app.route('/students', methods=['GET'])
def get_all_students():
    all_students = Students.query.all()
    serialized_students = [{
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age,
        'class':{
            'subject': Subjects.subject[Students.subject]
        }
    } for student in all_students]
    return jsonify(serialized_students)


# @app.route('/students', methods=['GET'])
# def get_old_students():
#     old_students = Students.query.filter(Students.age > 20).all()
#     #Turn into a list of objects
#     serialized_students = [{
#         'id': student.id,
#         'first_name': student.first_name,
#         'last_name': student.last_name,
#         'age': student.age,
#         'grade': student.grade
#     } for student in old_students]
#     return jsonify(serialized_students)

# @app.route('/young_students', methods=['GET'])
# def get_young_students():
#     young_students = Students.query.filter(Students.age < 21).all()
#     serialized_students = [{
#         'id': student.id,
#         'first_name': student.first_name,
#         'last_name': student.last_name,
#         'age': student.age,
#         'grade': student.grade
#     } for student in young_students]
#     return jsonify(serialized_students)

# Returns an array of all students.

# # Returns an array of student objects where students < 21 and grade of "A."
# @app.route('/advance_students', methods=['GET'])
# def get_advance_students():
#     advance_students = Students.query.filter(Students.age < 21, Students.grade == 'A').all()
#     serialized_students = [{
#         'id': student.id,
#         'first_name': student.first_name,
#         'last_name': student.last_name,
#         'age': student.age,
#         'grade': student.grade
#     } for student in advance_students]
#     return jsonify(serialized_students)

# # Returns an array of 'first_name' and 'last_name'.
# @app.route('/student_names', methods=['GET'])
# def get_student_names():
#     student_names = Students.query.with_entities(Students.first_name, Students.last_name).all()
#     serialized_students = [{
#         'first_name': student.first_name,
#         'last_name': student.last_name
#     } for student in student_names]
#     return jsonify(serialized_students)

# # Returns an array of 'student_name' and 'age'.
# @app.route('/student_ages', methods=['GET'])
# def get_student_ages():
#     student_ages = Students.query.with_entities(Students.first_name + ' ' + Students.last_name, Students.age).all()
#     serialized_students = [{
#         'student_name': student[0],
#         'age': student[1]
#     } for student in student_ages]
#     return jsonify(serialized_students)




#Start the Flask app/server with debugging on port 8000
if __name__ == '__main__':
    app.run(debug=True, port=8000)
