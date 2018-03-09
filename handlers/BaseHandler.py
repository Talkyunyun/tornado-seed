# coding=utf-8


import tornado.web
from config.Config import View


class BaseHandler(tornado.web.RequestHandler):

    # 响应json格式数据
    def resJson(self, msg='', data=[], code=10005):
        result = {
            'code': code,
            'msg': msg,
            'data': data
        }

        return self.finish(result)

    # 渲染页面模板，默认那当前调用者的前缀作为前置路径
    def renderView(self, template_name, **kwargs):
        currentName = (self.__class__.__name__)[0:-7]

        return self.render(currentName.lower() + '/' + template_name.lower() + View['suffix'], **kwargs)
