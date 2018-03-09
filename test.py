#!/usr/bin/env python
# coding=utf-8


import sys, getopt


# 处理命令行参数
try:
    opts, args = getopt.getopt(sys.argv[1:], 'Hh:p:e', ['help', 'host=', 'port=', 'env='])
except getopt.GetoptError:
    exit("\033[1;31;40m Invalid input parameters\033[0m")

for name, value in opts:
    if name in ("-h", "--host"):
        HOST = value
    elif name in ("-p", "--port"):
        PORT = value
    elif name in ("-e", "--env"):
        ENV = value
    else:
        exit("")
