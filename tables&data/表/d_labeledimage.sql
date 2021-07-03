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

 Date: 24/03/2021 22:49:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for d_labeledimage
-- ----------------------------
DROP TABLE IF EXISTS `d_labeledimage`;
CREATE TABLE `d_labeledimage`  (
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
  `PatientID` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CreatedBy` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT 'DOCTOR',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28498 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '被医生标记带有某种疾病的图像都被保存在这个表中' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
