"""
Insert data in DB

"""
from faker import Factory
from random import randint
from datetime import date, datetime

fake = Factory.create('uk_UA')

"""
1. Add Groups Data
INSERT
INTO
groups(title)
VALUES('Python6'), ('FullStack7'), ('QA8'), ('UI/UX9');


2. Add students Data
Use func get_students(50) - we create 50 unique students

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


3. Add teachers Data
Use func get_teachers(4) - we create 4 unique teachers

INSERT INTO teachers (first_name, last_name)
VALUES ('Ярема', 'Литвиненко'),
('Ліза', 'Давимука'),
('Адам', 'Авраменко'),
('Орест', 'Іщенко');

4. Add subjects Data
INSERT INTO subjects  (subject, teacher_id)
VALUES ('Python Data Science', 1),
       ('HTML/CSS/JS', 2),
       ('QA Auto/Manual', 3),
       ('Photoshop/Figma', 4);
       
5. Add mark Data
Use func get_mark(200)
INSERT INTO marks (mark, lesson_date, teacher_id,
student_id, subject_id)
VALUES (11, '2022-07-14', 3, 48, 3),
(11, '2022-04-18', 4, 26, 4),
(6, '2022-06-22', 2, 28, 2),
(12, '2022-01-24', 4, 12, 4);

"""


def get_students(count):
    for i in range(count):
        name = fake.first_name()
        last_name = fake.last_name()
        group_id = randint(1, 4)
        print(f'(\'{name}\', \'{last_name}\', {group_id}),')


def get_teachers(count):
    for i in range(count):
        name = fake.first_name()
        last_name = fake.last_name()
        print(f'(\'{name}\', \'{last_name}\'),')


def get_mark(count):
    for i in range(count):
        mark = randint(6, 12)
        rand_month = str(randint(1, 8))
        rand_day = str(randint(10, 27))
        rand_str = '2022' + '-0' + rand_month + '-' + rand_day
        rand_date = datetime.strptime(rand_str, '%Y-%m-%d').date()
        teach_subj_id = randint(1, 4)
        stud_id = randint(1, 50)

        print(f'({mark}, \'{rand_date}\', {teach_subj_id}, {stud_id}, {teach_subj_id}),')


if __name__ == '__main__':
    get_students(50)
    get_teachers(4)
    get_mark(200)
