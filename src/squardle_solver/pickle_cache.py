import os
import pickle
from jutility import util

class PickleCache:
    def load(self):
        full_path = self.get_path()

        if not os.path.isfile(full_path):
            print("> Making \"%s\"" % full_path)
            with util.Timer("PickleCache.make"):
                data = self.make()

            print("> Saving \"%s\"" % full_path)
            with util.Timer("PickleCache.save"):
                dir_name  = os.path.dirname(full_path)
                if not os.path.isdir(dir_name):
                    os.makedirs(dir_name)
                with open(full_path, "wb") as f:
                    pickle.dump(data, f)
        else:
            print("> Loading from \"%s\"" % full_path)
            with util.Timer("PickleCache.load"):
                data = util.load_pickle(full_path)

        return data

    def make(self):
        raise NotImplementedError()

    def get_path(self) -> str:
        raise NotImplementedError()
