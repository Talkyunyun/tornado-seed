# coding=utf-8
#
#
# 日志操作类，使用案例
# from libs.Log import Logger
# Logger().run("日志文件名").info("日志内容")
#
#

import logging, os
from logging.handlers import TimedRotatingFileHandler
from config.Config import Log


class Logger(object):
    __path = None  # 日志保存路径
    __logger = None  # logging日志操作对象

    def __init__(self):
        # 判断是否配置日志路径，没有使用默认
        if Log.has_key('path') is False:
            Log['path'] = './runtime/logs'

        # 判断日志路径是否存在，不存在创建
        if not os.path.exists(Log['path']) is True:
            os.makedirs(Log['path'])

        # 设置日志保存路径
        self.__path = Log['path']

    # 设置日志文件名称，并返回日志操作对象
    def run(self, name):
        # 创建实例
        self.__logger = logging.getLogger(name)
        # 设置日志级别
        self.__logger.setLevel(logging.DEBUG)

        #
        fileName = "%s.log" % (name)
        logPath = os.path.join(self.__path, fileName)

        handler = TimedRotatingFileHandler(logPath, when='d', interval=1, backupCount=7)
        handler.setLevel(logging.DEBUG)

        # 设置日志内容格式
        fmt = "%(asctime)s %(levelname)s %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)

        # 添加格式内容和句柄
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)

        return self.__logger
