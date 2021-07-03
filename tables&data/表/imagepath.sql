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

 Date: 24/03/2021 22:49:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for imagepath
-- ----------------------------
DROP TABLE IF EXISTS `imagepath`;
CREATE TABLE `imagepath`  (
  `CheckNumber` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PatientID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ImageID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ImgPath` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ImageID`) USING BTREE,
  INDEX `PatientID`(`PatientID`) USING BTREE,
  INDEX `ImageID`(`ImageID`) USING BTREE,
  INDEX `ImagePath`(`ImgPath`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
