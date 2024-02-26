
-- Schema
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(15) NOT NULL,
  last_name    varchar(15) NOT NULL,
  age          integer NOT NULL,
  subject      integer NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id  serial PRIMARY KEY,
  first_name   varchar(15) NOT NULL,
  last_name    varchar(15) NOT NULL,
  age          integer NOT NULL,
  subject      integer NOT NULL
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id serial PRIMARY KEY,
  subject varchar(25) NOT NULL
);
