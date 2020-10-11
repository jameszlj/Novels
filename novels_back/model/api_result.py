import json

from flask import current_app

from model.http_status_codes import HTTP_STATUS_CODES
from config import DEBUG


class ApiResult():
    def __init__(self):
        self.code = 200
        self.data = None
        self.message = ""
        self.headers = dict()
        self.err = None

    def to_resp(self):
        if self.code != 200 and self.data is None:
            self.data = {'msg': HTTP_STATUS_CODES.get(str(self.code), "")}
        if self.data is None:
            self.code = 204
        if self.err is not None:
            self.code = 500
            current_app.logger.error(self.err)
            if DEBUG:
                self.data = {'error_msg': self.err}
            else:
                self.data = {'msg': HTTP_STATUS_CODES.get(str(self.code), "")}
        # return self.data, self.code, self.headers
        if self.err:
            self.code = 0
            if DEBUG:
                self.message = self.err
            else:
                self.message = "error"
        else:
            self.code = 1
        return {'code': self.code, 'message': self.message, 'data': self.data}, 200, self.headers
