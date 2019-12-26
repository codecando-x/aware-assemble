import time

from assemble import Config
from assemble import Logger
from assemble import Manager

Config('config.json')
Logger(Config().get('log'))

while True:
    Logger().info('PROCESS STARTED')
    manager = Manager()
    manager.process()
    Logger().info('PROCESS ENDED')
    time.sleep(Config().get('interval'))
