--  script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT gen.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS gen
       INNER JOIN `tv_show_genres` AS tv
       ON gen.`id` = tv.`genre_id`
 GROUP BY gen.`name`
 ORDER BY `number_of_shows` DESC;
