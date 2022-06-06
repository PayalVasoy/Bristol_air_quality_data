-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:8080
-- Generation Time: Dec 18, 2021 at 05:01 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pollution-db`
--

-- --------------------------------------------------------

--
-- Table structure for table `readings`
--

CREATE TABLE `readings` (
  `reading_id` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `NOx` float DEFAULT NULL,
  `NO2` float DEFAULT NULL,
  `PM10` float DEFAULT NULL,
  `NVPM10` float DEFAULT NULL,
  `VPM10` float DEFAULT NULL,
  `NVPM2.5` float DEFAULT NULL,
  `PM2.5` float DEFAULT NULL,
  `VPM2.5` float DEFAULT NULL,
  `CO` float DEFAULT NULL,
  `O3` float DEFAULT NULL,
  `SO2` float DEFAULT NULL,
  `Temperature` float DEFAULT NULL,
  `RH` float DEFAULT NULL,
  `Air_pressure` float DEFAULT NULL,
  `DateStart` datetime DEFAULT NULL,
  `DateEnd` datetime DEFAULT NULL,
  `Current` text DEFAULT NULL,
  `Instrument_Type` varchar(45) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `schema`
--

CREATE TABLE `schema` (
  `measure` varchar(45) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `unit` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `station`
--

CREATE TABLE `station` (
  `station_id` int(11) NOT NULL,
  `Location` varchar(45) NOT NULL,
  `geo_point_2d` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `readings`
--
ALTER TABLE `readings`
  ADD PRIMARY KEY (`reading_id`),
  ADD KEY `station_id` (`station_id`);

--
-- Indexes for table `schema`
--
ALTER TABLE `schema`
  ADD PRIMARY KEY (`measure`);

--
-- Indexes for table `station`
--
ALTER TABLE `station`
  ADD PRIMARY KEY (`station_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `readings`
--
ALTER TABLE `readings`
  ADD CONSTRAINT `readings_ibfk_1` FOREIGN KEY (`station_id`) REFERENCES `station` (`station_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
