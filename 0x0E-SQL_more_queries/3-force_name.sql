-- Create table 'force_name'
-- The attribute name can't be null
-- The script should run if the table exists

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
