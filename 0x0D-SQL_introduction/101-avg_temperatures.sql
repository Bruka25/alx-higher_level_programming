-- Script that displays the average temperature
-- Group the result into city column
-- Order the avg_temp in descending order

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
