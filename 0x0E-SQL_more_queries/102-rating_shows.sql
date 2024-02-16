-- lists shows by their totall rattings
SELECT title, SUM(rate) AS R
FROM tv_shows
	INNER JOIN tv_show_ratings
	ON id = show_id
GROUP BY title
ORDER BY R DESC;
