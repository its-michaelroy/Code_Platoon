from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Create flask app object
#  The __name__ variable helps Flask determine the root path for the application
app = Flask(__name__)
cors = CORS(app)


# # Create a connection to the database school
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mr@localhost/new_school'

# # Init SQLAlchemy extnesion
# db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True, port=8000)
