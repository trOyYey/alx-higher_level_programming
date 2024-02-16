-- lists average temps by city in descending order
SELECT city, AVG(value) as average_temps
FROM temperatures
GROUP BY city
ORDER BY average_temps DESC
