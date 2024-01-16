-- Script that lists the number of records with the same score
-- The result will desplay the score and the number of occurances
-- of the score

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
