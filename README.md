Was-It-Rufus - Marcel Burgunder
Project for Pronto.ai Technical Interview

Background:
This project includes a python script that will print specifics about a local git repository.
This takes in one argument <git_dir> which denotes the git directory to assess the git status of.
If the directory is valid it prints the git repositories:
  1) Active branch
  2) Whether repository files have been modified
  3) Whether the current head commit was authored last week
  4) Whether the current head commit was authored by Rufus
 
Setup:
1. Make sure python is installed on your local machine (see https://www.python.org/downloads/)
2. Make sure git is installed on your local machine (see https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. If you haven't already, create a local git repository to work with. This can be done with the usual git commands in Git Bash
4. Place the script of this project, wasItRufus.py, in an accessible location. Placing it in the parent directory of the project may make things easier

How to run:
In your terminal, run the python script using the command 'python <path>\wasItRufus.py <git_dir>' 
