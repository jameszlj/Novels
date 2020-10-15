# coding:utf-8 
# author:james
# datetime:2020/10/11 13:09
from flask_restful import Resource, reqparse

from config import BOOK_LIST
from model.api_result import ApiResult
from service.novel_cate_server import get_cate_newst_books_30, get_cate_most_books_30
from . import api


@api.resource("/novel_cate")
class NovelCate(Resource):
    def get(self):
        result = ApiResult()

        data = [
            {"id": 0, "text": '首页', "url": '/'},
            {"id": 1, "text": '玄幻', "url": '/xuanhuan'},
            {"id": 2, "text": '修真', "url": '/xiuzhen'},
            {"id": 3, "text": '都市', "url": '/dushi'},
            {"id": 4, "text": '历史', "url": '/lishi'},
            {"id": 5, "text": '网游', "url": '/wangyou'},
            {"id": 6, "text": '科幻', "url": '/kehuan'},
            {"id": 7, "text": '言情', "url": '/yanqing'},
            {"id": 8, "text": '其他', "url": '/qita'},
            {"id": 9, "text": '完本', "url": '/quanben'},
        ]
        result.data = data

        return result.to_resp()


@api.resource("/<string:novel_cate>")
class NovelInfo(Resource):
    def post(self, novel_cate):
        result = ApiResult()
        parser = reqparse.RequestParser()
        parser.add_argument('key', location=['json', 'form'], type=str, default='')
        parser.add_argument('secretKey', location=['json', 'form'], type=str, default='')
        args = parser.parse_args()
        cate_data = []
        if novel_cate in BOOK_LIST:
            if args.get("key") == "newest":
                cate_data = get_cate_newst_books_30(novel_cate)
            elif args.get("key") == "most":
                cate_data = get_cate_most_books_30(novel_cate)
            else:
                result.message = "error"
        else:
            result.message = 'error'
        result.data = cate_data
        return result.to_resp()
