import os
import urllib.request
from jutility import util

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
        print("Downloading \"%s\" from \"%s\"" % (full_path, url))
        with util.Timer("download"):
            urllib.request.urlretrieve(url, full_path)

class WordsAlpha(DownloadableFile):
    def load(self):
        return util.load_text(self.get_path()).strip().split("\n")

    def get_path(self):
        return "words_alpha.txt"

    def get_url(self):
        return (
            "https://raw.githubusercontent.com/dwyl/english-words/master/"
            "words_alpha.txt"
        )