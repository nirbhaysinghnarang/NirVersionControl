import os
import configparser
from utils import *


class Repo(object):
    """
    Represents a repository.
    """

    workingTree = None
    directory = None
    config = None

    def __init__(self, path, force=False):
        """
        Creates a new repository.
        """
        self.workingTree = path
        self.directory = os.path.join(path, ".git")
        if not(force or os.path.isdir(self.directory)):
            raise Exception("Invalid directory.")
        # use configparser.ConfigParser() to read config gile in ./git/config
        self.config = configparser.ConfigParser()
        configFile = repo_file(self, "config")
        if configFile and os.path.exists(configFile):
            self.config.read([configFile])
        elif not force:
            raise Exception("Configuration file missing")
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception(
                    "Unsupported repositoryformatversion %s" % vers)

    def create(self):
        """
        Creates a repository at a path.
        Creating a repository entails:
            (1): creating .git dir
            (2): creating .git/objects dir
            (3): creating .git/refs/heads and .git/refs/tags
            (4): creating .git/HEAD file
            (5): creating .git/config file
            (6): creating .git/description file
        """
        # Check if path is valid

        if(os.path.exists(self.workingTree)):
            if not os.path.isdir(self.workingTree):
                raise Exception("%s is not a directory!" % self.workingTree)
        try:
            if os.listdir(self.workingTree):
                raise Exception("%s is not empty!" % self.workingTree)
            else:
                os.makedirs(self.directory)
        except:
            try:
                os.makedirs(self.directory)
            except:
                print(f"{self.workingTree} is already a repository.")
        # create sub dirs
        assert(repo_dir(self, "branches", mkDir=True))
        assert(repo_dir(self, "objects", mkDir=True))
        assert(repo_dir(self, "refs", "tags", mkDir=True))
        assert(repo_dir(self, "refs", "heads", mkDir=True))
        # create file

        with open(repo_file(self, "description"), "w") as f:
            f.write(
                "Unnamed repository; edit this file 'description' to name the repository.\n")
        # .git/HEAD
        with open(repo_file(self, "HEAD"), "w") as f:
            f.write("ref: refs/heads/master\n")

        with open(repo_file(self, "config"), "w") as f:
            config = repo_default_config()
            config.write(f)
