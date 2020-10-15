# coding:utf-8 
# author:james
# datetime:2020/10/13 21:43
from flask_restful import Resource, reqparse

from model.api_result import ApiResult
from service.novel_detail_server import get_book_detail_by_book_id_sort_id, get_next_cap_id, get_before_cap_id
from service.novel_idx_server import get_book_infos_by_book_id
from utils.rsa_tool import gen_secret_key, is_allow_domain_time
from . import api


@api.resource("/novel/<int:book_id>/<int:sort_id>")
class NovelDetail(Resource):
    def post(self,book_id,sort_id):
        result = ApiResult()
        parser = reqparse.RequestParser()
        parser.add_argument('key', location=['json', 'form'], type=str, default='')
        parser.add_argument('secretKey', location=['json', 'form'], type=str, default='')
        args = parser.parse_args()
        secret_result = gen_secret_key(args.get('secretKey'))
        if secret_result.get("request_time") == '':
            result.message = 'error'
            result.data = []
            return result.to_resp()
        if is_allow_domain_time(secret_result.get('request_time'),secret_result.get('request_url')):
            result.message = 'error'
            result.data = []
            return result.to_resp()
        is_exist_book = get_book_infos_by_book_id(book_id)
        detail_data = []
        if len(is_exist_book) > 0:
            detail_data = get_book_detail_by_book_id_sort_id(book_id, sort_id)
            next_data = get_next_cap_id(book_id,sort_id)
            if next_data is None:
                detail_data[0]['next_sort_id'] = ""
            else:
                detail_data[0]['next_sort_id'] = next_data['sort_id']
            before_data = get_before_cap_id(book_id,sort_id)
            if before_data is None:
                detail_data[0]['before_sort_id'] = ""
            else:
                detail_data[0]['before_sort_id'] = before_data['sort_id']
            detail_data[0]['book_name'] = is_exist_book[0]['book_name']
        else:
            result.message = "error"
        result.data = detail_data
        return result.to_resp()