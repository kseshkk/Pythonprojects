-- INSERT INTO games (title, genre, price, rating, multiplayer)
-- VALUES
-- ('Minecraft', 'Sandbox', 2500, 9.0, true),
-- ('The Witcher 3', 'RPG', 1800, 9.5, false),
-- ('CS2', 'Shooter', 0, 8.3, true),
-- ('Stardew Valley', 'Simulator', 700, 8.8, true),
-- ('Portal 2', 'Puzzle', 500, 9.2, true)

-- SELECT * FROM games
-- SELECT title, genre, price FROM games
-- SELECT * FROM games WHERE price > 1000
-- SELECT * FROM games WHERE rating > 8.5
-- SELECT * FROM games WHERE price < 2000 AND rating > 8.0
-- SELECT * FROM games WHERE price = 0 OR multiplayer = true

-- SELECT * FROM games ORDER BY price DESC
-- SELECT * FROM games ORDER BY rating DESC

-- SELECT * FROM games
-- ORDER BY id
-- LIMIT 3

-- SELECT * FROM games
-- ORDER BY id
-- LIMIT 3
-- OFFSET 2

-- SELECT * FROM games WHERE id=1
-- SELECT COUNT(id) AS count_all_games FROM games
-- SELECT COUNT(id) AS count_all_games FROM games WHERE multiplayer = true

-- SELECT SUM(price) FROM games
-- SELECT AVG(price) FROM games
-- SELECT MAX(price) FROM games

-- SELECT * FROM games WHERE price = (SELECT MAX(price) FROM games)
-- SELECT ROUND(AVG(price), 1) FROM games
-- SELECT * FROM games WHERE rating = (SELECT MAX(rating) FROM games)

-- SELECT NOW()