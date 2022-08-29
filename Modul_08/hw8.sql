CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title VARCHAR(30),
    education_year YEAR DEFAULT '2022' NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30));
   
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    subject VARCHAR(30),
    teacher_id INTEGER,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
     FOREIGN KEY (teacher_id) REFERENCES teachers (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE);

CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    mark INTEGER,
    lesson_date DATE,
    teacher_id INTEGER,
    student_id INTEGER,
    subject_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE,
    FOREIGN KEY (student_id) REFERENCES students (id)
          ON DELETE CASCADE
          ON UPDATE CASCADE);
         
INSERT INTO groups (title)
VALUES ('Python6'), ('FullStack7'), ('QA8'), ('UI/UX9');

INSERT INTO students (first_name, last_name, group_id)
VALUES ('Віра', 'Данильчук', 4),
('Ольга', 'Пилипенко', 2),
('Олесь', 'Непорожній', 4),
('Софія', 'Оробець', 4),
('Надія', 'Юхименко', 4),
('Герман ', 'Забарний', 3),
('Георгій', 'Корбут', 4),
('Вадим', 'Симоненко', 2),
('Єлисей', 'Гуцуляк', 4),
('Демид', 'Тимчук', 1),
('Пилип', 'Деркач', 1),
('Леон', 'Токар', 2),
('Станіслав', 'Яремків', 4),
('Лариса', 'Жук', 1),
('Володимира', 'Данчук', 2),
('Симон', 'Чумаченко', 4),
('Миколай', 'Василечко', 1),
('Артем', 'Данильчук', 1),
('Захар', 'Семенченко', 3),
('Захар', 'Яремко', 4),
('Емілія', 'Вертипорох', 3),
('Руслан', 'Ящук', 3),
('Веніямин', 'Шинкаренко', 1),
('Данна', 'Малишко', 2),
('Златослава', 'Бабак', 2),
('Лариса', 'Худобʼяк', 1),
('Еріка', 'Заїка', 2),
('Святослава', 'Негода', 4),
('Юстина', 'Лавренко', 4),
('Станіслав', 'Даньків', 2),
('Розалія', 'Рубець', 2),
('Августин', 'Байрак', 3),
('Іван', 'Затула', 2),
('Дмитро', 'Юхименко', 3),
('Ярема', 'Павличенко', 4),
('Веніямин', 'Скорик', 2),
('Костянтин', 'Деревʼянко', 1),
('Алла', 'Влох', 3),
('Пилип', 'Артим', 1),
('Роман', 'Ярош', 2),
('Амвросій', 'Фаренюк', 4),
('Євген', 'Данилюк', 1),
('Анастасія', 'Деркач', 3),
('Дарина', 'Рак', 4),
('Богодар', 'Наливайко', 3),
('Леон', 'Артимович', 4),
('Яків', 'Ірванець', 3),
('Венедикт', 'Вернигора', 1),
('Лесь', 'Гавришкевич', 3),
('Святослава', 'Ільченко', 3);

INSERT INTO teachers (first_name, last_name)
VALUES ('Ярема', 'Литвиненко'),
('Ліза', 'Давимука'),
('Адам', 'Авраменко'),
('Орест', 'Іщенко');

INSERT INTO subjects  (subject, teacher_id)
VALUES ('Python Data Science', 1),
       ('HTML/CSS/JS', 2),
       ('QA Auto/Manual', 3),
       ('Photoshop/Figma', 4);
       
INSERT INTO marks (mark, lesson_date, teacher_id,
student_id, subject_id)
VALUES (11, '2022-07-14', 3, 48, 3),
(11, '2022-04-18', 4, 26, 4),
(6, '2022-06-22', 2, 28, 2),
(12, '2022-01-24', 4, 12, 4);

--1
SELECT round(AVG(m.mark)) as Середній_бал, s.first_name Імя, s.last_name  Прізвище
FROM marks m
LEFT JOIN students s ON m.student_id = s.id
GROUP BY m.student_id
ORDER BY AVG(m.mark) DESC
LIMIT 5

--2 
SELECT sub.subject as Предмет, round(avg(m.mark)) as 'Середній бал', s.first_name Імя, s.last_name  Прізвище
FROM marks m
JOIN students s ON m.student_id = s.id
JOIN subjects sub ON m.subject_id = sub.id 
GROUP BY m.subject_id 
ORDER BY sub.id 

--3
SELECT CEIL(avg(m.mark)) as 'Середній бал', s.subject 'Предмет' 
FROM marks m, groups g 
JOIN subjects s ON m. 
GROUP BY g.id 

--4
SELECT FLOOR(AVG(m.mark)) as 'Середній бал в потоці'
FROM marks m 

--5
select t.first_name, t.last_name, s.subject 
from teachers t 
Join subjects s On s.teacher_id = t.id 

--6
SELECT s.id as ID, s.first_name as Імя, s.last_name as Прізвище, g.title as 'Назва групи'
FROM students s 
JOIN groups g ON g.id = s.group_id 
WHERE  g.title = 'Перша'

--7
SELECT s.first_name as Імя, s.last_name as Прізвище, m.mark as Оцінки, g.title as Група, sub.subject as Предмет
FROM students s
JOIN marks m ON m.student_id = s.id 
JOIN groups g ON s.group_id = g.id 
JOIN subjects sub ON m.subject_id  = sub.id 
WHERE s.group_id = 2 and m.subject_id = 1
ORDER BY m.mark DESC;

--8
SELECT max(m.lesson_date) as 'Дата заннятя', s.first_name as Імя, s.last_name as Прізвище, g.title as Група, sub.subject as Предмет
FROM marks m
LEFT JOIN students as s ON s.id = m.student_id
LEFT JOIN groups g ON g.id = s.group_id 
LEFT JOIN subjects sub ON sub.id = m.subject_id 
WHERE m.subject_id = 2 and g.id = 3;

--9
SELECT DISTINCT s.id as ID, s.first_name as Імя, s.last_name as Прізвище,  sub.subject as Предмет
FROM students s 
JOIN marks m ON m.student_id  = s.id 
JOIN subjects sub ON sub.id = m.subject_id 
WHERE s.id = 8;

--10
SELECT DISTINCT s.id as ID, s.first_name as Імя, s.last_name as Прізвище,  sub.subject as Предмет, t.last_name as 'Прізвище викладачa'
FROM students s 
JOIN marks m ON m.student_id  = s.id 
JOIN subjects sub ON sub.id = m.subject_id 
JOIN teachers t ON m.teacher_id = t.id 
WHERE s.id = 18 and t.id = 2;

--11
SELECT round(avg(m.mark)) as 'Середній бал' ,s.first_name 'Імя студента', s.last_name 'Прізвище студента' 
FROM students s 
JOIN marks m ON m.student_id = s.id 
JOIN teachers t ON t.id = m.teacher_id
WHERE s.id = 22;

--12
SELECT ROUND(AVG(m.mark))  as 'Середній бал' , t.first_name 'Імя викладача', t.last_name 'Прізвище викладача'
FROM teachers t
JOIN marks m  ON teacher_id = m.teacher_id 
WHERE  t.id = 2;



