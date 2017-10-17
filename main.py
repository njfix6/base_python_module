import os, sys, shutil, git, argparse, chalk, json, re, pprint, json
from pathlib import Path
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def root_path(path):
    return os.path.join(ROOT_PATH, path)

def main(argv):
    parser = argparse.ArgumentParser()

if __name__ == "__main__":
    main(sys.argv)
