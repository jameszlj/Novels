from os import walk
from os.path import dirname, realpath
from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint("api", __name__)
api = Api(api_bp)
path = dirname(realpath(__file__))
file_list = list()
import_list = list()

for root, dirs, files in walk(path):
    file_list = files
    break

import_module = "from . import %s"

for f in file_list:
    if f != "__init__.py":
        module_name = f[:f.index(".")]
        import_list.append(import_module % module_name)

for import_ in import_list:
    exec(import_)

