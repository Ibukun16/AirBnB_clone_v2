-- A script that prepares a MySQL server for this project
-- creating a project testing database with the name : hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating a new user named : hbnb_test, in localhost and set password to it.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_test_pwd';
-- grant all privilege for user 'hbnb_test' on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant privilege of SELECT to user 'hbnb_test' on the database performance_schema
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
