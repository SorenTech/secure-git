# Creates queries to the GitHub API and contructs an API object, per the adaptor, out of them.

from .repo import Repository
from .github_adaptor import GitHubObject as ghObject

# Construct a GraphQL Query for the repo
def graphql_query(repo: Repository):
'''
Queries the GitHub GraphQL API for info on a named repository and returns the results.
'''
    return graphReturn

# Create a dictionary for the keyword arguments
def create_values(repo: Repository, graphReturn) -> dict:
'''
Returns a dictionary of values based on the results of the graphQL query.
'''
    values = {}
    
    return values


# Instantiate a ghObject with the keyword arguments
def create_gh_object(repo: Repository):
'''
Creates a GitHub Object based on the results of a GraphQL query, uses that object to update a repository's state.
'''
    graphReturn = graphql_query(repo)
    
    values = create_values(repo, graphReturn)
    
    object = new ghObject(**values)

    # Update the repo object based on ghObject
    object.repo_update()