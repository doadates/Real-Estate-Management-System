CREATE TABLE estate_agent (

id SERIAL PRIMARY KEY,
name VARCHAR(100),
address TEXT,
login VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(100) NOT NULL 
);


CREATE TABLE estate (

id SERIAL PRIMARY KEY,
city VARCHAR(100),
postal_code INT,
street VARCHAR(100),
street_number VARCHAR(50),
square_area INT,
agent_id INT NOT NULL REFERENCES estate_agent(id) ON DELETE SET NULL /*Each estate is managed by one agent: [1:1]*/

);



CREATE TABLE apartment (
id INT PRIMARY KEY REFERENCES estate(id) ON DELETE CASCADE,
floor INT,
rent REAL,
rooms INT,
balcony BOOLEAN,
built_in_kitchen BOOLEAN

);


CREATE TABLE house (
id INT PRIMARY KEY REFERENCES estate(id) ON DELETE CASCADE,
floor INT,
price REAL,
garden BOOLEAN

);

CREATE TABLE person (
id SERIAL PRIMARY KEY,
first_name VARCHAR(100),
name VARCHAR(100),
adress TEXT

);
 


CREATE TABLE contract (
id SERIAL PRIMARY KEY,
contract_no INT UNIQUE,
date DATE,
place VARCHAR(100),
person_id INT REFERENCES person(id) ON DELETE SET NULL
);

CREATE TABLE tenancy_contract (
id INT REFERENCES contract(id) ON DELETE CASCADE,
star_date DATE,
duration INT,
additional_costs DOUBLE PRECISION,
apartment_id INT  REFERENCES UNIQUE apartment(id) ON DELETE CASCADE

);


CREATE TABLE purchase_contract (
id INT PRIMARY KEY REFERENCES contract(id) ON DELETE CASCADE,
no_of_installments INT,
interest_rate DOUBLE PRECISION,
house_id INT  REFERENCES UNIQUE house(id) ON DELETE CASCADE

);



SELECT *
FROM estate_agent;


SELECT *
FROM estate;


SELECT *
FROM apartment;


SELECT *
FROM house;

SELECT *
FROM person;


SELECT *
FROM contract;