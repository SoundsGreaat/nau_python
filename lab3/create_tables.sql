CREATE SEQUENCE students_id_seq;

CREATE TABLE students
(
    id  INT DEFAULT nextval('students_id_seq') PRIMARY KEY,
    FIO TEXT,
    dob DATE,
    UNIQUE (FIO, dob)
);

CREATE SEQUENCE properties_id_seq;

CREATE TABLE properties
(
    id         INT DEFAULT nextval('properties_id_seq') PRIMARY KEY,
    student_id INT REFERENCES students (id),
    property   TEXT,
    UNIQUE (student_id, property)
);
