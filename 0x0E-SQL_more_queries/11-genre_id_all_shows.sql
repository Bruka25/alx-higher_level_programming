-- Script that  lists all shows contained in the database hbtn_0d_tvshows
-- Results will be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Display NULL if a show doesn't have genre

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
