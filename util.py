import os

def readInput(path):
    path = f"{os.path.dirname(__file__)}/{path}"
    with open(path) as file:
        lines = file.readlines()

    return lines