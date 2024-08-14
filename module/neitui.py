import json
import os
import random
from datetime import datetime
# import faker

from sqlalchemy import JSON, Column, Integer, String, Text, func, text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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


class Neitui(db.Model):
    """
    内推表
    """
    __tablename__ = "neitui"

    id = Column(Integer, primary_key=True)
    neitui_name = Column(String(255))
    be_neitui_name = Column(String(255))
    ruzhi_time = Column(String(255))
    or_pass = Column(String(255))
    fenzu = Column(String(255))
    yuefen = Column(String(255))
    jiangli = Column(String(255))
    daxiang = Column(String(255))

