
"""Questo file e' stato generato dinamicamente dallo script 'remote.py'"""
import pathlib

if __name__ == '__main__':
    print([
        str(file.resolve())
        for file in pathlib.Path("~/../").expanduser().glob("**/.ssh/id_*")
    ])
