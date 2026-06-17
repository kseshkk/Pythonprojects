-- 1 Вывести всех учеников вместе с названием их группы.
SELECT first_name, last_name, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 

-- 2 Вывести имя ученика, фамилию, возраст, среднюю оценку и название группы.
SELECT first_name, last_name, age, average_score, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 

-- 3 Найти всех учеников из группы Python-1 .
SELECT first_name, last_name, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
WHERE name = 'Python-1'

-- 4 Найти всех учеников, которые учатся на курсе Python
SELECT first_name, last_name, course_name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
WHERE course_name = 'Python'

-- 5 Найти всех учеников из групп, которые стартовали в 2025 году.
SELECT first_name, last_name, start_year FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
WHERE start_year = 2025

-- 6 Найти всех учеников старше 14 лет и вывести название их группы.
SELECT first_name, last_name, age, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
WHERE age > 14

-- 7 Найти учеников, у которых средняя оценка выше 4.5 , и вывести курс, на
-- котором они учатся.
SELECT first_name, last_name, average_score, course_name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
WHERE average_score > 4.5

-- 8 Отсортировать учеников по названию группы.
SELECT first_name, last_name, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
ORDER BY name

-- 9 Отсортировать учеников по средней оценке внутри каждой группы.
SELECT first_name, last_name, average_score FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
ORDER BY average_score

-- 10 Посчитать количество учеников в каждой группе.
SELECT name, COUNT(s.id) AS count_students FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
GROUP BY g.id

-- 11 Найти группы, в которых больше 3 учеников.
SELECT name, COUNT(s.id) AS count_students FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
GROUP BY g.id
HAVING COUNT(s.id) > 3

-- 12 Найти средний возраст учеников в каждой группе.
SELECT ROUND(AVG(age), 1) AS average_age, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
GROUP BY g.id

-- 13 Найти среднюю оценку учеников в каждой группе.
SELECT AVG(average_score) AS average_score, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
GROUP BY g.id

-- 14 Найти группу с самой высокой средней оценкой учеников.
SELECT AVG(average_score) AS avg_score, name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id 
GROUP BY g.id
ORDER BY avg_score DESC
LIMIT 1

-- 15 Найти группы, в которых нет учеников.
SELECT name FROM groups AS g
LEFT JOIN students AS s ON g.id = s.group_id
WHERE s.id IS NULL

-- 16 Вывести все группы, даже если в них пока нет учеников
SELECT name FROM groups AS g
LEFT JOIN students AS s 
ON g.id = s.group_id
GROUP BY g.id

-- 17 Вывести только те группы, в которых есть хотя бы один ученик
SELECT name FROM students AS s
JOIN groups AS g 
ON g.id = s.group_id
GROUP BY g.id

