Lab Assignment 3: Working with MySQL
====================================

In this assignment we will continue the work on MySQL data that we carried on in class. Your data at this point should be the result after we execute all the commands in the mysql section of the notes, that we just went over together in class. You should download [this SQL script from GitHub](https://github.com/skiadas/DataWranglingCourse/blob/gh-pages/assignments/assignment3.sql) and open the script file from mysqlworkbench. It contains instructions that would delete the tables we created and recreate them. When you want to "reset" the database, just execute that script. You will add your answers at the bottom of that file.

Make sure to do these assignments in order.

1. Write the SQL command to create a new table, called `grades`. It will have two attributes: One will be called "letter", and it should be a fixed 2-byte character string (big enough to hold things like A+). The other should be called "point" and it should be a double-precision number. The letter attribute should be marked as a primary key, and the gpa attribute should be marked as unique.
2. Now populate this table using an INSERT, to put in it the correspondence between letter grades and gpas outlined in the college catalog (for instance A would be paired with 4.0). You can get an online copy of the catalog at my.hanover.edu. You only need to include grades up to F.
3. Use ALTER TABLE to change the enrollments table so that it has a FOREIGN KEY on the `letter_grade` attribute, pointing to the `letter` attribute of the `grades` table. Do the same for the `point_grade` attribute, it should point to the `point` attribute of the `grades` table.
4. Write UPDATE statements that add grades to students enrolled in courses as follows:
    - Assign A to everyone with last name "Somebody" in all their classes.
    - Assign C to everyone with last name "Doe" in all their CS classes.
    - Assign B to every student on every course that they are enrolled in and that they don't have a grade yet.
    - In each case you should be assigning both letter grades and point grades.
5. Write a SELECT query that for each student prints out the student's id along with the number of credits they have.
6. Write a SELECT query that prints out on each row the student's id along with their cumulative gpa. To compute that gpa you would need to do the following: You can do a join of the students, enrollments and courses, then have a GROUP BY clause for student id, then compute the sum of "points times credits" and divide by the sum of credits. Something like `SUM(point_grade*credits) / SUM(credits)` would do that part. Name the column "gpa".
7. Write a query to return the ids of students who are not enrolled in any CS courses.
8. Write an UPDATE query that would correctly set the gpa and number of credits earned values in the students table.
9. Write an INSERT that would find any student that got at least a B (use the point grade instead) in CS220, and enroll them in CS223.

You should submit your completed SQL script as an email attachment to me. The name of the file should include your first and last name, in addition to the assignment's number. It should contain no whitespaces.
