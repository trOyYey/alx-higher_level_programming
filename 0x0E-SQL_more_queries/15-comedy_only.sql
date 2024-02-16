-- lists comedy shows from database
SELECT show.title 
FROM television_genres AS genre 
	INNER JOIN television_show_genres AS show_genre 
	ON genre.id = show_genre.genre_id 
	INNER JOIN television_shows AS show 
	ON show_genre.show_id = show.id 
WHERE genre.name = 'Comedy' 
ORDER BY show.title ASC;
