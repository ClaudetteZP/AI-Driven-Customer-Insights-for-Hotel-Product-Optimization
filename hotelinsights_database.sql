CREATE DATABASE HotelInsights;
GO

USE HotelInsights;
GO

-- Bookings table
CREATE TABLE Bookings (
    booking_id INT IDENTITY(1,1) PRIMARY KEY,
    hotel NVARCHAR(100),
    is_canceled BIT,
    lead_time INT,
    arrival_date DATE,
    country NVARCHAR(50),
    children INT
);

-- Reviews table
CREATE TABLE Reviews (
    review_id INT IDENTITY(1,1) PRIMARY KEY,
    rating INT,
    review_text NVARCHAR(MAX),
    review_date DATE
);
