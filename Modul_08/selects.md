# Select Data 

**1) 5 студентів із найбільшим середнім балом з усіх предметів**
```
SELECT round(AVG(m.mark)) as Середній_бал, s.first_name Імя, s.last_name  Прізвище
FROM marks m
LEFT JOIN students s ON m.student_id = s.id
GROUP BY m.student_id
ORDER BY AVG(m.mark) DESC
LIMIT 5
```
![result 01](img/01.png)

**2) студент із найвищим середнім балом з одного предмета**
```
SELECT sub.subject as Предмет, round(avg(m.mark)) as 'Середній бал', s.first_name Імя, s.last_name  Прізвище
FROM marks m
JOIN students s ON m.student_id = s.id
JOIN subjects sub ON m.subject_id = sub.id 
GROUP BY m.subject_id 
ORDER BY sub.id 
```
![result 01](img/02.png)

**3) середній бал в групі по одному предмету**

**4) Середній бал у потоці**

**5) Які курси читає викладач**
```
select t.first_name, t.last_name, s.subject
from teachers t
Join subjects s On s.teacher_id = t.id
``` 

![result 05](img/05.png)


**6) Список студентів у групі**

**7) Оцінки студентів у групі з предмета**

**8) Оцінки студентів у групі з предмета на останньому занятті**

**9) Список курсів, які відвідує студент**

**10) Список курсів, які студенту читає викладач**

**11) Середній бал, який викладач ставить студенту**

**12) Середній бал, який ставить викладач**