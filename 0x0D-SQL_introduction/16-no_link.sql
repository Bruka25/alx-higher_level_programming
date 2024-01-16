-- Script that lists all the records of the table second_table
-- List without the name value will not be displayed
-- Order the scores in descending order
 
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
