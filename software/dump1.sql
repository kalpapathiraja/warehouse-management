CREATE DATABASE  IF NOT EXISTS `supplier_identi` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `supplier_identi`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: supplier_identi
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` varchar(10) NOT NULL,
  `supp_code` varchar(45) NOT NULL,
  `stock_code` varchar(45) NOT NULL,
  `type_material` varchar(45) NOT NULL,
  `ec_val` int NOT NULL,
  `moisture` int NOT NULL,
  `fiber` int NOT NULL,
  `amount` float NOT NULL,
  `qc_check` varchar(45) NOT NULL,
  `storage_area` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'2023/10/27','JJ','271023JJ','wash',10,11,12,1000,'kalpa','lkr'),(2,'2023/10/27','JJ','271023JJ','wash',10,11,12,1000,'kalpa','lkr'),(3,'weq','qwe','qwe','qwe',12,12,12,22222,'sas','sda'),(4,'sdsadas','asdad','asdad','asdad',12,23,21,1000.12,'sdffs','asdad'),(5,'','','','',0,0,0,0,'',NULL),(6,'','','','',0,0,0,0,'',NULL),(7,'','','','',0,0,0,0,'',NULL),(8,'','','','',0,0,0,0,'',NULL),(9,'sf','sdf','sfdsf','sfd',11,11,11,1111,'sdf','sdf'),(10,'jjj','jjjj','jjjj','jjjj',111,11,11,11,'sdf','sdf'),(11,'asd','sdasa','asd','asd',11,11,11,111,'sad','asd'),(12,'2023/10/27','FF','271023FF','wash',300,12,23,2000,'kalpa','lkr'),(13,'2023/10/28','KK','281023KK','wash',350,20,24,2400,'kalpa','lkr'),(14,'2023/10/30','HP02','301023HP02','Treat',290,23,27,3000,'kalpa','kpl');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'supplier_identi'
--

--
-- Dumping routines for database 'supplier_identi'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-28  1:05:46
