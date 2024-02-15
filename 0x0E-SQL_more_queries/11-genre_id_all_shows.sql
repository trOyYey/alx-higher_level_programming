-- lists shows contained within hbtn_0d_tvshows
SELECT series.title, gnr.genre_id 
FROM tv_shows AS series
	LEFT JOIN tv_show_genres AS gnr
	ON series.id = gnr.show_id 
ORDER BY series.title ASC, gnr.genre_id ASC;
