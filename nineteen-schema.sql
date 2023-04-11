DROP DATABASE IF EXISTS nineteen;
CREATE DATABASE nineteen;
USE nineteen;

CREATE TABLE IF NOT EXISTS User (
    user_id INT AUTO_INCREMENT NOT NULL,
    user_username VARCHAR(50) NOT NULL,
    user_password VARCHAR(50) NOT NULL,
    user_email VARCHAR(100) NOT NULL ,
    PRIMARY KEY (user_id)
);

CREATE TABLE media (
	media_id	INT NOT NULL,
	media_type	VARCHAR(255) NOT NULL,
	link	VARCHAR(255),

	PRIMARY KEY (media_id)
);
