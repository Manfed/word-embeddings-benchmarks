import os


def get_full_path():
    path = os.path.abspath(__file__)
    return os.path.dirname(path)
