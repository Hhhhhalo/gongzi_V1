from pymysql import *

conn = connect(host='localhost',user='root',password='123456',database='gongzi',port=3306)
cursor = conn.cursor()


def querys(sql,params,type='no_select'):
    params = tuple(params)
    cursor.execute(sql,params)
    conn.ping(reconnect=True)
    if type != 'no_select':
        data_list = cursor.fetchall()
        conn.commit()
        return data_list
    else:
        conn.commit()
        return '数据库语句执行成功'


def connect_to_mysql(host='localhost', user='root', password='123456', database='gongzi', port=3306):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
        else:
            print('Could not connect to MySQL database')
    except Error as e:
        print(f"Error: '{e}'")
    return None


def query_all(sql, params=None, fetch=False):
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        if fetch:
            return cursor.fetchall()
        else:
            conn.commit()
            return 'Database statement executed successfully'
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()