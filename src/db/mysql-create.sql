-- MySQL dump 10.13  Distrib 5.1.49, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: dotabook
-- ------------------------------------------------------
-- Server version	5.1.49-1ubuntu8.1

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
-- Table structure for table `t_dota_config`
--

DROP TABLE IF EXISTS `t_dota_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_config` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(64) DEFAULT NULL,
  `value` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_grade`
--

DROP TABLE IF EXISTS `t_dota_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_grade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) DEFAULT NULL,
  `hid` int(11) DEFAULT NULL,
  `score` float DEFAULT NULL,
  `catalog` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_hero`
--

DROP TABLE IF EXISTS `t_dota_hero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_hero` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vid` int(11) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `namecn` varchar(64) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_hero_attr`
--

DROP TABLE IF EXISTS `t_dota_hero_attr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_hero_attr` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hid` int(11) DEFAULT NULL,
  `hp` int(11) DEFAULT NULL,
  `mp` int(11) DEFAULT NULL,
  `basic` varchar(1) DEFAULT NULL,
  `affilication` varchar(1) DEFAULT NULL,
  `damage` varchar(16) DEFAULT NULL,
  `armor` float DEFAULT NULL,
  `move_speed` int(11) DEFAULT NULL,
  `attack_range` int(11) DEFAULT NULL,
  `attack_animation` varchar(16) DEFAULT NULL,
  `casting_animation` varchar(16) DEFAULT NULL,
  `attack_time` float DEFAULT NULL,
  `missile_speed` int(11) DEFAULT NULL,
  `sight_range` varchar(16) DEFAULT NULL,
  `intelligence` int(11) DEFAULT NULL,
  `agility` int(11) DEFAULT NULL,
  `strength` int(11) DEFAULT NULL,
  `goup_intelligence` float DEFAULT NULL,
  `goup_agility` float DEFAULT NULL,
  `goup_strength` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_hero_image`
--

DROP TABLE IF EXISTS `t_dota_hero_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_hero_image` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hid` int(11) DEFAULT NULL,
  `image45` varchar(128) DEFAULT NULL,
  `image64` varchar(128) DEFAULT NULL,
  `comic` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_hero_skill`
--

DROP TABLE IF EXISTS `t_dota_hero_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_hero_skill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hid` int(11) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `namecn` varchar(64) DEFAULT NULL,
  `hotkey` varchar(1) DEFAULT NULL,
  `ability` varchar(16) DEFAULT NULL,
  `target` varchar(16) DEFAULT NULL,
  `image` varchar(128) DEFAULT NULL,
  `description` text,
  `note` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=413 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_hero_skill_level`
--

DROP TABLE IF EXISTS `t_dota_hero_skill_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_hero_skill_level` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `mana_cost` int(11) DEFAULT NULL,
  `cooldown` int(11) DEFAULT NULL,
  `casting_range` int(11) DEFAULT NULL,
  `area` int(11) DEFAULT NULL,
  `duration` varchar(64) DEFAULT NULL,
  `target` varchar(16) DEFAULT NULL,
  `effect` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1556 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_item`
--

DROP TABLE IF EXISTS `t_dota_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vid` int(11) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `namecn` varchar(64) DEFAULT NULL,
  `picture` varchar(512) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `shop` varchar(64) DEFAULT NULL,
  `category` varchar(16) DEFAULT NULL,
  `description` text,
  `info` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=164 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_item_compound`
--

DROP TABLE IF EXISTS `t_dota_item_compound`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_item_compound` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `iid_1` int(11) DEFAULT NULL,
  `iid_2` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=193 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_item_skill`
--

DROP TABLE IF EXISTS `t_dota_item_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_item_skill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `iid` int(11) DEFAULT NULL,
  `name` varchar(64) DEFAULT NULL,
  `namecn` varchar(64) DEFAULT NULL,
  `ability` varchar(16) DEFAULT NULL,
  `mana_cost` int(11) DEFAULT NULL,
  `cooldown` int(11) DEFAULT NULL,
  `duration` varchar(64) DEFAULT NULL,
  `casting_range` int(11) DEFAULT NULL,
  `area` int(11) DEFAULT NULL,
  `description` text,
  `note` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_map`
--

DROP TABLE IF EXISTS `t_dota_map`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_map` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(64) DEFAULT NULL,
  `namecn` varchar(64) DEFAULT NULL,
  `description` text,
  `filename` varchar(512) DEFAULT NULL,
  `category` varchar(16) DEFAULT NULL,
  `url` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `version` (`version`),
  UNIQUE KEY `namecn` (`namecn`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_dota_version`
--

DROP TABLE IF EXISTS `t_dota_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_dota_version` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(16) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `version` (`version`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_upgrade`
--

DROP TABLE IF EXISTS `t_upgrade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_upgrade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` datetime DEFAULT NULL,
  `datetag` int(11) DEFAULT NULL,
  `title` varchar(16) DEFAULT NULL,
  `description` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) DEFAULT NULL,
  `username` varchar(64) DEFAULT NULL,
  `nickname` varchar(64) DEFAULT NULL,
  `source` varchar(32) DEFAULT NULL,
  `token_key` varchar(64) DEFAULT NULL,
  `token_secret` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-03-25 14:08:01
