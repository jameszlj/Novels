import json
import functools
from flask import session, current_app
from model.api_result import ApiResult


def login_required(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        is_login = session.get('is_login')
        if is_login:
            return func(*args, **kwargs)
        else:
            result = ApiResult()
            result.code = 401
            return result.to_resp()
    return inner
