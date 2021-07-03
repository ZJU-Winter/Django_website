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

 Date: 24/03/2021 22:49:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for patientbasicinfos
-- ----------------------------
DROP TABLE IF EXISTS `patientbasicinfos`;
CREATE TABLE `patientbasicinfos`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CheckDate` datetime(6) NULL DEFAULT NULL,
  `CheckNumber` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PatientID` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PatientName` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Gender` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `Age` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ClinicalDiagnosis` varchar(4000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ExaminationFindings` varchar(4000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `EndoscopicDiagnosis` varchar(4000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PathologicalDiagnosis` varchar(4000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PatientReport` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `HospitalID` varchar(3) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `PatientID`(`PatientID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19223 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
