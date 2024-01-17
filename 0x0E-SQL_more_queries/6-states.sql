-- Script that creates a table states
-- With  primary key unique 'id' that will increment
-- with name of 256 chars limit
-- Script should run if states already exists

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
