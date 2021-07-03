/*
 Navicat Premium Data Transfer

 Source Server         : 本机MySQL
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : database_exp

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 24/03/2021 22:49:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for diseasedict
-- ----------------------------
DROP TABLE IF EXISTS `diseasedict`;
CREATE TABLE `diseasedict`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DiseaseName` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `DiseaseID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 125 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '疾病字典，包括三个字段，第一列为疾病部位：0表示胃；第二列为疾病名称；第三列为疾病字串ID。' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
