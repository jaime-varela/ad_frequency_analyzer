import sys
import os

def listFiles(dir):
    return [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

def listDirs(dir):
    return [f for f in os.listdir(dir) if not os.path.isfile(os.path.join(dir, f))]
