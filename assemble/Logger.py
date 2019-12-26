
import logging

class Logger:

    class __Logger:
        def __init__(self, file_path: str):
            self.logger = logging.getLogger('aware-assemble')
            log = logging.FileHandler(file_path)
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            log.setFormatter(formatter)
            self.logger.addHandler(log) 
            self.logger.setLevel(logging.INFO)

    instance = None

    def __init__(self, file_path: str = ''):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(file_path)

    def info(self, msg: str):
        return Logger.instance.logger.info(msg)

    def error(self, msg: str):
        return Logger.instance.logger.error(msg)

    def debug(self, msg: str):
        return Logger.instance.logger.debug(msg)
