-- Customer details table
CREATE TABLE customer_details (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(225) NOT NULL
);

-- Customer quotation table
CREATE TABLE customer_quotation (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    quotation_name VARCHAR(225) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer_details(id)
);

-- Quotation table instance
CREATE TABLE quotation_table_instance (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    quotation_id INT NOT NULL,
    table_name VARCHAR(225) NOT NULL,
    FOREIGN KEY (quotation_id) REFERENCES customer_quotation(id)
);

CREATE TABLE table_header_type (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    field_type VARCHAR(225) NOT NULL
);
INSERT INTO `customer_quotation`.`table_header_type` (`id`, `field_type`) VALUES ('1', 'Text');
INSERT INTO `customer_quotation`.`table_header_type` (`id`, `field_type`) VALUES ('2', 'Amount');
INSERT INTO `customer_quotation`.`table_header_type` (`id`, `field_type`) VALUES ('3', 'Number');
INSERT INTO `customer_quotation`.`table_header_type` (`id`, `field_type`) VALUES ('4', 'Date');

-- Quotation table header
CREATE TABLE quotation_table_header (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    table_id INT NOT NULL,
    field_type INT NOT NULL,
    field_name VARCHAR(225) NOT NULL,
    FOREIGN KEY (table_id) REFERENCES quotation_table_instance(id),
    FOREIGN KEY (field_type) REFERENCES table_header_type(id)
);

-- Quotation table value
CREATE TABLE quotation_table_value (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    field_id INT NOT NULL,
    field_value VARCHAR(225) NOT NULL,
    FOREIGN KEY (field_id) REFERENCES quotation_table_header(id)
);

CREATE TABLE customer_quotation_details (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    quotation_date DATE,
    quotation_address TEXT,
    quotation_subject TEXT(255),
    quotation_description VARCHAR(255),
    quotation_referrence VARCHAR(255),
    quotation_note TEXT(255),
    quotation_bank_details TEXT,
    quotation_signature VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES customer_details(id)
);

-- Add row_id to your value table
ALTER TABLE quotation_table_value ADD COLUMN row_id INT NOT NULL AFTER id;

-- Add a unique constraint to prevent duplicate values for same field in same row
ALTER TABLE quotation_table_value 
ADD CONSTRAINT unique_field_per_row UNIQUE (field_id, row_id);


-- Add row_id to your value table
ALTER TABLE customer_quotation_details ADD COLUMN quotation_id INT NOT NULL AFTER id;

ALTER TABLE quotation_table_instance ADD COLUMN table_total float NULL AFTER table_name;