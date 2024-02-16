-- lists all shows and all genres linked to specified show
SELECT show.title, genre.name
FROM television_shows AS show
	LEFT JOIN television_show_genres AS show_genre
	ON show.id = show_genre.show_id
		LEFT JOIN television_genres AS genre
		ON show_genre.genre_id = genre.id
ORDER BY show.title ASC, genre.name ASC;
