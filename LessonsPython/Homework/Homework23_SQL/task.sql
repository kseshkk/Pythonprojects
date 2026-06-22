-- Задания на SELECT
SELECT * FROM players
SELECT * FROM teams
SELECT * FROM tournaments
SELECT * FROM tournament_players
SELECT nickname, age, rating FROM players
SELECT title, game_name, prize_pool, status FROM tournaments

-- Задания на WHERE, AND, OR
SELECT * FROM players WHERE age > 15
SELECT * FROM players WHERE age < 16
SELECT * FROM players WHERE rating > 4.5
SELECT * FROM players WHERE coins > 1000
SELECT * FROM players WHERE rating > 4.5 AND coins > 1000
SELECT * FROM players WHERE age = 14 OR rating < 4.0
SELECT * FROM tournaments WHERE status = 'finished'
SELECT * FROM tournaments WHERE status = 'planned'
SELECT * FROM tournaments WHERE prize_pool > 40000
SELECT * FROM tournaments WHERE status = 'finished' AND prize_pool > 30000

-- Задания на ORDER BY и LIMIT
SELECT * FROM players ORDER BY rating DESC
SELECT * FROM players ORDER BY coins
SELECT * FROM tournaments ORDER BY prize_pool DESC
SELECT * FROM tournaments ORDER BY start_date
SELECT * FROM players ORDER BY rating DESC LIMIT 3
SELECT * FROM players ORDER BY coins DESC LIMIT 3
SELECT * FROM tournaments ORDER BY prize_pool DESC LIMIT 2
SELECT * FROM tournaments
WHERE status = 'planned'
ORDER BY start_date 
LIMIT 1

-- Задания на LIKE
SELECT * FROM players WHERE nickname LIKE '%sql%'
SELECT * FROM players WHERE nickname LIKE '%dev%'
SELECT * FROM players WHERE nickname LIKE '%py%'
SELECT * FROM players WHERE nickname LIKE 'm%'
SELECT * FROM tournaments WHERE title LIKE '%SQL%'
SELECT * FROM tournaments WHERE title LIKE '%Cup%'
SELECT * FROM tournaments WHERE game_name LIKE '%Python%'

-- Задания на BETWEEN
SELECT * FROM players WHERE age BETWEEN 15 AND 16
SELECT * FROM players WHERE rating BETWEEN 4.0 AND 4.7
SELECT * FROM players WHERE coins BETWEEN 500 AND 1200
SELECT * FROM tournaments WHERE prize_pool BETWEEN 30000 AND 70000
SELECT * FROM tournaments WHERE start_date BETWEEN '2026-04-01' AND '2026-07-31'

-- Задания на IN
SELECT * FROM players WHERE team_id IN (1, 2, 4)
SELECT * FROM tournaments WHERE status IN ('finished', 'active')
SELECT * FROM tournaments WHERE game_name IN ('SQL Arena', 'Python Quest')
SELECT * FROM teams WHERE city IN ('Брянск', 'Москва', 'Курск')

-- Задания на DISTINCT
SELECT DISTINCT city FROM teams
SELECT DISTINCT status FROM tournaments
SELECT DISTINCT game_name FROM tournaments
SELECT DISTINCT age FROM players
SELECT COUNT(DISTINCT city) FROM teams
SELECT COUNT(DISTINCT game_name) FROM tournaments

-- Задания на AS
SELECT nickname AS "Никнейм", rating AS "Рейтинг" FROM players
SELECT name AS "Команда", city AS "Город" FROM teams
SELECT title AS "Турнир", prize_pool AS "Призовой фонд" FROM tournaments
SELECT game_name AS "Игра", status AS "Статус" FROM tournaments
SELECT p.nickname AS "Никнейм игрока", t.name    AS "Команда", p.rating  AS "Рейтинг игрока"
FROM players AS p
LEFT JOIN teams AS t 
ON p.team_id = t.id

-- Задания на UPDATE
UPDATE players SET coins = coins + 300 WHERE nickname = 'kirill_dev'
UPDATE players SET rating = rating + 0.4 WHERE nickname = 'max_bug'
UPDATE tournaments SET status = 'finished' WHERE title = 'Bug Hunter Night'
UPDATE tournaments SET prize_pool = prize_pool + 10000 WHERE status = 'planned'
UPDATE players SET team_id = (SELECT id FROM teams WHERE name = 'Null Pointers') WHERE nickname = 'oleg_null'
UPDATE players SET rating = rating + 0.2 WHERE rating < 4.0

SELECT * FROM tournament_players
TRUNCATE TABLE tournament_players
SELECT * FROM tournament_players

-- Задания на INNER JOIN
-- 1. Вывести игроков вместе с названиями их команд.
-- 2. Вывести только тех игроков, у которых есть команда.
SELECT p.*, t.name
FROM players AS p
JOIN teams AS t ON p.team_id = t.id

-- 3. Вывести название турнира, никнейм игрока, очки и место.
SELECT t.title, p.nickname, tp.points, tp.final_place
FROM tournament_players AS tp
JOIN tournaments AS t 
ON tp.tournament_id = t.id
JOIN players AS p 
ON tp.player_id = p.id 

-- 4. Вывести всех участников турнира Spring SQL Cup.
SELECT p.*
FROM tournament_players AS tp
JOIN tournaments AS t 
ON tp.tournament_id = t.id
JOIN players AS p 
ON tp.player_id = p.id 
WHERE t.title = 'Spring SQL Cup'

-- 5. Вывести всех игроков, которые участвовали в турнирах по игре SQL Arena.
SELECT p.*
FROM tournament_players AS tp
JOIN tournaments AS t 
ON tp.tournament_id = t.id
JOIN players AS p 
ON tp.player_id = p.id 
WHERE t.game_name = 'SQL Arena'

-- 6. Вывести всех игроков, которые участвовали в турнирах с призовым фондом больше 40000.
SELECT p.*
FROM tournament_players AS tp
JOIN tournaments AS t 
ON tp.tournament_id = t.id
JOIN players AS p 
ON tp.player_id = p.id 
WHERE t.prize_pool > 40000

-- 7. Вывести никнейм игрока, название команды, название турнира и очки.
SELECT p.nickname, tm.name, t.title, tp.points
FROM tournament_players AS tp
JOIN tournaments AS t 
ON tp.tournament_id = t.id
JOIN players AS p 
ON tp.player_id = p.id 
JOIN teams AS tm 
ON p.team_id = tm.id

-- 8. Вывести игроков, команды и турниры, где игрок набрал больше 800 очков.
SELECT p.*, tm.*, t.*
FROM tournament_players AS tp
JOIN tournaments AS t 
ON tp.tournament_id = t.id
JOIN players AS p 
ON tp.player_id = p.id 
JOIN teams AS tm 
ON p.team_id = tm.id
WHERE tp.points > 800

-- Задания на LEFT JOIN
-- 1. Вывести все команды и игроков в них.
SELECT t.*, p.*
FROM teams AS t
LEFT JOIN players AS p
ON t.id = p.team_id

-- 2. Найти команды, в которых нет игроков.
SELECT t.*
FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
WHERE p.id IS NULL

-- 3. Вывести всех игроков и их команды, включая игроков без команды.
SELECT t.*, p.*
FROM players AS p
LEFT JOIN teams AS t
ON t.id = p.team_id

-- 4. Найти игроков, которые не состоят ни в одной команде.
SELECT p.*
FROM players AS p
LEFT JOIN teams AS t 
ON t.id = p.team_id
WHERE t.id IS NULL

-- 5. Вывести все турниры и участников в них.
SELECT t.*, p.*
FROM tournaments AS t
LEFT JOIN tournament_players AS tp
ON t.id = tp.tournament_id
LEFT JOIN players AS p
ON tp.player_id = p.id

-- 6. Найти турниры, в которых пока нет участников.
SELECT t.*
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
WHERE tp.tournament_id IS NULL

-- 7. Вывести всех игроков и турниры, в которых они участвовали.
SELECT p.*, t.*
FROM players AS p
LEFT JOIN tournament_players AS tp 
ON p.id = tp.player_id
LEFT JOIN tournaments AS t 
ON tp.tournament_id = t.id

-- 8. Найти игроков, которые не участвовали ни в одном турнире.
SELECT p.*
FROM players AS p
LEFT JOIN tournament_players AS tp 
ON p.id = tp.player_id
WHERE tp.player_id IS NULL

-- 9. Вывести все команды и количество игроков в каждой, включая пустые команды.
SELECT t.*, COUNT(p.id) AS count_players
FROM teams AS t
LEFT JOIN players AS p
ON t.id = p.team_id
GROUP BY t.id, t.name, t.city, t.rating

-- 10. Вывести все турниры и количество участников, включая турниры без участников.
SELECT t.*, COUNT(p.id) AS count_players
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
LEFT JOIN players AS p
ON tp.player_id = p.id
GROUP BY t.id, t.title, t.game_name, t.prize_pool, t.status, t.start_date

-- Задания на RIGHT JOIN
-- 1. Вывести команды и игроков через RIGHT JOIN .
SELECT t.*, p.*
FROM players AS p
RIGHT JOIN teams AS t
ON t.id = p.team_id

-- 2. Вывести турниры и участников через RIGHT JOIN .
SELECT t.*, p.*
FROM tournament_players AS tp
RIGHT JOIN tournaments AS t 
ON tp.tournament_id = t.id
RIGHT JOIN players AS p 
ON tp.player_id = p.id

-- 3. Один запрос с RIGHT JOIN переписать через LEFT JOIN
SELECT t.*, p.*
FROM teams AS t
LEFT JOIN players AS p
ON t.id = p.team_id

-- Задания на COUNT
SELECT COUNT(p.id) AS players_count FROM players AS p
SELECT COUNT(t.id) AS teams_count FROM teams AS t
SELECT COUNT(t.id) AS tournaments_count FROM tournaments AS t
SELECT COUNT(tp.*) AS tournament_players_count FROM tournament_players AS tp

-- 5. Посчитать количество игроков в каждой команде.
SELECT t.name, COUNT(p.id) AS players_count
FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
GROUP BY t.id

-- 6. Посчитать количество участников в каждом турнире.
SELECT t.title, COUNT(tp.player_id) players_count
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id

-- 7. Посчитать количество турниров по каждому статусу.
SELECT status, COUNT(t.*) AS count_tournaments
FROM tournaments AS t
GROUP BY status

-- 8. Посчитать количество турниров по каждой игре.
SELECT game_name, COUNT(t.*) AS count_tournaments
FROM tournaments AS t
GROUP BY game_name

-- Задания на AVG, MIN, MAX, SUM, ROUND
SELECT AVG(rating) FROM players
SELECT AVG(age) FROM players
SELECT MIN(rating) FROM players
SELECT MAX(rating) FROM players
SELECT SUM(coins) FROM players
SELECT MAX(prize_pool) FROM tournaments
SELECT MIN(prize_pool) FROM tournaments
SELECT SUM(prize_pool) FROM tournaments
SELECT AVG(points) FROM tournament_players
SELECT ROUND(AVG(rating), 2) FROM players
SELECT ROUND(AVG(age), 1) FROM players
SELECT ROUND(AVG(points), 2) FROM tournament_players

-- Задания на GROUP BY
-- 1. Посчитать количество игроков в каждой команде
SELECT t.name, COUNT(p.id) FROM teams AS t
LEFT JOIN players AS p
ON t.id = p.team_id
GROUP BY t.id, t.name

-- 2. Посчитать средний рейтинг игроков в каждой команде.
SELECT t.name, AVG(p.rating) FROM teams AS t
LEFT JOIN players AS p
ON t.id = p.team_id
GROUP BY t.id, t.name

-- 3. Посчитать сумму монет игроков в каждой команде
SELECT t.name, SUM(p.coins) FROM teams AS t
LEFT JOIN players AS p
ON t.id = p.team_id
GROUP BY t.id, t.name

-- 4. Посчитать количество участников в каждом турнире.
SELECT t.title, COUNT(tp.player_id)
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title

-- 5. Посчитать среднее количество очков в каждом турнире.
SELECT t.title, AVG(tp.points)
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title

-- 6. Найти максимальный результат в каждом турнире.
SELECT t.title, MAX(tp.points)
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title

-- 7. Найти минимальный результат в каждом турнире
SELECT t.title, MIN(tp.points)
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title

-- 8. Посчитать количество турниров по каждому статусу.
SELECT t.status, COUNT(t.status)
FROM tournaments AS t
GROUP BY t.status

-- 9. Посчитать общий призовой фонд турниров по каждой игре.
SELECT game_name, SUM(prize_pool)
FROM tournaments
GROUP BY game_name

-- 10. Посчитать средний призовой фонд турниров по каждому статусу.
SELECT status, AVG(prize_pool)
FROM tournaments
GROUP BY status

-- Задания на HAVING
-- 1. Вывести команды, где больше одного игрока.
SELECT t.*
FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
GROUP BY t.id
HAVING COUNT(p.id) > 1

-- 2. Вывести команды, где средний рейтинг игроков больше 4.5.
SELECT t.*
FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
GROUP BY t.id
HAVING AVG(p.rating) > 4.5

-- 3. Вывести команды, где суммарно больше 2000 монет.
SELECT t.*
FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
GROUP BY t.id
HAVING SUM(p.coins) > 2000

-- 4. Вывести турниры, где больше 3 участников
SELECT t.*
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title, t.game_name, t.prize_pool, t.status, t.start_date
HAVING COUNT(tp.player_id) > 3

-- 5. Вывести турниры, где среднее количество очков больше 700.
SELECT t.*
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title, t.game_name, t.prize_pool, t.status, t.start_date
HAVING AVG(tp.points) > 700

-- 6. Вывести игры, по которым суммарный призовой фонд больше 50000.
SELECT game_name, SUM(prize_pool)
FROM tournaments
GROUP BY game_name
HAVING SUM(prize_pool) > 50000

-- 7. Вывести статусы турниров, где количество турниров больше одного.
SELECT status, COUNT(*) 
FROM tournaments
GROUP BY status
HAVING COUNT(*) > 1

-- 8. Вывести турниры, где максимальный результат больше 900.
SELECT t.*
FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title, t.game_name, t.prize_pool, t.status, t.start_date
HAVING MAX(tp.points) > 900

-- Задания на подзапросы
-- 1. Найти игроков, чей рейтинг выше среднего рейтинга всех игроков.
SELECT * FROM players WHERE rating > (SELECT AVG(rating) FROM players)

-- 2. Найти игроков, у которых монет больше среднего количества монет.
SELECT * FROM players WHERE coins > (SELECT AVG(coins) FROM players)

-- 3. Найти турниры, у которых призовой фонд выше среднего призового фонда всех турниров
SELECT * FROM tournaments WHERE prize_pool > (SELECT AVG(prize_pool) FROM tournaments)

-- 4. Найти игроков, которые состоят в командах из городов Брянск или Москва.
SELECT p.* FROM players AS p
WHERE p.team_id IN (SELECT id FROM teams WHERE city IN ('Брянск', 'Москва'))

-- 5. Найти игроков, которые участвовали в турнирах по игре SQL Arena .
SELECT p.* FROM players AS p
WHERE p.id IN 
(SELECT tp.player_id 
FROM tournament_players AS tp 
JOIN tournaments AS t 
ON tp.tournament_id = t.id
WHERE t.game_name = 'SQL Arena')

-- 6. Найти игроков, которые участвовали хотя бы в одном завершённом турнире.
SELECT p.* FROM players AS p
WHERE p.id IN 
(SELECT tp.player_id 
FROM tournament_players AS tp 
JOIN tournaments AS t 
ON tp.tournament_id = t.id
WHERE t.status = 'finished')

-- 7. Найти команды, в которых есть хотя бы один игрок с рейтингом выше 4.5.
SELECT t.* FROM teams AS t 
WHERE t.id IN (SELECT team_id FROM players WHERE rating > 4.5)

-- 8. Найти турниры, в которых участвовал игрок kirill_dev
SELECT * FROM tournaments
WHERE id IN (SELECT tournament_id 
FROM tournament_players 
WHERE player_id = 
(SELECT id FROM players WHERE nickname = 'kirill_dev'))

-- Итоговый отчёт
-- 1. Топ-5 игроков по рейтингу.
SELECT * FROM players ORDER BY rating DESC LIMIT 5

-- 2. Топ-3 игроков по количеству монет.
SELECT * FROM players ORDER BY coins DESC LIMIT 3

-- 3. Все команды и количество игроков в каждой.
SELECT t.*, COUNT(p.id) FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
GROUP BY t.id

-- 4. Команды без игроков.
SELECT t.* FROM teams AS t
LEFT JOIN players AS p 
ON t.id = p.team_id
WHERE p.id IS NULL

-- 5. Игроки без команды.
SELECT p.* FROM players AS p
LEFT JOIN teams AS t
ON t.id = p.team_id
WHERE t.id IS NULL

-- 6. Все турниры и количество участников в каждом.
SELECT t.*, COUNT(tp.player_id) FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id

-- 7. Турниры без участников.
SELECT t.* FROM tournaments AS t
LEFT JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
WHERE tp.tournament_id IS NULL

-- 8. Игроки, которые не участвовали ни в одном турнире.
SELECT p.* FROM players AS p
LEFT JOIN tournament_players AS tp 
ON p.id = tp.player_id
WHERE tp.player_id IS NULL

-- 9. Игроки, участвовавшие в турнирах по SQL Arena .
SELECT p.* FROM players AS p
JOIN tournament_players AS tp 
ON p.id = tp.player_id
JOIN tournaments AS tr 
ON tp.tournament_id = tr.id
WHERE tr.game_name = 'SQL Arena'

-- 10. Игроки, участвовавшие в турнирах с призовым фондом больше 40000.
SELECT p.* FROM players AS p
JOIN tournament_players AS tp 
ON p.id = tp.player_id
JOIN tournaments AS tr 
ON tp.tournament_id = tr.id
WHERE tr.prize_pool > 40000

-- Задание со звёздочкой
SELECT t.title AS "название турнира", 
t.game_name AS "название игры", 
t.status AS "статус турнира", 
t.prize_pool AS "призовой фонд",
COUNT(tp.player_id) AS "количество участников", 
ROUND(AVG(tp.points), 2) AS "среднее количество очков", 
MAX(tp.points) AS "Максимальное количество очков",
MIN(tp.points) AS "Минимальное количество очков"
FROM tournaments AS t
JOIN tournament_players AS tp 
ON t.id = tp.tournament_id
GROUP BY t.id, t.title, t.game_name, t.status, t.prize_pool
HAVING COUNT(tp.player_id) > 2
ORDER BY AVG(tp.points) DESC