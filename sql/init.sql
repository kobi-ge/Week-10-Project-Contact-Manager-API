CREATE TABLE IF NOT EXISTS contacts_table(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name	VARCHAR(50)	Not null,
    last_name VARCHAR(50),
    phone_number VARCHAR(20) Not nulL Unique
);
