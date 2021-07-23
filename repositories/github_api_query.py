# Creates queries to the GitHub API and contructs an API object, per the adaptor, out of them.

from .repo import Repository

# Construct a GraphQL Query for the repo
def graphql_query(repo: Repository):
'''
Queries the GitHub GraphQL API for info on a named repository and returns the results:
    - signedCommits: via Branch Protection Rules
    - verifiedMerges: Percentage of the last 100 merge commits with valid signatures
    - codeReviews: required for main branch via branch protection rules
    - pullRequests: required for main branch (via branch protection rules)
    - noForceMerges: blocked via branch protection rules
'''
    return graphReturn

# Create a dictionary for the keyword arguments
def create_values(repo: Repository, graphReturn) -> dict:
'''
Returns a dictionary of values based on the results of the graphQL query.
'''
    values = {}
    
    return values
