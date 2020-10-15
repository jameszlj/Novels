# coding:utf-8 
# author:james
# datetime:2020/10/14 15:08
from config import DB_CONFIG
from utils.mysql_helper import MysqlHelper


def search_infos_by_key(search_key):
    result = None
    str_sql = """
        SELECT
            id,
            book_id,
            book_name,
            book_author,
            book_newest_url,
            book_newest_name 
        FROM
            book_infos 
    """.format(search_key,search_key)
    sql_array = list()
    params = list()
    sql_array.append(str_sql)
    if search_key:
        sql_array.append("WHERE book_name LIKE %s")
        sql_array.append("OR book_author LIKE %s")
        params.append('%' + search_key + '%')
        params.append('%' + search_key + '%')
        with MysqlHelper(DB_CONFIG) as mysql:
            result = mysql.exec_query(' '.join(sql_array), params)

    return result if result else []