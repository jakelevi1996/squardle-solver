from squardle_solver import full_path
from squardle_solver.pickle_cache import PickleCache
from squardle_solver.download import DownloadableFile

class WordTree:
    def __init__(self, word_list: list[str]):
        prefix_dict: dict[str, list[str]] = dict()
        leaf_list: list[str] = []
        for word in word_list:
            if len(word) == 1:
                leaf_list.append(word)
            else:
                if word[0] not in prefix_dict:
                    prefix_dict[word[0]] = [word[1:]]
                else:
                    prefix_dict[word[0]].append(word[1:])

        self.subtree_dict = {k: WordTree(v) for k, v in prefix_dict.items()}
        self.leaf_str = "".join(leaf_list)

    def is_leaf(self, c: str):
        return c in self.leaf_str

    def get_subtree(self, c: str):
        return self.subtree_dict.get(c)

class WordTreeCache(PickleCache):
    def __init__(self, word_list: DownloadableFile):
        self.word_list = word_list

    def make(self):
        self.word_list.display_load()
        return WordTree(self.word_list.load())

    def get_path(self) -> str:
        return full_path.get("word_tree_%s.pkl" % self.word_list)
