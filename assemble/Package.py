import subprocess
import time
import glob
import os

from typing import List

from .Config import Config
from .Logger import Logger
from .File import File

class Package():

    def __init__(self, source: dict):
        self.zipped = False
        self.sent = False
        self.source = source
        self.files = []

        for filepath in glob.glob(self.source['path']):
            file = File(filepath)
            self.files.append(file)

    def zip(self):
        #files_str = ' '.join([f.filepath for f in self.files])

        with open(Config().get('unpackaged_files_path'), 'a') as file_list:
            for file in self.files:
                file_list.write("{}\n".format(file.filepath))

        self.filepath = Config().get('dest') + '-'.join([Config().get('node_id'),self.source['name'],str(time.time())])

        cmd = "tar -cvzf {} -T {}".format(
            self.filepath,
            Config().get('unpackaged_files_path')
        )

        Logger().info(cmd)
        zip_process = subprocess.getoutput(cmd)
        Logger().info(zip_process)

        os.remove(Config().get('unpackaged_files_path'))

        self.zipped = True

    def send(self):
        if self.zipped == False:
            Logger().info('could not send, package is not zipped')
            return

        cmd = "scp -i {} -P {} {} {}@{}:{}".format(
            Config().get('user')['key'],
            Config().get('user')['port'],
            self.filepath,
            Config().get('user')['name'],
            Config().get('user')['host'],
            Config().get('user')['dest']
        )

        Logger().info(cmd)
        scp_process = subprocess.getoutput(cmd)
        Logger().info(scp_process)

        os.remove(self.filepath)

        self.sent = True
