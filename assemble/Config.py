import json

class Config:

    class __Config:
        def __init__(self, file_path: str):
            self.config = None
            try:
                with open(file_path, "r") as read_file:
                    self.config = json.load(read_file)
            except FileNotFoundError:
                print(file_path + ' configuration file not found')
                exit()

        def __str__(self):
            return repr(self) + str(self.config)

    instance = None

    def __init__(self, file_path: str  = ''):
        if not Config.instance:
            Config.instance = Config.__Config(file_path)

    def get(self, key: str):
        if key is None:
            return Config.instance.config
        else:
            return Config.instance.config[key]
