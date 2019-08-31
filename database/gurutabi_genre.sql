-- MySQL dump 10.13  Distrib 8.0.15, for osx10.14 (x86_64)
--
-- Host: localhost    Database: spot_db
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gurutabi_genre_small`
--

DROP TABLE IF EXISTS `gurutabi_genre_small`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
INSERT INTO `gurutabi_genre_small` VALUES (1,'山岳','自然'),(2,'高原','自然'),(3,'湖沼','自然'),(4,'滝・河川','自然'),(5,'海岸','自然'),(6,'洞窟・鍾乳洞','自然'),(7,'展望台','自然'),(8,'湧水・名水','自然'),(9,'その他の自然風景','自然'),(10,'神社・仏閣','歴史・郷土文化'),(11,'城・城址','歴史・郷土文化'),(12,'歴史的・近代的建造物','歴史・郷土文化'),(13,'ダム・水門','歴史・郷土文化'),(14,'旧街道','歴史・郷土文化'),(15,'町並み','歴史・郷土文化'),(16,'港・漁港','歴史・郷土文化'),(17,'その他体験プログラム','体験プログラム'),(18,'テーマパーク・レジャーランド','テーマパーク・体験施設'),(19,'工場見学・その他見学施設','テーマパーク・体験施設'),(20,'海水浴場・潮干狩り場','テーマパーク・体験施設'),(21,'釣り・漁体験','テーマパーク・体験施設'),(22,'農園・果樹園','テーマパーク・体験施設'),(23,'その他体験施設','テーマパーク・体験施設'),(24,'温泉地・温泉街','温泉'),(25,'公園','公園・庭園'),(26,'庭園','公園・庭園'),(27,'動物園','動物園・水族館'),(28,'水族館','動物園・水族館'),(29,'植物園','動物園・水族館'),(30,'美術館','美術館・博物館'),(31,'博物館','美術館・博物館'),(32,'空港・遊覧飛行場','乗り物'),(33,'フェリー・船乗り場','乗り物'),(34,'ケーブルカー・ロープウェイ','乗り物'),(35,'鉄道','乗り物'),(36,'キャンプ場・バーベキュー場','アウトドア・スポーツ'),(37,'ハイキングコース','アウトドア・スポーツ'),(38,'サイクリングコース','アウトドア・スポーツ'),(39,'フィールド・アスレチック','アウトドア・スポーツ'),(40,'ゴルフ場','アウトドア・スポーツ'),(41,'スキー場','アウトドア・スポーツ'),(42,'運動公園・ほかスポーツ施設','アウトドア・スポーツ'),(43,'マリーナ・ヨットハーバー','アウトドア・スポーツ'),(44,'観光案内所','観光案内'),(45,'観光タクシー','観光案内'),(46,'レンタサイクル','観光案内'),(47,'観光ボランティア','観光案内'),(48,'観光船・水上バス','ケーブルカー・遊覧船'),(49,'アウトレット','百貨店・ショッピングモール・アウトレットモール'),(50,'酒蔵','酒屋・酒造・ワイナリー'),(51,'ワイナリー','酒屋・酒造・ワイナリー'),(52,'道の駅','その他施設・名所'),(53,'劇場・コンサートホール','その他施設・名所'),(54,'公共施設','その他施設・名所');
/*!40000 ALTER TABLE `gurutabi_genre_small` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-31 11:42:52
