# coding:utf-8 
# author:james
# datetime:2020/10/13 11:41
from config import DB_CONFIG
from utils.mysql_helper import MysqlHelper


def get_book_infos_by_book_id(book_id):
    result = None
    str_sql = """
    SELECT
        book_id,
        book_name,
        book_author,
        book_newest_name,
        DATE_FORMAT(book_last_update_time,%s) as book_last_update_time,
        book_status,
        image_paths,
        image_urls,
        book_desc
    FROM
        book_infos 
    WHERE
        book_id = %s
    """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, ['%Y-%m-%d %H:%i:%S', book_id])

    return result if result else []


def get_book_caps_by_book_id(book_id, limit=None):
    result = None
    str_sql = """
        SELECT
            id,
            book_id,
            sort_id,
            detail_title 
        FROM
            book_details 
        WHERE
            book_id = %s 
        ORDER BY
            sort_id DESC 
    """
    if limit:
        str_sql += f" LIMIT {int(limit)}"
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, [book_id,])

    return result if result else []



