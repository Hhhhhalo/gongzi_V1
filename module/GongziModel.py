import json
import os
import random
from datetime import datetime
# import faker

from sqlalchemy import JSON, Column, Integer, String, Text, func, text
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()


class YuangongGongzi(db.Model):
    __tablename__ = 'yuangong_gongzi'

    id = Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = Column(String(200), nullable=False, comment='工号')
    name = Column(String(200), nullable=False, comment='姓名')
    yingfa = Column(String(200), comment='应发')  # 通常这里应该用Float或Decimal
    baoshui_jine = Column(String(200), comment='报税金额')  # 同上
    yingfa_dixin = Column(String(200), comment='应发底薪')  # 同上
    yingfa_jixiao = Column(String(200), comment='应发绩效')  # 同上
    butie_heji = Column(String(200), comment='补贴合计')  # 同上
    koujianxiang = Column(String(200), comment='扣减项')
    yijiao_shebao = Column(String(200), comment='应缴社保')  # 同上
    geshui = Column(String(200), comment='个税')  # 同上
    shifa = Column(String(200), comment='实发')  # 同上
    gongzi_time = Column(db.DateTime, comment='结算日期')  # 修改为DateTime类型
    create_time = Column(db.DateTime, comment='创建日期')  # 修改为DateTime类型

class YuangongJixiao(db.Model):
    __tablename__ = 'yuangong_jixiao'

    id = Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = Column(String(200), nullable=False, comment='工号')
    name = Column(String(200), nullable=False, comment='姓名')
    xiangmuhao = Column(String(200), comment='项目号')  # 通常这里应该用Float或Decimal
    xiangmumingc = Column(String(200), comment='项目名称')  # 同上
    yeji = Column(String(200), comment='业绩')  # 同上
    jixiaodian = Column(String(200), comment='绩效点')  # 同上
    jili = Column(String(200), comment='激励')  # 同上
    jixiao = Column(String(200), comment='绩效')
    gongzi_time = Column(db.DateTime, comment='结算日期')  # 修改为DateTime类型
    create_time = Column(db.DateTime, comment='创建日期')  # 修改为DateTime类型


class Neitui(db.Model):
        # return f'<Neitui {self.id}: {self.neitui_name}>'
    __tablename__ = 'neitui'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    neitui_name = db.Column(db.String(200), nullable=False, comment='推荐人')
    be_neitui_name = db.Column(db.String(200), comment='被推荐人')
    ruzhi_time = db.Column(db.String(200), comment='是否通过')  # 注意：这个字段名可能不太准确，根据实际情况调整
    or_pass = db.Column(db.String(200), comment='推荐状态')  # 修改字段名以避免混淆
    fenzu = db.Column(db.String(200), comment='分组')
    jiangli = db.Column(db.String(200), comment='奖励')
    daxiang = db.Column(db.String(200), comment='大项')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.DateTime, comment='创建日期')



class Shebao(db.Model):
    __tablename__ = 'shebao'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    fenzu = db.Column(db.String(200), comment='分组')
    danwei = db.Column(db.String(200), comment='单位合计')
    geren = db.Column(db.String(200), comment='个人合计')
    gongshang = db.Column(db.String(200), comment='工伤')
    shiye = db.Column(db.String(200), comment='失业')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime


class Yibao(db.Model):
    __tablename__ = 'yibao'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    fenzu = db.Column(db.String(200), comment='分组')
    danwei = db.Column(db.String(200), comment='单位合计')
    geren = db.Column(db.String(200), comment='个人合计')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime


class Kaoqin(db.Model):
    __tablename__ = 'kaoqin'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    bumen = db.Column(db.String(200), comment='部门')
    ying_chuqin = db.Column(db.String(200), comment='应出勤天')
    shiji_chuqin = db.Column(db.String(200), comment='实际出勤')
    chuqinlv = db.Column(db.String(200), comment='出勤率')
    quanqin = db.Column(db.String(200), comment='全勤奖')
    queka = db.Column(db.String(200), comment='缺卡')
    queka_fare = db.Column(db.String(200), comment='缺卡扣款')
    chidao = db.Column(db.String(200), comment='迟到')
    chidao_fare = db.Column(db.String(200), comment='迟到扣款')
    bingjia = db.Column(db.String(200), comment='病假')
    shijia = db.Column(db.String(200), comment='事假')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.DateTime, comment='时间')


class Duanxin(db.Model):
    __tablename__ = 'duanxin'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    xiangmu = db.Column(db.String(200), comment='项目')
    shenqing_fare = db.Column(db.String(200), comment='申请费用')
    renshu = db.Column(db.String(200), comment='人数')
    or_pass = db.Column(db.String(200), comment='组管是否确认')
    shifa = db.Column(db.String(200), comment='实发')
    fangshi = db.Column(db.String(200), comment='发放方式')
    shifa_time = db.Column(db.String(200), comment='实发时间')
    huishou_time = db.Column(db.String(200), comment='回收时间')
    huishou_fare = db.Column(db.String(200), comment='回收费用')
    daxiang = db.Column(db.String(200), comment='大项')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime


class ZhichangKaizhi(db.Model):
    __tablename__ = 'zhichang_kaizhi'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    xiangmu = db.Column(db.String(200), comment='项目')
    fare = db.Column(db.String(200), comment='金额')
    daxiang = db.Column(db.DateTime, comment='大项')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.String(200), comment='创建日期')  # 通常建议使用db.DateTime


class ZongjingbanKaizhi(db.Model):
    __tablename__ = 'zongjingban_kaizhi'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    xiangmu = db.Column(db.DateTime, comment='项目')
    fare = db.Column(db.String(200), comment='金额')
    daxiang = db.Column(db.String(200), comment='大项')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.String(200), comment='创建日期')  # 通常建议使用db.DateTime


class DuanxinFare(db.Model):
    __tablename__ = 'duanxin_fare'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='姓名')
    fare = db.Column(db.String(200), comment='实际费用')
    gongzi_time = db.Column(db.DateTime, comment='结算日期')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime



class Xiangmu(db.Model):
    __tablename__ = 'xiangmu'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='项目号')
    xiangmu_name = db.Column(db.String(200), nullable=False, comment='项目名称')
    ticheng = db.Column(db.String(200), comment='提成')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime


class Jixiaofangan(db.Model):
    __tablename__ = 'jixiaofangan'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='方案号')
    jine = db.Column(db.String(200), nullable=False, comment='回收金额')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime
    tichengdian = db.Column(db.String(200), comment='提成点')

    xishu = db.Column(db.String(200), comment='系数')


class Bumen(db.Model):
    __tablename__ = 'bumen'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='部门号')
    bumen_name = db.Column(db.String(200), nullable=False, comment='部门名称')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime


class Yuangong(db.Model):
    __tablename__ = 'yuangong'
    id = db.Column(db.BigInteger, primary_key=True, comment='主键')
    gonghao = db.Column(db.String(200), nullable=False, comment='工号')
    name = db.Column(db.String(200), nullable=False, comment='员工名字')
    bumen_name = db.Column(db.String(200), nullable=False, comment='部门名称')
    dixin = db.Column(db.String(200), nullable=False, comment='底薪')
    create_time = db.Column(db.DateTime, comment='创建日期')  # 通常建议使用db.DateTime

# 注意：以上所有模型中的日期和时间字段都使用了db.String类型。
# 在实际应用中，如果你需要处理日期和时间，建议使用db.DateTime类型，如下所示：
# create_time = db.Column(db.DateTime, comment='创建日期')

# 如果你的Flask应用需要这些模型类，确保在创建数据库表之前导入它们。
# 例如，在Flask应用的某个初始化脚本或模块中：
# from your_app.models import db, Neitui, Shebao, Yibao, ...  # 导入所有模型类
# db.create_all()  # 创建所有表