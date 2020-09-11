import json
import sys
from pathlib import Path
import yaml

class Config:

    class __Config:
        def __init__(self, file_path: str):
            self.config = None
            try:
                with open(file_path, "r") as config_file:
                    if Path(file_path).suffix == '.json':
                        self.config = json.load(config_file)
                    elif Path(file_path).suffix == '.yaml':
                        self.config = yaml.load(config_file, Loader=yaml.FullLoader)
                    else:
                        raise TypeError("config: {} filetype not supported".format(file_path))

            except FileNotFoundError:
                print(file_path + ' configuration file not found')
                sys.exit()

        def __str__(self):
            return repr(self) + str(self.config)

    instance = None

    def __init__(self, file_path: str = ''):
        if not Config.instance:
            Config.instance = Config.__Config(file_path)

    def get(self, key: str):
        if key is None:
            return Config.instance.config
        else:
            return Config.instance.config[key]
