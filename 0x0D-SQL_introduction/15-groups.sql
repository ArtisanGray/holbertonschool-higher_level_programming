-- lists records with equal values.
SELECT score, COUNT(*) number
FROM second_table
GROUP BY score
ORDER BY number DESC;
