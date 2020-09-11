from .Config import Config
from .Package import Package

class Manager():

    STATUS_PROCESSING = 'PROCESSING'
    STATUS_READY = 'READY'

    def __init__(self):
        self.status = self.STATUS_READY

    def process(self):
        self.status = self.STATUS_PROCESSING
        for source in Config().get('sources'):
            package = Package(source)
            package.zip()
            package.send()
        self.status = self.STATUS_READY