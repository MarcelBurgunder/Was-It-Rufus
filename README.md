Was-It-Rufus - Marcel Burgunder
Project for Pronto.ai Technical Interview

Background:
This project includes a Python script that will print specifics about a local git repository.
This takes in one argument <git_dir> which denotes the local git directory path to assess the git status of. If no argument is passed in, then the script will assume its parent directory as the directory to assess.

If the directory path is invalid, then an error will be printed and the program will exit.
Otherwise it prints the git repositories:
  1) Active branch name
  2) Whether local repository files have been modifies or there are new uncommited files.
  3) Whether the current head commit was authored last week, specifically whether it was authored exactly 7 days from the current time and day.
  4) Whether the current head commit was authored by Rufus; this is non-case sensitive and independent of spaces, thus: RUFUS, rUfuS, r UFU s, Ru Fus, are all equivalent to Rufus.  
 
Setup:
1. Make sure Python is installed (see https://www.python.org/downloads/).
2. Make sure Git is installed (see https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
3. Make sure the GitPython module is installed (https://gitpython.readthedocs.io/en/stable/intro.html).
3. If you haven't already, create a local git repository to work with. This can be done with the usual git commands in Git Bash
4. Place the script of this project, wasItRufus.py, in an accessible location. Placing it in the parent directory of the project may make things easier.

How to run:
In your terminal, run the Python script using the command 'python <path_to_file>\wasItRufus.py <git_dir>'.

Note: The exercise instructions indicate that the active branch returned is a boolean; this didn't make much sense to me, so instead my Python script is returning a string that denotes the active branches name. The program runs just as expected.
