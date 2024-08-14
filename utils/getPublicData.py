import json
from utils.query import querys
import pandas as pd
import re
import sys
sys.path.append('model')
# def fetch_data_by_month(table_name, month):
#     """
#     从指定表中按月份提取数据
#     :param db_path: 数据库文件路径
#     :param table_name: 表名
#     :param month: 要查询的月份，格式为'YYYY-MM'
#     :return: 查询结果的列表
#     """
#
#     # 构造查询SQL，这里假设每个表都有一个名为create_time的日期字段
#     allData =querys( f"SELECT * FROM {table_name} WHERE strftime('%Y-%m', create_time) = ?"  ,[],'select')
#
#     return allData


def fetch_data_by_month( table_name, month):
    """
    从指定MySQL表中按月份提取数据
    :param conn: MySQL数据库连接对象
    :param table_name: 表名
    :param month: 要查询的月份，格式为'YYYY-MM'
    :return: 查询结果的列表
    """
    sql = f"SELECT * FROM {table_name} WHERE YEAR(create_time) = %s AND MONTH(create_time) = %s"
    params = (int(month.split('-')[0]), int(month.split('-')[1]))
    return querys( sql, params, type=True)


def getBumenData():
    allData = querys('select * from bumen',[],'select')
    return allData



# if __name__ == '__main__':
#     print(fetch_data_by_month("bumen","2023-04"))