import time

from .Config import Config
from .Logger import Logger

class Application:

    def __init__(self):
        Config('../config.yaml')
        Logger(Config().get('log'))

    def run(self):
        while True:
            Logger().info('PROCESS STARTED')
            manager = Manager()
            manager.process()
            Logger().info('PROCESS ENDED')
            time.sleep(Config().get('interval'))
