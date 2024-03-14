--  script that creates the MySQL server user user_0d_1.
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES TO 'user_0d_1'@'localhost';
