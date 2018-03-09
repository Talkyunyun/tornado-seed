#!/usr/bin/env python
# coding=utf-8

from handlers.BaseHandler import BaseHandler
from model.Zone import Zone
from libs.Log import Logger


class IndexHandler(BaseHandler):

    # 接收get请求
    def get(self):

        return self.renderView('index', name='Gene')

    # mysql数据库操作案例
    def mysqlDemo(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        result = Zone().selectOne('zone_id, zone_title', 'zone_id=1')

        # json格式响应
        return self.resJson('请求成功', result)

    # 视图渲染案例
    def viewDemo(self):

        return self.renderView('index', name='Gene')

    # 日志操作案例
    def logDemo(self):
        Logger().run('run').info("我会写入run.log日志文件中")





    # 接收post请求
    def post(self, *args, **kwargs):
        name = self.get_argument('name')

        self.write(name)
