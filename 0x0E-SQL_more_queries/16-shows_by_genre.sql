-- Script that lists all shows, and all genres linked to that show, from the database
-- Results must be sorted in ascending order by the show title and genre name
-- If the show doesn't have genre display NULL the genre column

SELECT t.`title`, tvg.`name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS tvs ON t.`id` = tvs.`show_id`
LEFT JOIN `tv_genres` AS tvg ON tvs.`genre_id` = tvg.`id`
ORDER BY t.`title`, tvg.`name`;
