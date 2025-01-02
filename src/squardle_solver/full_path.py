import os

def get_data_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(current_dir, "..", "..", "data"))

def get(file_name):
    return os.path.join(get_data_dir(), file_name)
