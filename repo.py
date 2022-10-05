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

        if not(force or os.path.isdir(self.gitdir)):
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
