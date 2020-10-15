# coding:utf-8 
# author:james
# datetime:2020/10/15 11:45
import base64
import time

import rsa

from config import REQUSET_LISTS


def gen_secret_key(cryp_data):
    pri_key = rsa.PrivateKey.load_pkcs1(open("rsa_1024_priv.pem",'rb').read())
    msg = rsa.decrypt(base64.b64decode(cryp_data),pri_key)
    try:
        result = {
            'request_time': msg.decode().split(":")[0],
            'request_url': msg.decode().split(":")[1],
            'request_infos': msg.decode().split(":")[2],
        }
    except:
        result = {
            'request_time': '',
            'request_url': '',
            'request_infos': '',
        }
    return result


def is_allow_domain_time(request_time, request_url):

    if int(time.time() * 1000) - int(request_time) > 300000:
        # 一个加密数据只能在3W毫秒之内访问
        return True
    if request_url not in REQUSET_LISTS:
        # 只有指定的域名才能访问

        return True
    return False


