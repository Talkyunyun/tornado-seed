# coding=utf-8
#
# 数据库操作类，定义基本操作
#

import MySQLdb
from libs.mysql.Db import Db


class Dao:
    def __init__(self):
        self.table = ''
        self.action = ''
        self.error = None
        self.data = {}
        self.sql = ''
        self.affect_rows = 0
        self.last_id = -1
        self.conn = None
        self.cur = None

    def DATA(self, data):

        if self.action.lower() == 'insert' and isinstance(data,dict):
            values = self.__value_fomart_list(data.values())
            keys =  self.__key_fomart_list(data.keys())
            self.sql += ' (%s) values (%s)' % (",".join(keys),",".join(values))
        elif self.action.lower() == 'update' and isinstance(data,dict):
            values = []
            for k,v in data.items():
                values.append("%s=%s" % (self.__key_fomart(k),self.__value_fomart(v)))
            self.sql += ' SET %s' % ','.join(values)

        else:
            self.sql += data

        return self

    def SELECT(self, fields='*'):
        self.action = 'SELECT'

        if isinstance(fields,list):
            self.sql = '%s %s' % (self.action,",".join(fields))
        else:
            self.sql = '%s %s' % (self.action,fields)
        return self

    def INSERT(self, table):
        self.action = 'INSERT'
        self.table = table
        self.sql = '%s INTO %s' % (self.action,self.table)
        return self

    def UPDATE(self, table):
        self.action = 'UPDATE'
        self.table = table
        self.sql = '%s %s' % (self.action,self.table)
        return self

    def DELETE(self):
        self.action = 'DELETE'
        self.sql = '%s' % self.action
        return self

    def FROM(self, table):
        self.table = table
        self.sql += ' FROM %s' % self.table
        return self

    def WHERE(self, field):
        self.sql += " WHERE %s" % self.__key_fomart(field)
        return self

    def AND_WHERE(self, field):
        self.sql += " AND %s" % self.__key_fomart(field)
        return self

    def EQ(self,value):
        self.sql += " =%s" % self.__value_fomart(value)
        return self

    def NEQ(self,value):
        self.sql += " !=%s" % self.__value_fomart(value)
        return self

    def LT(self,value):
        self.sql += " <%s" % self.__value_fomart(value)
        return self

    def LTE(self,value):
        self.sql += " <=%s" % self.__value_fomart(value)
        return self

    def GT(self,value):
        self.sql += " >%s" % self.__value_fomart(value)
        return self

    def GTE(self,value):
        self.sql += " >=%s" % self.__value_fomart(value)
        return self

    def IN(self,values):
        values = self.__value_fomart_list(values)
        self.sql += " IN (%s)" % ",".join(values)
        return self

    def LIKE(self,like):
        self.sql += " LIKE %s" % self.__key_fomart(like)
        return self

    def LIMIT(self,limit):
        self.sql += " LIMIT %s" % str(limit)
        return self

    def OFFSET(self,offset):
        self.sql += " OFFSET %s" % str(offset)
        return self

    def GROUP_BY(self,field):
        self.sql += " GROUP BY %s" % self.__key_fomart(field)
        return self

    def ORDER_BY(self,field):
        self.sql += " ORDER BY %s" % self.__key_fomart(field)
        return self

    def ASC(self):
        self.sql += " ASC"
        return self

    def DESC(self):
        self.sql += " DESC"
        return self

    def __key_fomart(self,key):
        if type(key) == unicode:
            key = key.encode('utf-8')
        return key

    def __key_fomart_list(self,keys):
        new = []
        for k in keys:
            new.append(self.__key_fomart(k))
        return new

    def __value_fomart(self,value):
        if type(value) == unicode:
            value = value.encode('utf-8')

        if type(value) == str:
            result = '\'%s\'' % MySQLdb.escape_string(value)
        elif type(value) == float:
            result = value
        elif type(value) == bool:
            result = 'true' if value else 'false'
        elif type(value) == int:
            result = str(value)
        elif type(value) == long:
            result = str(value)
        else:
            result = value
        return result

    def __value_fomart_list(self,values):
        new = []
        for v in values:
            new.append(self.__value_fomart(v))
        return new

    def __close(self):
        try:
            if self.cur:
                self.cur.close()
            Db().getConnect().release()
        except Exception as e:
            print e

    def EXEC(self):
        try:
            self.conn = Db().getConnect()

            self.cur = self.conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            self.affect_rows = self.cur.execute(self.sql)

            if self.action.lower()!= 'select':
                self.conn.commit()

            if self.action.lower() == 'insert':
                self.last_id = self.cur.lastrowid

        except Exception as e:
            self.error = str(e)
            print e
        finally:
            if self.action.lower()!= 'select':
                self.__close()
            return self

    def FETCH(self):
        try:
            if not self.cur:
                self.EXEC()
            res = self.cur.fetchone()
            return res
        except Exception as e:
            self.error = str(e)
            print e
        finally:
            self.__close()

    def FETCHALL(self):
        try:
            if not self.cur:
                self.EXEC()
            res = self.cur.fetchall()
            return res
        except Exception as e:
            self.error = str(e)
            print e
        finally:
            self.__close()
