import sys
from git import Repo, exc
from os import path
from time import time

SEVEN_DAYS = 7*24*60*60 # denotes the duration of seven days in seconds

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
    git_dir = sys.argv[1] if len(sys.argv) > 1 else "./"
    if not path.exists(git_dir):
        print("The provided path: \"" + str(git_dir) + "\" does not exist")
        return

    try:
        rep = Repo(git_dir)
    except exc.InvalidGitRepositoryError:
        print("The provided path: \"" + str(git_dir) + "\" is not a valid git repository")
        return

    print("For the git repository \"" + str(git_dir) + "\":")
    print("active branch: " + getActiveBranch(rep))
    print("local changes: " + str(hasLocalChanges(rep)))
    print("recent commit: " + str(hadRecentCommit(rep)))
    print("blame Rufus: " + str(blameRufus(rep)))
    return

def getActiveBranch(rep: Repo) -> str:
    """
    Returns the active branch of the git repository
    """
    return rep.active_branch.name

def hasLocalChanges(rep: Repo) -> bool:
    """
    Returns True if repository files have been modified, False otherwise.
    This includes whether or not there exist new files.
    """
    return len(rep.head.commit.diff()) > 0

def hadRecentCommit(rep: Repo) -> bool:
    """
    Returns True if the current head commit was authored last week, False otherwise.
    This specifically verifies whether the head was committed within 604800 seconds (7 full days) from the current day and time.
    """
    return time()-rep.head.commit.committed_date < SEVEN_DAYS

def blameRufus(rep: Repo) -> bool:
    """
    Returns True the current head commit was authored by Rufus, False otherwise.
    This doesn't respect case sensitivity and strips all spaces; thus RUFUS, ru fus, and r UFus are all equivalent.
    """
    return "".join(rep.head.commit.author.name.split()).upper() == "RUFUS"

main()
