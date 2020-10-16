#-*- coding:utf-8 -*-
import os
import uuid
import json
import logging.config
from flask import Flask, request
from flask_cors import CORS
from api import api_bp
from config import DEBUG, LOG_CONFIG


logging.config.dictConfig(LOG_CONFIG)

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())[0:7]
app.register_blueprint(api_bp, url_prefix="/api")
app.debug = DEBUG
# app.debug = False
CORS(app, supports_credentials=True)


@app.route('/favicon.ico')
def get_fav():
    return app.send_static_file('static/favicon.ico')

@app.before_request
def request_interceptor():
    # return None 直接放行
    print(request.path, request.remote_addr)
    request.path = "/api/test2"
    return None

@app.after_request
def response_interceptor(resp):
    # print(dir(resp))
    # print(json.loads(str(resp.data, encoding="utf-8")))
    # print(request.path, request.remote_addr)
    return resp


if __name__ == "__main__":
    print("-----")
    app.run(host="0.0.0.0", port=8080)
