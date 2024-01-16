-- Script that lists all the records from the second_table
-- The scores should be >= 10
-- Ordered them in a descending order

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
