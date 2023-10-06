
-- Create Initial Tables

CREATE TABLE GeneralUserPool
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    home_address VARCHAR(150) NOT NULL
);

CREATE TABLE GroundTruth
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    home_address VARCHAR(150) NOT NULL
);

CREATE TABLE SessionTable
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    home_address VARCHAR(150) NOT NULL
);

-- Merchandise Buyers Table
CREATE TABLE MerchandiseBuyers
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    purchaseDate DATE NOT NULL,
    moneySpent DECIMAL(10,2) NOT NULL
);

-- Parents of KSU Students
CREATE TABLE ParentsOfKSUStudents
(
    userID SERIAL PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    streetAddress VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    usState VARCHAR(50) NOT NULL,
    zipCode VARCHAR(50) NOT NULL,
    childName VARCHAR(50) NOT NULL,
    childEmail VARCHAR(50),
    stillAttending BOOLEAN NOT NULL
);

-- Regular Ticket Buyers
CREATE TABLE RegularTicketBuyers
(
    buyerID SERIAL PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    purchaseDate DATE NOT NULL,
    moneySpent DECIMAL(10,2) NOT NULL,
    gameDate DATE NOT NULL
);

-- Mailing List
CREATE TABLE MailingList
(
    userID SERIAL PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL
);

-- Alumni
CREATE TABLE Alumni
(
    userID SERIAL PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    streetAddress VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    usState VARCHAR(50) NOT NULL,
    zipCode VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    dateEnrolled DATE NOT NULL,
    gradYear INT NOT NULL,
    degree VARCHAR(50) NOT NULL,
    major VARCHAR(50) NOT NULL,
    stillAttending BOOLEAN NOT NULL
);
