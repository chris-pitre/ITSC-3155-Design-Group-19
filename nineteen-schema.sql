DROP DATABASE IF EXISTS nineteen;
CREATE DATABASE nineteen;
USE nineteen;

CREATE TABLE media (
	media_id	INT NOT NULL,
	media_type	VARCHAR(255) NOT NULL,
	link	VARCHAR(255),

	PRIMARY KEY (media_id)
);