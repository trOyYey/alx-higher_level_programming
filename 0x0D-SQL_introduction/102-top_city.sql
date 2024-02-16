--lists the top 3 temps dwuring august and july in descending order
SELECT city, AVG(value) as avg_temp
FROM temperatures
where month = 8 OR month = 7
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3
