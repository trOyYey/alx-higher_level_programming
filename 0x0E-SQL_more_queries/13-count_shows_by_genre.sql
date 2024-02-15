-- lists genres from hbtn_0d_tvshows
SELECT gnr.name AS genre, COUNT(seriesgnr.show_id) AS number_of_shows
FROM tv_genres AS gnr
	INNER JOIN tv_show_genres AS seriesgnr
	on gnr.id = seriesgnr.genre_id 
GROUP BY gnr.name 
ORDER BY number_of_shows DESC;
