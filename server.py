#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
from application import Application
from tornado.options import options, define


# 定义全局变量，命令参数
define("port", default=8000, help="run on the given port", type=int)
define("host", default='127.0.0.1', help="run on the given host", type=str)


def main():
    tornado.options.parse_command_line()
    application = Application()
    httpServer = tornado.httpserver.HTTPServer(application)
    httpServer.listen(options.port, options.host)

    print("=" * 100)
    print "* Server: Success!"
    print "* Host:   http://" + options.host + ":%s" % options.port
    print "* Quit the server with Control-C"
    print("=" * 100)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
