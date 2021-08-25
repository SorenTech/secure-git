'''
Initialize a new sGit repository. Essentially just creates a repo object based on local repository details.
'''

from pathlib import Path

root = Path('.')
git = root / '.git' / 'remotes'

def get_repo_info(git):
    if (git.exists() && git.is_dir()):
        with open() as info:
            read_info = info.read()
            
        info.closed
    else:
        # return error

def init_repo():

