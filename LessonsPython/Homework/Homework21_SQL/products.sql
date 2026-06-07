-- INSERT INTO products (name, category, price, quantity, discount_percent)
-- VALUES
-- ('Ноутбук Lenovo', 'Ноутбуки', 55000, 4, 10),
-- ('Мышка Logitech', 'Аксессуары', 2500, 15, 0),
-- ('Клавиатура HyperX', 'Аксессуары', 7000, 8, 5),
-- ('Монитор Samsung', 'Мониторы', 18000, 3, 15),
-- ('Наушники Sony', 'Аудио', 12000, 6, 0)

-- SELECT * FROM products
-- SELECT name, category, price FROM products
-- SELECT * FROM products WHERE price > 10000
-- SELECT * FROM products WHERE quantity > 5
-- SELECT * FROM products WHERE price > 5000 AND discount_percent > 0
-- SELECT * FROM products WHERE category='Аксессуары' OR price < 3000
-- SELECT * FROM products ORDER BY price DESC

-- SELECT * FROM products
-- ORDER BY id
-- LIMIT 3

-- SELECT * FROM products
-- ORDER BY id
-- LIMIT 3
-- OFFSET 2

-- SELECT * FROM products WHERE id=1
-- SELECT COUNT(id) AS count_all_products FROM products
-- SELECT COUNT(id) AS count_all_products_with_discount FROM products WHERE discount_percent>0

-- SELECT SUM(price) FROM products
-- SELECT AVG(price) FROM products
-- SELECT MAX(price) FROM products

-- SELECT * FROM products WHERE price = (SELECT MAX(price) FROM products)
-- SELECT ROUND(AVG(price), 1) FROM products
-- SELECT * FROM products WHERE quantity = (SELECT MAX(quantity) FROM products)

-- SELECT NOW()