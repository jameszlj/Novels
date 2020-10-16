ENV = "DEV"

if ENV == "DEV":
    DEBUG = True
    DB_CONFIG = {
        'host': "localhost",
        'user': "root",
        'passwd': "root",
        'db': "novel",
        'port': 3306,
        'charset': 'utf8'
    }

if ENV == "TEST":
    DEBUG = False
    DB_CONFIG = {
        'host': "mysql-gen",
        'user': "root",
        'passwd': "ROOT",
        'db': "novel",
        'port': 3306,
        'charset': 'utf8'
    }

BOOK_LIST = [
    'xuanhuan',
    'xiuzhen',
    'dushi',
    'lishi',
    'wangyou',
    'kehuan',
    'yanqing',
    'qita',
    'quanben'
]

REQUSET_LISTS = ['www.baidu.com', 'www.mi-novel.com']

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "defult": {
            "format": "%(asctime)s - %(thread)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "defult",
            "stream": "ext://sys.stdout"
        },
        "debug_file_handler": {
            "class": "utils.log_handler.MultiprocessHandler",
            "level": "DEBUG",
            "formatter": "defult",
            "filename": "debug.log",
            "backupCount": 32,
            "encoding": "utf8"
        },
        "info_file_handler": {
            "class": "utils.log_handler.MultiprocessHandler",
            "level": "INFO",
            "formatter": "defult",
            "filename": "info.log",
            "backupCount": 8,
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "utils.log_handler.MultiprocessHandler",
            "level": "ERROR",
            "formatter": "defult",
            "filename": "errors.log",
            "backupCount": 32,
            "encoding": "utf8"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "debug_file_handler", "info_file_handler", "error_file_handler"]
    }
}
