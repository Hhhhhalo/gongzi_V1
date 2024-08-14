import json
import os
import random
from datetime import datetime
# import faker

from sqlalchemy import JSON, Column, Integer, String, Text, func, text
from module.__init__ import db


def to_float(val, default=0):
    try:
        return float(val)
    except:
        return default


def to_int(val, default=0):
    try:
        return int(val)
    except:
        return default


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    role = Column(String(255), default="user")
    date = db.Column(db.DateTime, default=datetime.now)


class Record(db.Model):
    """
    监测记录
    """
    __tablename__ = "tb_record"

    id = Column(Integer, primary_key=True)
    position = Column(String(255))   # 监测点位
    jsl = Column(String(255))  # 降水量
    ysl = Column(String(255))    # 涌水量
    sw = Column(String(255))  # 水位
    temp = Column(String(255))  # 水温
    sls = Column(String(255))   # 水流速
    dbcxwy = Column(String(255))   # 地表沉陷位移
    wz = Column(String(255))   # 微震
    date = db.Column(db.DateTime)  # 时间


class Setting(db.Model):
    """
    监测配置
    """
    __tablename__ = "tb_setting"

    id = Column(Integer, primary_key=True)
    jsl = Column(JSON)  # 降水量
    ysl = Column(JSON)  # 涌水量
    sw = Column(JSON)  # 水位
    temp = Column(JSON)  # 水温
    sls = Column(JSON)  # 水流速
    dbcxwy = Column(JSON)  # 地表沉陷位移
    wz = Column(JSON)  # 微震
    date = db.Column(db.DateTime, default=datetime.now)



def init_data():
    """
    初始化数据库数据，把采集到的唐卡信息导入到数据表中
    """
    ret = User.query.filter_by(role="admin").first()
    if not ret:
        user = User()
        user.username = "admin"
        user.password = "admin"
        user.role = "admin"
        db.session.add(user)
        db.session.commit()

