import os

class File():

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename, self._extension = os.path.splitext(self.filepath)

    @property
    def filepath(self):
        return self.__filepath

    @filepath.setter
    def filepath(self, filepath):
        self.__filepath = filepath

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        self.__filename = filename
