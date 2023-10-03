--Create Initial Tables

--Merchandise Buyers Table
Create Table MerchandiseBuyers
(
    buyerID int Identity(1,1) Primary Key,
    firstName varchar(50) not null,
    lastName varchar(50) not null,
    purchaseDate date not null,
    moneySpent decimal(10,2) not null,
    email varchar(50) not null,
    phone varchar(50) not null,
)

--Parents of KSU Students
Create Table ParentsOfKSUStudents
(
    userID int Identity(1,1) Primary Key,
    firstName varchar(50) not null,
    lastName varchar(50) not null,
    streetAddress varchar(50) not null,
    city varchar(50) not null,
    usState varchar(50) not null,
    zipCode varchar(50) not null,
    childName varchar(50) not null,
    childEmail varchar(50)
    stillAttending bit not null,
)

--Regular Ticket Buyers
Create Table RegularTicketBuyers
(
    buyerID int Identity(1,1) Primary Key,
    firstName varchar(50) not null,
    lastName varchar(50) not null,
    purchaseDate date not null,
    moneySpent decimal(10,2) not null,
    gameDate date not null,
)

--Mailing List
Create Table MailingList
(
    userID int Identity(1,1) Primary Key,
    firstName varchar(50) not null,
    lastName varchar(50) not null,
    email varchar(50) not null,
    phone varchar(50) not null,
)

--Alumni
Create Table Alumni
(
    userID int Identity(1,1) Primary Key,
    firstName varchar(50) not null,
    lastName varchar(50) not null,
    gender varchar(50) not null,
    age int not null,
    streetAddress varchar(50) not null,
    city varchar(50) not null,
    usState varchar(50) not null,
    zipCode varchar(50) not null,
    email varchar(50) not null,
    phone varchar(50) not null,
    dateEnrolled date not null,
    gradYear int not null,
    degree varchar(50) not null,
    major varchar(50) not null,
    stillAttending bit not null,
)
--County Resident
--TODO: Add County Resident Table
--Gonna hold off on this one as the data for users addresses are already in most of the tables
-- Create Table CountyResident
-- (

-- )

