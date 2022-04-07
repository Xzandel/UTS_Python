-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2022 at 09:31 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_uts`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbarang`
--

CREATE TABLE `tbarang` (
  `KodeBrg` int(11) NOT NULL,
  `NamaBrg` varchar(40) NOT NULL,
  `Jenis` varchar(25) NOT NULL,
  `Stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbarangmasuk`
--

CREATE TABLE `tbarangmasuk` (
  `KodeBrgIn` int(11) NOT NULL,
  `KodeBrg` int(11) NOT NULL,
  `TglMasuk` date NOT NULL,
  `Jumlah` int(11) NOT NULL,
  `Supplier` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbarang`
--
ALTER TABLE `tbarang`
  ADD PRIMARY KEY (`KodeBrg`);

--
-- Indexes for table `tbarangmasuk`
--
ALTER TABLE `tbarangmasuk`
  ADD PRIMARY KEY (`KodeBrgIn`),
  ADD KEY `KodeBrg` (`KodeBrg`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tbarangmasuk`
--
ALTER TABLE `tbarangmasuk`
  ADD CONSTRAINT `KodeBrgConstraint` FOREIGN KEY (`KodeBrg`) REFERENCES `tbarang` (`KodeBrg`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
