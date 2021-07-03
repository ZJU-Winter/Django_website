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

 Date: 24/03/2021 22:49:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for d_arearoi
-- ----------------------------
DROP TABLE IF EXISTS `d_arearoi`;
CREATE TABLE `d_arearoi`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `AreaID` int(11) NOT NULL,
  `DiseaseID` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 78012 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '感兴趣区域ROI的矩形框，一个矩形框表示的疾病可能由多行信息限定。' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
