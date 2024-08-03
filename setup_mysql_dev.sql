-- A script that prepares a MySQL server for this project
-- creating a project development database with the name: hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating a new user name: 'hbnh_dev', having all privileges on hbnb_dev_db only.
-- password for 'hbnh_dev_db' set to hbnb_dev_pwd.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges to new user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- grant SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
