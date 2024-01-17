-- Script that creates the database hbtn_0d_usa and the table cities
-- with desriptions 'id', 'state_id', and  'name'
-- Script should run if the table already exists

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(id)
);
