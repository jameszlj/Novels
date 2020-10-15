# coding:utf-8 
# author:james
# datetime:2020/10/13 10:32
from flask_restful import Resource, reqparse

from model.api_result import ApiResult
from service.novel_idx_server import get_book_caps_by_book_id, get_book_infos_by_book_id
from . import api


@api.resource("/novel/<int:book_id>")
class NovelIndex(Resource):
    def post(self, book_id):
        result = ApiResult()
        parser = reqparse.RequestParser()
        parser.add_argument('key', location=['json', 'form'], type=str, default='')
        parser.add_argument('secretKey', location=['json', 'form'], type=str, default='')
        args = parser.parse_args()
        idx_data = []
        if args.get("key") == "index":
            idx_data = get_book_infos_by_book_id(book_id)
        elif args.get("key") == "cap20":
            idx_data = get_book_caps_by_book_id(book_id, limit=20)
        elif args.get("key") == "all":
            idx_data = get_book_caps_by_book_id(book_id)
        else:
            result.message = "error"
        result.data = idx_data
        return result.to_resp()
