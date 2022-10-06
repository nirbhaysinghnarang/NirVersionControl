import argparse
import collections
import hashlib
import os
import re
import sys
import zlib
from repo import Repo
from utils import *


r = Repo(path="/Users/nirbhaysingh/new/", force=True)
r.create()
