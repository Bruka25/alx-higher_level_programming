-- Script that creates table 'id_not_null'
-- id INT default value 1, name VARCHAR(256)
-- Script should run if the table exists already

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
