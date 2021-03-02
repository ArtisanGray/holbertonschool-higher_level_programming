-- lists all records of a table, if not empty.
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
