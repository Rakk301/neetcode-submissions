-- Write your query below


SELECT left_operand, operator, right_operand, CASE 
    WHEN operator = '=' AND l_value.value = r_value.value THEN 'true' 
    WHEN operator = '>' AND l_value.value > r_value.value THEN 'true' 
    WHEN operator = '<' AND l_value.value < r_value.value THEN 'true' 
    ELSE 'false'
    END AS value
FROM expressions as e
LEFT JOIN variables as l_value ON e.left_operand = l_value.name 
LEFT JOIN variables as r_value ON e.right_operand = r_value.name
