-- Write your query below
SELECT o.customer_id, c.customer_name
FROM orders as o 
LEFT JOIN customers as c ON o.customer_id = c.customer_id
WHERE o.customer_id IN (SELECT DISTINCT customer_id FROM orders WHERE product_name = 'A')
    AND o.customer_id IN (SELECT DISTINCT customer_id FROM orders WHERE product_name = 'B')
    AND o.customer_id NOT IN (SELECT DISTINCT customer_id FROM orders WHERE product_name = 'C')
GROUP BY o.customer_id, c.customer_name
ORDER by c.customer_name;