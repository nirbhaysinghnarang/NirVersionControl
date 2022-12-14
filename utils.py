import os
import configparser

"""
Utility functions for paths, files, and the like.
"""


def repo_path(repo, *path):
    """
    Returns path under repository's Git directory.
    """
    return os.path.join(repo.directory, *path)


def repo_file(repo, *path, mkDir=False):
    """
    Return and optionally create a path to a file.
    """
    if repo_dir(repo, *path[:-1], mkDir=mkDir):
        return repo_path(repo, *path)


def repo_dir(repo, *path, mkDir=False):
    """
    Return and optionally create a path to a directory.
    """
    path = repo_path(
        repo,
        *path
    )
    if(os.path.exists(path)):
        if(os.path.isdir(path)):
            return path
        raise Exception("Not a directory")
    if mkDir:
        os.makedirs(path)
        return path
    return None


def repo_default_config():
    """
    Create default config for a repository.
    """
    ret = configparser.ConfigParser()

    ret.add_section("core")
    ret.set("core", "repositoryformatversion", "0")
    ret.set("core", "filemode", "false")
    ret.set("core", "bare", "false")

    return ret
