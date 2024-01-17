-- Script that  creates table 'unique_id'
-- with the attribute 'id' has to be unique
-- Script should run if the table exists already

CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
