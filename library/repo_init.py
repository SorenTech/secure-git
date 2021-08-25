# Initialize a new sGit repository. Essentially just creates a repo object based on local repository details.

from pathlib import Path
import repositories.repo

root = Path('.')
git = root / '.git' / 'remotes'

repo_name = ""
repo_host = ""
repo_url = ""

def get_repo_info(git):
    if (git.exists() && git.is_dir()):
        with open() as info: # to-do: add file with remote configs
            read_info = info.read()
            
        info.closed
    else:
        # to-do: return error

def init_repo():
    repo = Repository(repo_name, repo_host, repo_url)
    # to-do: persist this somewhere 
