-- lists comedy shows from database
SELECT show_a.title 
FROM tv_genres AS tv_g
	INNER JOIN tv_show_genres AS tv_show_g
	ON tv_g.id = tv_show_g.genre_id 
	INNER JOIN tv_shows AS show_a
	ON tv_show_g.show_id = show_a.id 
WHERE tv_g.name = 'Comedy' 
ORDER BY show_a.title ASC;
