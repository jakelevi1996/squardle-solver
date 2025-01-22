import os
import urllib.request
from jutility import util
from squardle_solver import full_path, download

class WordList(download.DownloadableFile):
    def load(self):
        return util.load_text(self.get_path()).strip().split("\n")

class WordsAlpha(WordList):
    def get_path(self):
        return full_path.get("words_alpha.txt")

    def get_url(self):
        return (
            "https://raw.githubusercontent.com/dwyl/english-words/master/"
            "words_alpha.txt"
        )

class NorvigNgrams(WordList):
    def get_path(self):
        return full_path.get("norvig_ngrams.txt")

    def get_url(self):
        return (
            "https://norvig.com/ngrams/enable1.txt"
        )

class Nwl(WordList):
    def load(self):
        return [
            s.split(" ")[0].lower()
            for s in util.load_text(self.get_path()).strip().split("\n")
        ]

class Nwl2020(Nwl):
    def get_path(self):
        return full_path.get("NWL2020.txt")

    def get_url(self):
        return (
            "https://raw.githubusercontent.com/scrabblewords/scrabblewords/"
            "main/words/North-American/NWL2020.txt"
        )

class Nwl2023(Nwl):
    def get_path(self):
        return full_path.get("NWL2023.txt")

    def get_url(self):
        return (
            "https://raw.githubusercontent.com/scrabblewords/scrabblewords/"
            "main/words/North-American/NWL2023.txt"
        )
