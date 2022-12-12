create table IF NOT EXISTS Publishers(
    publisherID         varchar(5)  NOT NULL,
    name                varchar(40) NOT NULL,
    address             varchar(150),
    phone               varchar(10),
    email               varchar(40),
    bankAccount         varchar(15) UNIQUE NOT NULL,
    PRIMARY KEY(publisherID)
);

create table IF NOT EXISTS Users(
    username            varchar(30) NOT NULL,
    password            varchar(30) NOT NULL,
    PRIMARY KEY(username)
);

create table IF NOT EXISTS Books(
    ISBN                char(6) NOT NULL,
    BookName            varchar(350) NOT NULL,
    author              varchar(50),
    price               numeric(9,2),
    salePercentage      numeric(4,2),
    numPages            numeric(7,0),
    genre               varchar(30),
    publisherID         varchar(5),
    PRIMARY KEY(ISBN),
    FOREIGN KEY(publisherID) REFERENCES Publishers
);

create table IF NOT EXISTS Orders(
    orderNum            numeric(4, 0) NOT NULL,
    orderDate           date,
    orderQuantity       numeric(100,0),
    ISBN                char(6) NOT NULL,
    username            varchar(30) NOT NULL,
    PRIMARY KEY(orderNum, ISBN, username),
    FOREIGN KEY(ISBN) references Books,
    FOREIGN KEY(username) references Users

);

create table IF NOT EXISTS Billing(
    username            varchar(30) NOT NULL,
    billingInfo         varchar(150) NOT NULL,
    PRIMARY KEY(username, billingInfo),
    FOREIGN KEY(username) references Users
);

create table IF NOT EXISTS Shipping(
    username            varchar(30) NOT NULL,
    shippingInfo         varchar(150) NOT NULL,
    PRIMARY KEY(username, shippingInfo),
    FOREIGN KEY(username) references Users
);