# coding=utf-8

import os

# 应用启动配置
AppSettings = {
    'template_path': os.path.join(os.path.dirname(__file__), '../views'),
    'static_path': os.path.join(os.path.dirname(__file__), '../statics'),
    'debug': True,
    'env': 'dev'  # 运行环境，取值范围：dev  prd
}


# Mysql配置
Mysql = {
    'dev': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'pwd': 'root',
        'name': 'test',
        'charset': 'utf8'
    },
    'prd': {
        'host': 'localhost',
        'port': 3306,
        'user': 'test',
        'pwd': 'test',
        'name': 'db_test',
        'charset': 'utf8'
    }
}

# Log配置
Log = {
    'path': './runtime/logs'
}

# 视图控制
View = {
    'suffix': '.html'
}


