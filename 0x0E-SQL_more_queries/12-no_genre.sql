-- list shows with no genre
SELECT series.title, gnr.genre_id 
FROM tv_shows AS series 
	LEFT JOIN tv_show_genres AS gnr
	ON series.id = gnr.show_id
WHERE gnr.show_id IS NULL
ORDER BY series.title ASC, gnr.genre_id ASC;
