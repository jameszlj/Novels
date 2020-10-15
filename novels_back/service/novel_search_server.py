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
        WHERE
            book_name = %s OR book_author = %s 
    """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, [search_key, search_key])

    return result if result else []