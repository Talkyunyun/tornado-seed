# coding=utf-8


from url import url
from config import Config

import tornado.web


class Application(tornado.web.Application):
    def __init__(self):

        handlers = url
        settings = {
            'template_path': Config.AppSettings['template_path'],
            'static_path': Config.AppSettings['static_path'],
            'debug': Config.AppSettings['debug'],
            'autoreload': True
        }

        tornado.web.Application.__init__(self, handlers, **settings)
