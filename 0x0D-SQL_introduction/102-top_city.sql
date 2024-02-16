--lists the top 3 temps dwuring august and july in descending order
SELECT city, AVG(value) as av_temps
FROM temperatures
where month = 8 OR month = 7
GROUP BY city
ORDER BY av_temps DESC
LIMIT 3
