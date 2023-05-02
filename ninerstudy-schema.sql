DROP DATABASE IF EXISTS ninerstudy;
CREATE DATABASE ninerstudy;
USE ninerstudy;

CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT NOT NULL,
    user_username VARCHAR(50) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_email VARCHAR(100) NOT NULL ,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS media (
	media_id	INT AUTO_INCREMENT NOT NULL,
	media_path	VARCHAR(1024) NOT NULL,
    media_alttext VARCHAR(512),
	PRIMARY KEY (media_id)
);

CREATE TABLE IF NOT EXISTS post(
    post_id int AUTO_INCREMENT NOT NULL,
    title VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    post_text TEXT NOT NULL,
    user_id INT NOT NULL,
    media_id INT,
    post_date datetime NOT NULL,
    last_updated datetime NOT NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY(media_id) REFERENCES media(media_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id)
);

CREATE TABLE IF NOT EXISTS reply(
    reply_id INT AUTO_INCREMENT NOT NULL,
    post_id INT NOT NULL,
    reply_text TEXT NOT NULL,
    media_id INT,
    post_date datetime NOT NULL,
    PRIMARY KEY(reply_id),
    FOREIGN KEY(post_id) REFERENCES post(post_id),
    FOREIGN KEY(media_id) REFERENCES media(media_id)
);