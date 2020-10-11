# -*- coding: utf-8 -*-
import pymysql
from traceback import format_exc


class DBOperateException(Exception):
    pass


class DBConnectException(Exception):
    pass


class MysqlHelper(object):
    def __init__(self, DBCONFIG):
        self.dbconfig = DBCONFIG
        self.__cur = None
        self.__conn = None

    def __enter__(self):
        try:
            if not self.dbconfig:
                raise DBConnectException("not set database connection info")
            self.__connect_database()
        except Exception:
            raise
        return self

    def __exit__(self, type, value, trace):
        if isinstance(value, Exception):
            self.roll_back()
            self.__close_db()
            raise value
        else:
            self.commit()
            self.__close_db()

    def __close_db(self):
        if isinstance(self.__conn, pymysql.connections.Connection):
            self.__conn.close()

    def __connect_database(self):
        try:
            self.__conn = pymysql.connect(
                host=self.dbconfig['host'],
                port=self.dbconfig['port'],
                user=self.dbconfig['user'],
                passwd=self.dbconfig['passwd'],
                db=self.dbconfig['db'],
                charset=self.dbconfig['charset']
            )
            self.__cur = self.__conn.cursor(pymysql.cursors.DictCursor)
        except DBConnectException:
            raise

    def __handle_sql_str_and_para(self, sql, para=[]):
        exec_sql = sql
        exec_para = []
        if isinstance(para, dict):
            exec_para = list(para.values())
        elif not isinstance(para, list):
            exec_para = list(para)
        else:
            exec_para = para
        return exec_sql, exec_para

    def exec_query(self, sql, para=[]):
        exec_sql, exec_para = self.__handle_sql_str_and_para(sql, para)
        try:
            self.__cur.execute(exec_sql, exec_para)
            data = self.__cur.fetchall()
            return data
        except Exception as e:
            raise DBOperateException("exec error[{}] sql: {}, para: {}".format(
                str(e), exec_sql, str(exec_para)))

    def commit(self):
        try:
            if isinstance(self.__conn, pymysql.connections.Connection):
                self.__conn.commit()
        except Exception:
            raise DBOperateException("commit faild", format_exc())

    def roll_back(self):
        if isinstance(self.__conn, pymysql.connections.Connection):
            self.__conn.rollback()

    @property
    def connected(self):
        if self.__conn and self.__conn._conn:
            return self.__conn._conn.connected
        else:
            return False

    def change_db(self, dbname):
        try:
            self.__db = dbname
            self.__conn._conn.select_db(dbname)
            self.__cur = self.__conn.cursor()
            return True
        except DBConnectException:
            return False
