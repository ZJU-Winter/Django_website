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

 Date: 24/03/2021 22:49:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for a_labeledimage
-- ----------------------------
DROP TABLE IF EXISTS `a_labeledimage`;
CREATE TABLE `a_labeledimage`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `ImageID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `AreaID` int(11) NOT NULL,
  `Path` multipoint NULL,
  `PathType` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `UserID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `UserType` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `UserID_Check_1` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `UserID_Check_2` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CreateDate` datetime(6) NULL DEFAULT NULL,
  `PatientID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23585 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
