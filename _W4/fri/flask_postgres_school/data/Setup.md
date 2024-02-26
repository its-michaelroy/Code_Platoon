1. createdb database name
2. Examine csv & create schema.sql (columns and types) for each table/file
3. Once done, \q psql and run "psql database_name < schema.sql" (Loads schema)
4. psql database_name
5. copy everything for each file IE: \copy table_name FROM 'path/to/file.csv' DELIMITER ',' CSV HEADER;
   \*MAKE SURE YOU'RE CONNECTED TO THE CORRECT DB!!!

6. Setup Flask/SQLAlchemy connect to db path/jsonify to deliver content

7. Create class Table_name(db.Model)
   \*Named after similar tablename(s) in connected DB

8. All attributes need to line up with the columns in the mimicked table.
   IE: class Students(db.Model):
   id = db.Column(db.Integer, primary_key=True) # Columns in students table == Columns in psql Database.
   first_name = db.Column(db.String(15))
   last_name = db.Column(db.String(15))
   age = db.Column(db.Integer)
   subject_id = db.Column(db.Integer)

9. Next create required get methods for each node to serve up the requested content based on requirement IE: Students who have an A, etc

10. Finally, review content and troubleshoot!!
