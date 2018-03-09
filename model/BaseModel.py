# coding=utf-8
#
# 模型基类
#
from libs.mysql.Dao import Dao


class BaseModel(object):

    def __init__(self, table):
        self.dao = Dao()
        self.table = table

    def insert(self, where, data):
        if where and not where == '':
            self.dao.INSERT(self.table).DATA(data).WHERE(where).EXEC()
        else:
            self.dao.INSERT(self.table).DATA(data).EXEC()
        return self.dao.last_id

    def update(self, where, data):
        self.dao.UPDATE(self.table).DATA(data).WHERE(where).EXEC()
        return self.dao.affect_rows

    def delete(self, where):
        self.dao.DELETE().FROM(self.table).WHERE(where).EXEC()
        return self.dao.affect_rows

    def select(self, fields, where):
        return self.dao.SELECT(fields).FROM(self.table).WHERE(where).EXEC().FETCHALL()

    def selectOne(self, fields, where):
        return self.dao.SELECT(fields).FROM(self.table).WHERE(where).EXEC().FETCH()

    def count(self, where):
        res = self.dao.SELECT('count(*) as count').FROM(self.table).WHERE(where).EXEC().FETCH()
        return res['count']

    def _count(self, table, where):
        res = self.dao.SELECT("count(*) as count").FROM(table).WHERE(where).EXEC().FETCH()
        return res['count']