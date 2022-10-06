import argparse
import collections
import hashlib
import os
import re
import sys
import zlib
from repo import Repo
from utils import *


def cmd_init(args):
    r = Repo(path=args.path, force=True)
    r.create()
    print(f"Init repo in {args.path}")


argparser = argparse.ArgumentParser()
argsubparsers = argparser.add_subparsers(
    title="Commands",
    dest="command"
)
argsubparsers.required = True
argsp = argsubparsers.add_parser(
    "init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")


def main(argv=sys.argv[1:]):

    args = argparser.parse_args(argv)
    if(args.command == "init"):
        cmd_init(args)


main()
