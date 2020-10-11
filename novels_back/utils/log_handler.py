#-*- coding:utf-8 -*-
import os
import re
import datetime
import logging
import traceback


class MultiprocessHandler(logging.FileHandler):
    def __init__(self, filename, when='D', backupCount=0, encoding=None, delay=False):
        self.prefix = filename
        self.backupCount = backupCount
        self.when = when.upper()
        self.reg_date = r"^\d{4}-\d{2}-\d{2}"

        self.when_dict = {
            'M': "%Y-%m-%d-%H-%M",
            'H': "%Y-%m-%d-%H",
            'D': "%Y-%m-%d"
        }
        self.suffix = self.when_dict.get(when)
        if not self.suffix:
            raise ValueError(u"wrong param [when]: %s" % self.when)
        self.filefmt = os.path.join("logs", "%s.%s" % (self.prefix, self.suffix))
        self.filePath = datetime.datetime.now().strftime(self.filefmt)
        _dir = os.path.dirname(self.filefmt)
        try:
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        except Exception:
            traceback.print_exc()
            print("dir path：" + self.filePath)

        logging.FileHandler.__init__(self, self.filePath, 'a+', encoding, delay)

    def should_change_file_to_write(self):
        _filePath = datetime.datetime.now().strftime(self.filefmt)
        if _filePath != self.filePath:
            self.filePath = _filePath
            return True
        return False

    def change_file(self):
        self.baseFilename = os.path.abspath(self.filePath)
        if self.stream:
            self.stream.close()
            self.stream = None # important!
        if not self.delay:
            self.stream = self._open()
        if self.backupCount > 0:
            for s in self.get_files_to_delete():
                os.remove(s)

    def get_files_to_delete(self):
        dirName, _ = os.path.split(self.baseFilename)
        fileNames = os.listdir(dirName)
        result = []
        prefix = self.prefix + '.'
        plen = len(prefix)
        for fileName in fileNames:
            if fileName[:plen] == prefix:
                suffix = fileName[plen:]
                if re.compile(self.reg_date).match(suffix):
                    result.append(os.path.join(dirName, fileName))
        result.sort()
        if len(result) < self.backupCount:
            result = []
        else:
            result = result[:len(result) - self.backupCount]
        return result

    def emit(self, record):
        try:
            if self.should_change_file_to_write():
                self.change_file()
            logging.FileHandler.emit(self, record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
