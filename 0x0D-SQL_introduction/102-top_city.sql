-- displays the average temperature by city ordered by temp
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month in (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
