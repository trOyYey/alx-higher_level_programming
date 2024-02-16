-- lists same genre shows as in Dexter
SELECT gnr.name FROM tv_genres AS gnr
	INNER JOIN tv_show_genres AS show_gnr
	ON gnr.id = show_gnr.genre_id
		INNER JOIN tv_shows AS tv_s
		ON show_gnr.show_id = tv_s.id
WHERE tv_s.title = 'Dexter'
ORDER BY gnr.name ASC;
