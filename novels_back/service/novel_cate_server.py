# coding:utf-8 
# author:james
# datetime:2020/10/12 14:23
from config import DB_CONFIG
from utils.mysql_helper import MysqlHelper


def get_cate_newst_books_30(novel_cate):
    result = None
    str_sql = """
    SELECT
        id,
        book_name,
        book_id,
        date_format(book_last_update_time, %s ) as book_last_update_time,
        book_newest_name,
        book_newest_url 
    FROM
        book_infos 
    WHERE
        book_cate = %s 
    ORDER BY
        book_last_update_time DESC 
        LIMIT 30;
    """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, ['%Y-%m-%d %H:%i:%S',novel_cate,])

    return result if result else []


def get_cate_most_books_30(novel_cate):
    result = None
    str_sql = """
    SELECT
        id,
        book_id,
        book_name,
        book_author,
        book_newest_url 
    FROM
        book_infos 
    WHERE
        book_cate = %s 
    ORDER BY
        book_newest_url DESC 
        LIMIT 30;
    """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, [novel_cate,])

    return result if result else []


def get_new_books_top_5():
    result = None
    str_sql = """
        SELECT
            book_id,
            book_name,
            image_urls	
        FROM
            book_infos 
        ORDER BY
            book_last_update_time DESC 
            LIMIT 5
    """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql)

    return result if result else []