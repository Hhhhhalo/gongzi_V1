

--
-- Table structure for table `aboutus`
--

DROP TABLE IF EXISTS `neitui`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `yuangong_gongzi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `yingfa` varchar(200) DEFAULT NULL COMMENT '应发',
  `baoshui_jine` varchar(200) DEFAULT NULL COMMENT '报税金额',
  `yingfa_dixin` varchar(200) DEFAULT NULL COMMENT '应发底薪',
  `yingfa_jixiao` varchar(200) DEFAULT NULL COMMENT '应发绩效',
  `butie_heji` varchar(200) DEFAULT NULL COMMENT '补贴合计',
  `koujianxiang` varchar(200) DEFAULT NULL COMMENT '扣减项',
  `yijiao_shebao` varchar(200) DEFAULT NULL COMMENT '应缴社保',
  `geshui` varchar(200) DEFAULT NULL COMMENT '个税',
  `shifa` varchar(200) DEFAULT NULL COMMENT '实发',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='内推表';

CREATE TABLE `yuangong_jixiao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `xiangmuhao` varchar(200) DEFAULT NULL COMMENT '项目号',
  `xiangmumingc` varchar(200) DEFAULT NULL COMMENT '项目名称',
  `yeji` varchar(200) DEFAULT NULL COMMENT '业绩',
  `jixiaodian` varchar(200) DEFAULT NULL COMMENT '绩效点',
  `jili` varchar(200) DEFAULT NULL COMMENT '激励',
  `jixiao` varchar(200) DEFAULT NULL COMMENT '绩效',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='员工绩效表';

CREATE TABLE `neitui` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `neitui_name` varchar(200) NOT NULL COMMENT '推荐人',
  `be_neitui_name` varchar(200) DEFAULT NULL COMMENT '被推荐人',
  `ruzhi_time` varchar(200) DEFAULT NULL COMMENT '是否通过',
  `or_pass` varchar(200) DEFAULT NULL COMMENT '推荐人',
  `fenzu` varchar(200) DEFAULT NULL COMMENT '分组',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
   `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  `jiangli` varchar(200) DEFAULT NULL COMMENT '奖励',
  `daxiang` varchar(200) DEFAULT NULL COMMENT '大项',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='内推表';


CREATE TABLE `shebao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `fenzu` varchar(200) DEFAULT NULL COMMENT '分组',
  `danwei` varchar(200) DEFAULT NULL COMMENT '单位合计',
  `geren` varchar(200) DEFAULT NULL COMMENT '个人合计',
  `gongshang` varchar(200) DEFAULT NULL COMMENT '工伤',
  `shiye` varchar(200) DEFAULT NULL COMMENT '失业',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
   `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='shebao';


CREATE TABLE `yibao` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
    `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `fenzu` varchar(200) DEFAULT NULL COMMENT '分组',
  `danwei` varchar(200) DEFAULT NULL COMMENT '单位合计',
  `geren` varchar(200) DEFAULT NULL COMMENT '个人合计',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
   `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='yibao';

CREATE TABLE `kaoqin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
   `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `bumen` varchar(200) DEFAULT NULL COMMENT '部门',
  `ying_chuqin` varchar(200) DEFAULT NULL COMMENT '应出勤天',
  `shiji_chuqin` varchar(200) DEFAULT NULL COMMENT '实际出勤',
  `chuqinlv` varchar(200) DEFAULT NULL COMMENT '出勤率',
  `quanqin` varchar(200) DEFAULT NULL COMMENT '全勤奖',
  `queka` varchar(200) DEFAULT NULL COMMENT '缺卡',
  `queka_fare` varchar(200) DEFAULT NULL COMMENT '缺卡扣款',
  `chidao` varchar(200) DEFAULT NULL COMMENT '迟到',
  `chidao_fare` varchar(200) DEFAULT NULL COMMENT '迟到扣款',
  `bingjia` varchar(200) DEFAULT NULL COMMENT '病假',
  `shijia` varchar(200) DEFAULT NULL COMMENT '事假',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
  `create_time` varchar(200) DEFAULT NULL COMMENT '时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='kaoqin';


CREATE TABLE `duanxin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
   `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `xiangmu` varchar(200) DEFAULT NULL COMMENT '项目',
  `shenqing_fare` varchar(200) DEFAULT NULL COMMENT '申请费用',
  `renshu` varchar(200) DEFAULT NULL COMMENT '人数',
  `or_pass` varchar(200) DEFAULT NULL COMMENT '组管是否确认',
  `shifa` varchar(200) DEFAULT NULL COMMENT '实发',
  `fangshi` varchar(200) DEFAULT NULL COMMENT '发放方式',
  `shifa_time` varchar(200) DEFAULT NULL COMMENT '实发时间',
  `huishou_time` varchar(200) DEFAULT NULL COMMENT '回收时间',
  `huishou_fare` varchar(200) DEFAULT NULL COMMENT '回收费用',
  `daxiang` varchar(200) DEFAULT NULL COMMENT '大项',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='duanxin';

CREATE TABLE `zhichang_kaizhi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
    `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  
  `xiangmu` varchar(200) DEFAULT NULL COMMENT '项目',
  `fare` varchar(200) DEFAULT NULL COMMENT '金额',
  `daxiang` varchar(200) DEFAULT NULL COMMENT '大项',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
`create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='zhichang_kaizhi';

CREATE TABLE `zongjingban_kaizhi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
    `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  `xiangmu` varchar(200) DEFAULT NULL COMMENT '项目',
  `fare` varchar(200) DEFAULT NULL COMMENT '金额',

  `daxiang` varchar(200) DEFAULT NULL COMMENT '大项',
`gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='zongjingban_kaizhi';

CREATE TABLE `duanxin_fare` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
    `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '姓名',
  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  `gongzi_time` varchar(200) DEFAULT NULL COMMENT '结算日期',
  `fare` varchar(200) DEFAULT NULL COMMENT '实际费用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='duanxin_fare';


CREATE TABLE `xiangmu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
    `gonghao` varchar(200) NOT NULL COMMENT '项目号',
  `xiangmu_name` varchar(200) NOT NULL COMMENT '项目名称',

  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  `ticheng` varchar(200) DEFAULT NULL COMMENT '提成',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='xiangmu';

CREATE TABLE `jixiaofangan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
 `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `jine` varchar(200) NOT NULL COMMENT '回收金额',
  `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  `tichengdian` varchar(200) DEFAULT NULL COMMENT '提成点',
  `xishu` varchar(200) DEFAULT NULL COMMENT '系数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='jixiaofangan';

CREATE TABLE `bumen` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
 `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `bumen_name` varchar(200) NOT NULL COMMENT '部门名称',
   `create_time` varchar(200) DEFAULT NULL COMMENT '创kaoqin建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='bumen';

CREATE TABLE `yuangong` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
   `gonghao` varchar(200) NOT NULL COMMENT '工号',
  `name` varchar(200) NOT NULL COMMENT '员工名字',
  `bumen_name` varchar(200) NOT NULL COMMENT '部门名称',
  `dixin` varchar(200) NOT NULL COMMENT '底薪',
   `create_time` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='yuangong';

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
   `username` varchar(200) NOT NULL COMMENT '账号',
  `password` varchar(200) NOT NULL COMMENT '密码',
  `role` varchar(200) NOT NULL COMMENT '密码',
   `date` varchar(200) DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='users';
