-- lists all shows and all genres linked to specified show
SELECT show_s.title, tv_g.name
FROM tv_shows AS show_s
	LEFT JOIN tv_show_genres AS show_g
	ON show_s.id = show_g.show_id
		LEFT JOIN tv_genres AS tv_g
		ON show_g.genre_id = tv_g.id
ORDER BY show_s.title ASC, tv_g.name ASC;
