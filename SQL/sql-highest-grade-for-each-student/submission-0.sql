-- Write your query below
WITH scores AS (
    SELECT *, RANK() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as sc_rnk 
    FROM exam_results
)
SELECT student_id, exam_id, score
FROM scores 
WHERE sc_rnk = 1
ORDER BY student_id ASC