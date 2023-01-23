import sys
from git import Repo, exc
from os import path
from time import time

sevenDays = 7*24*60*60 # denotes the duration of seven days in seconds

def main():
    """
    Main routine for the blame rufus program.
    Accepts and requires one argument that denotes a git repository path.
    Validates the path, and then prints:
        1) Its active branch
        2) Whether local repository files have been modified.
        3) Whether the current head commit was authored in the last week
        4) Whether the current head commit was authored by Rufus
    """
    dirPath = sys.argv[0] if len(sys.argv) > 1 else "./"
    if not path.exists(dirPath):
        print("The provided path: \"" + str(dirPath) + "\" does not exist")
        return

    try:
        repo = Repo(dirPath)
    except exc.InvalidGitRepositoryError:
        print("The provided path: \"" + str(dirPath) + "\" is not a valid git repository")
        return True

    print("For the git repository \"" + str(dirPath) + "\":")
    print("active branch: " + getActiveBranch(repo))
    print("local changes: " + str(hasLocalChanges(repo)))
    print("recent commit: " + str(hadRecentCommit(repo)))
    print("blame Rufus: " + str(blameRufus(repo)))
    return

def getActiveBranch(repo: Repo) -> str:
    """
    Returns the active branch of the git repository
    """
    return repo.active_branch.name

def hasLocalChanges(repo: Repo) -> bool:
    """
    Returns True if repository files have been modified, False otherwise.
    This includes whether or not there exist new files.
    """
    return len(repo.head.commit.diff()) > 0

def hadRecentCommit(repo: Repo) -> bool:
    """
    Returns True if the current head commit was authored last week, False otherwise.
    This specifically verifies whether the head was committed within 604800 seconds (7 full days) from the current day and time.
    """
    return time()-repo.head.commit.committed_date < sevenDays

def blameRufus(repo: Repo) -> bool:
    """
    Returns True the current head commit was authored by Rufus, False otherwise.
    This doesn't respect case sensitivity and strips all spaces; thus RUFUS, ru fus, and r UFus are all equivalent.
    """
    return "".join(repo.head.commit.author.name.split()).upper() == "RUFUS"

main()
