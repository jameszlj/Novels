# coding:utf-8 
# author:james
# datetime:2020/10/13 21:54
from config import DB_CONFIG
from utils.mysql_helper import MysqlHelper


def get_book_detail_by_book_id_sort_id(book_id,sort_id):
    result = None
    str_sql = """
        SELECT
            book_id,
            detail_title,
            detail_content
        FROM
            book_details 
        WHERE
            book_id = %s 
            AND sort_id = %s
        """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, [book_id, sort_id])

    return result if result else []


def get_next_cap_id(book_id, sort_id):
    result = None
    str_sql = """
    SELECT
        sort_id
    FROM
        book_details 
    WHERE
        book_id = %s
        AND sort_id > %s
    ORDER BY sort_id 
    LIMIT 1
        """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, [book_id, sort_id])
    return result[0] if result else None


def get_before_cap_id(book_id, sort_id):
    result = None
    str_sql = """
    SELECT
        sort_id
    FROM
        book_details 
    WHERE
        book_id = %s
        AND sort_id < %s
    ORDER BY sort_id DESC
    LIMIT 1
        """
    with MysqlHelper(DB_CONFIG) as mysql:
        result = mysql.exec_query(str_sql, [book_id, sort_id])
    return result[0] if result else None

