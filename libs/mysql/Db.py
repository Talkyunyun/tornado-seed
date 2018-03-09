# coding=utf-8
#
# MySQL数据库连接类
#
import MySQLdb
from config import Config

mySqlConfig = Config.Mysql
appConfig = Config.AppSettings


class Db:
    __db = None

    # 初始化Mysql连接对象
    def __init__(self):

        self.__db = MySQLdb.connect(
            mySqlConfig[appConfig['env']]['host'],
            mySqlConfig[appConfig['env']]['user'],
            mySqlConfig[appConfig['env']]['pwd'],
            mySqlConfig[appConfig['env']]['name'],
            charset=mySqlConfig[appConfig['env']]['charset']
        )

    # 获取Mysql连接对象
    def getConnect(self):
        return self.__db
