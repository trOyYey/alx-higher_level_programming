-- lists all non empty records in descending score order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
