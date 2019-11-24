-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: spot_db
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gurutabi_genre`
--

DROP TABLE IF EXISTS `gurutabi_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gurutabi_genre` (
  `id` int(11) NOT NULL,
  `gurutabi_genre_id` int(11) DEFAULT NULL,
  `oreore_genre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `gurutabi_genre_id` (`gurutabi_genre_id`),
  KEY `oreore_genre_id` (`oreore_genre_id`),
  CONSTRAINT `gurutabi_genre_ibfk_1` FOREIGN KEY (`gurutabi_genre_id`) REFERENCES `gurutabi_genre_small` (`gurutabi_genre_id`),
  CONSTRAINT `gurutabi_genre_ibfk_2` FOREIGN KEY (`oreore_genre_id`) REFERENCES `oreore_genre` (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gurutabi_genre`
--

LOCK TABLES `gurutabi_genre` WRITE;
/*!40000 ALTER TABLE `gurutabi_genre` DISABLE KEYS */;
/*!40000 ALTER TABLE `gurutabi_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gurutabi_genre_small`
--

DROP TABLE IF EXISTS `gurutabi_genre_small`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gurutabi_genre_small` (
  `gurutabi_genre_id` int(11) NOT NULL,
  `genre_small` varchar(128) DEFAULT NULL,
  `genre_middle` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`gurutabi_genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gurutabi_genre_small`
--

LOCK TABLES `gurutabi_genre_small` WRITE;
/*!40000 ALTER TABLE `gurutabi_genre_small` DISABLE KEYS */;
/*!40000 ALTER TABLE `gurutabi_genre_small` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jalan_genre`
--

DROP TABLE IF EXISTS `jalan_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jalan_genre` (
  `id` int(11) NOT NULL,
  `jalan_genre_id` int(11) DEFAULT NULL,
  `oreore_genre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `jalan_genre_id` (`jalan_genre_id`),
  KEY `oreore_genre_id` (`oreore_genre_id`),
  CONSTRAINT `jalan_genre_ibfk_1` FOREIGN KEY (`oreore_genre_id`) REFERENCES `oreore_genre` (`genre_id`),
  CONSTRAINT `jalan_genre_ibfk_2` FOREIGN KEY (`jalan_genre_id`) REFERENCES `jalan_genre_small` (`jalan_genre_id`),
  CONSTRAINT `jalan_genre_ibfk_3` FOREIGN KEY (`oreore_genre_id`) REFERENCES `oreore_genre` (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jalan_genre`
--

LOCK TABLES `jalan_genre` WRITE;
/*!40000 ALTER TABLE `jalan_genre` DISABLE KEYS */;
/*!40000 ALTER TABLE `jalan_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jalan_genre_small`
--

DROP TABLE IF EXISTS `jalan_genre_small`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jalan_genre_small` (
  `jalan_genre_id` int(11) NOT NULL,
  `genre_small` varchar(128) DEFAULT NULL,
  `genre_large` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`jalan_genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jalan_genre_small`
--

LOCK TABLES `jalan_genre_small` WRITE;
/*!40000 ALTER TABLE `jalan_genre_small` DISABLE KEYS */;
/*!40000 ALTER TABLE `jalan_genre_small` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oreore_genre`
--

DROP TABLE IF EXISTS `oreore_genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oreore_genre` (
  `genre_id` int(11) NOT NULL,
  `genre_name` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oreore_genre`
--

LOCK TABLES `oreore_genre` WRITE;
/*!40000 ALTER TABLE `oreore_genre` DISABLE KEYS */;
/*!40000 ALTER TABLE `oreore_genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spot`
--

DROP TABLE IF EXISTS `spot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `spot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `lon` float NOT NULL,
  `lat` float NOT NULL,
  `image` varchar(256) NOT NULL,
  `access_text` varchar(256) NOT NULL,
  `address_code` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spot`
--

LOCK TABLES `spot` WRITE;
/*!40000 ALTER TABLE `spot` DISABLE KEYS */;
/*!40000 ALTER TABLE `spot` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

--
-- Table structure for table `oreore_spot_mapping`
--

DROP TABLE IF EXISTS `oreore_spot_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oreore_spot_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spot_id` int(11) NOT NULL,
  `oreore_genre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `oreore_spot_mapping_ibfk_1` FOREIGN KEY (`spot_id`) REFERENCES `spot` (`id`),
  CONSTRAINT `oreore_spot_mapping_ibfk_2` FOREIGN KEY (`oreore_genre_id`) REFERENCES `oreore_genre` (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oreore_spot_mapping`
--

LOCK TABLES `oreore_spot_mapping` WRITE;
/*!40000 ALTER TABLE `oreore_spot_mapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `oreore_spot_mapping` ENABLE KEYS */;
UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-10 11:30:39
