import os
import urllib.request
from jutility import util
from squardle_solver import full_path

class DownloadableFile:
    def __init__(self):
        if not os.path.isfile(self.get_path()):
            self.download()

    def load(self):
        raise NotImplementedError()

    def get_path(self) -> str:
        raise NotImplementedError()

    def get_url(self) -> str:
        raise NotImplementedError()

    def download(self):
        url = self.get_url()
        full_path = self.get_path()
        dir_name  = os.path.dirname(full_path)
        print("Downloading \"%s\" to \"%s\"" % (url, full_path))

        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        with util.Timer("DownloadableFile.download"):
            urllib.request.urlretrieve(url, full_path)

    def __repr__(self):
        return type(self).__name__

class WordsAlpha(DownloadableFile):
    def load(self):
        print("Loading from \"%s\"" % self.get_path())
        return util.load_text(self.get_path()).strip().split("\n")

    def get_path(self):
        return full_path.get("words_alpha.txt")

    def get_url(self):
        return (
            "https://raw.githubusercontent.com/dwyl/english-words/master/"
            "words_alpha.txt"
        )
