-- -- CREATE TABLE movie (
-- --     movie_id SERIAL PRIMARY KEY,
-- --     movie_name VARCHAR(100) UNIQUE NOT NULL,
-- --     age_limit INT
-- --         NOT NULL
-- --         CHECK(age_limit > 18 AND age_limit < 100)
-- -- );
-- DROP TABLE IF EXISTS social_security CASCADE;

-- CREATE TABLE social_security(
--     social_security_id SERIAL PRIMARY KEY,
--     ssn INT NOT NULL UNIQUE
-- );

-- DROP TABLE IF EXISTS employee;

-- CREATE TABLE employee(
--     employee_id SERIAL PRIMARY KEY,
--     employee_name VARCHAR(90) NOT NULL,
--     ssn_id INT,
--     FOREIGN KEY (ssn_id) 
--         REFERENCES social_security(social_security_id)
-- );

-- INSERT INTO social_security(ssn) VALUES (1234567890);

-- INSERT INTO employee(employee_name, ssn_id) VALUES('Adam Cahan', 1);


-- CREATE TABLE school(
--     school_id SERIAL PRIMARY KEY,
--     school_name VARCHAR(15) NOT NULL UNIQUE
-- );

-- CREATE TABLE student(
--     student_id SERIAL PRIMARY KEY,
--     student_name VARCHAR(20) NOT NULL,
--     -- other details
--     school_id INT NOT NULL,
--     FOREIGN KEY (school_id) REFERENCES school(school_id)
-- );

-- INSERT INTO school(school_name) VALUES ('Eric White');
-- INSERT INTO school(school_name) VALUES ('Garfield');

-- INSERT INTO student(student_name, school_id) VALUES ('Francisco', 1);

-- INSERT INTO student(student_name, school_id) VALUES ('Adam', 1);

-- INSERT INTO student(student_name, school_id) VALUES ('Zaynab', 2);

-- INSERT INTO student(student_name, school_id) VALUES ('Raphael', 2);
DROP TABLE IF EXISTS student CASCADE; 
CREATE TABLE student(
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(20) NOT NULL
);

DROP TABLE IF EXISTS course CASCADE;
CREATE TABLE course(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(20) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS course_students;

CREATE TABLE course_students(
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

INSERT INTO student(student_name) VALUES ('Francisco');
INSERT INTO student(student_name) VALUES ('Adam');
INSERT INTO student(student_name) VALUES ('Zaynab');
INSERT INTO student(student_name) VALUES ('Ralph');

INSERT INTO course(course_name) VALUES ('Python');
INSERT INTO course(course_name) VALUES ('JavaScript');
INSERT INTO course(course_name) VALUES ('SQL');
INSERT INTO course(course_name) VALUES ('OOP');

INSERT INTO course_students(student_id, course_id) VALUES(1,2);
INSERT INTO course_students(student_id, course_id) VALUES(1,1);
INSERT INTO course_students(student_id, course_id) VALUES(1,4);
INSERT INTO course_students(student_id, course_id) VALUES(2,2);
INSERT INTO course_students(student_id, course_id) VALUES(3,2);
INSERT INTO course_students(student_id, course_id) VALUES(3,3);
INSERT INTO course_students(student_id, course_id) VALUES(4,4);