""" Create tables

1. Create Groups table
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title VARCHAR(30),
    education_year DATE DEFAULT CURRENT_DATE NOT NULL
);


2. Create students table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

3. Create teachers table
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30));

4. Create subjects table
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    subject VARCHAR(30),
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

5. Create marks table
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    mark VARCHAR(30),
    lesson_date DATE,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    subject_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

"""

