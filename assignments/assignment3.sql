# Working with databases
#
# This script will delete and then remake the tables for this assignment.
# Load the script when you need to "reset" things.
# You will also add your solutions at the bottom.

DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
CREATE TABLE students (
    id    INT  UNIQUE   NOT NULL AUTO_INCREMENT,
    login VARCHAR(20) UNIQUE NOT NULL,
    first VARCHAR(20),
    last  VARCHAR(20),
    credits INT DEFAULT 0,
    gpa     DOUBLE DEFAULT 0,
    PRIMARY KEY (id)
);
CREATE TABLE courses (
    id     INT  UNIQUE   NOT NULL AUTO_INCREMENT,
    prefix CHAR(4) NOT NULL,
    no     INT NOT NULL,
    title  VARCHAR(55) NOT NULL,
    credits INT NOT NULL DEFAULT 4,
    UNIQUE KEY fullCode (prefix, no),
    PRIMARY KEY (id)
);
CREATE TABLE enrollments (
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    letter_grade  CHAR(2),
    point_grade   DOUBLE,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id)  REFERENCES courses(id) ON DELETE CASCADE,
    PRIMARY KEY (student_id, course_id)
);

INSERT INTO students (login, first, last) VALUES
    ("somebodyj1", "Joe", "Somebody"),
    ("somebodyj2", "Joel", "Somebody"),
    ("otherp1", "Peter", "Other"),
    ("otherm1", "Mary", "Other"),
    ("doem1", "Mary", "Doe"),
    ("doep1", "Peter", "Doe"),
    ("doed1", "David", "Doe");

INSERT INTO courses (prefix, no, title) VALUES
    ("MAT", 121, "Calculus 1"),
    ("CS", 220, "Intro to CS"),
    ("MAT", 122, "Calculus 2"),
    ("MAT", 221, "Calculus 3"),
    ("CS", 223, "Data Structures");

INSERT INTO enrollments (student_id, course_id)
SELECT id, 1 FROM students;

INSERT IGNORE INTO enrollments (student_id, course_id)
SELECT s.id, c.id
FROM students AS s, courses AS c
WHERE s.last = "Somebody"
AND c.prefix = "CS";

INSERT INTO enrollments (student_id, course_id)
SELECT s.id, c2.id
FROM students AS s, courses AS c2
WHERE c2.prefix = "CS"
AND c2.no = 220
AND NOT EXISTS (SELECT prefix
                FROM enrollments AS e, courses AS c
                WHERE e.course_id = c.id
                AND e.student_id = s.id
                AND c.prefix = "CS"
               );

DELETE FROM enrollments
WHERE student_id IN (SELECT id from students
                     WHERE first = "Joe")
AND course_id > 0;

UPDATE students AS s
SET s.credits = (SELECT COALESCE(SUM(c.credits), 0)
                 FROM courses AS c
                 JOIN enrollments AS e on e.course_id = c.id
                 WHERE e.student_id = s.id)
WHERE s.id > 0;

UPDATE students AS s
SET s.credits = (SELECT COALESCE(SUM(c.credits), 0)
                 FROM courses AS c
                 JOIN enrollments AS e on e.course_id = c.id
                 WHERE e.student_id = s.id
                 AND e.letter_grade IS NOT NULL)
WHERE s.id > 0;

# Add your answers here

