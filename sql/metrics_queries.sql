SELECT product_id, COUNT(*) AS views
FROM user_actions
WHERE action = 'view'
GROUP BY product_id
ORDER BY views DESC
LIMIT 10;

SELECT product_id, COUNT(*) AS cart_adds
FROM user_actions
WHERE action = 'add_to_cart'
GROUP BY product_id
ORDER BY cart_adds DESC
LIMIT 10;

SELECT product_id, COUNT(*) AS purchases
FROM user_actions
WHERE action = 'purchase'
GROUP BY product_id
ORDER BY purchases DESC
LIMIT 10;