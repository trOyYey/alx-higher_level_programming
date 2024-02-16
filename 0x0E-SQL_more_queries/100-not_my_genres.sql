-- lists genre opposite of Dexter's
SELECT tv_genres.name
from tv_genres
WHERE tv_genres.name NOT IN (
		SELECT tv_g.name FROM tv_genres AS tv_g
			INNER JOIN tv_show_genres AS show_g
			ON tv_g.id = show_g.genre_id
			INNER JOIN tv_shows AS show_s
			ON show_g.show_id = show_s.id
		WHERE show_s.title = 'Dexter')
ORDER BY tv_genres.name ASC;
