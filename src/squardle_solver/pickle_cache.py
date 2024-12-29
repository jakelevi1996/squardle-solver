import os
import pickle
from jutility import util

class PickleCache:
    def load(self):
        full_path = self.get_path()
        dir_name  = os.path.dirname(full_path)
        print("Loading from \"%s\"" % full_path)

        if not os.path.isfile(full_path):
            with util.Timer("make"):
                data = self.make()
            if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
            with open(full_path, "wb") as f:
                pickle.dump(data, f)

            return data
        else:
            return util.load_pickle(full_path)

    def make(self):
        raise NotImplementedError()

    def get_path(self) -> str:
        raise NotImplementedError()
