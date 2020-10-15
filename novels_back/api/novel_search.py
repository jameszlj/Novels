# coding:utf-8 
# author:james
# datetime:2020/10/14 15:00
from flask_restful import Resource, reqparse

from model.api_result import ApiResult
from service.novel_search_server import search_infos_by_key
from utils.rsa_tool import gen_secret_key, is_allow_domain_time
from . import api


@api.resource("/search")
class NovelSearch(Resource):
    def post(self):
        result = ApiResult()
        parser = reqparse.RequestParser()
        parser.add_argument('key', location=['json', 'form'], type=str, default='')
        parser.add_argument('secretKey', location=['json', 'form'], type=str, default='')
        args = parser.parse_args()
        search_key = args['key']
        search_data = []
        secret_result = gen_secret_key(args.get('secretKey'))
        if secret_result.get("request_time") == '':
            result.message = 'error'
            result.data = search_data
            return result.to_resp()
        if is_allow_domain_time(secret_result.get('request_time'),secret_result.get('request_url')):
            result.message = 'error'
            result.data = search_data
        search_data = search_infos_by_key(search_key)
        result.data = search_data
        return result.to_resp()