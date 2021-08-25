# Translates GitHub API return values into Repository object fields.

from . import Repository

# Intermediary API Object:
class GHObject:
    def __init__(self, repo: Repository, users: dict, agents: dict, signedCommits: bool, actualSignedCommits: float, actualVerifiedMerges: float, codeReviews: float, pullRequests: float, blockForceMerges: float):
    '''
    Defines an object that (a) references a repo object (the repo being examined) and (b) contains the results of a GitHub API request in the format we need to populate the values of the repo through the Repository class's included methods.
    '''
        self.repo = repo
		self.users = users
		self.agents = agents
        self.signedCommits = signedCommits
        self.actualSignedCommits = actualSignedCommits
        self.actualVerifiedMerges = actualVerifiedMerges
        self.codeReviews = codeReviews
        self.pullRequests = pullRequests
        self.blockForceMerges = blockForceMerges

# Signature Verification (via Branch Protection Rules)
    def signed_commits(self):
    '''
    If the API object indicates that the repostory requires signed commits, this will trigger a call to the Repository.signatures_required method with the value "true" to update the repo object.
    '''
        if (self.reqsSignedCommits == true): 
            repo.signatures_required(true)

# Percentage of signed commits (via commit history)        
    def signed_commits_actual(self):
    '''
    If the API object has data about the percentage of commits that are signed, will trigger a call to the Repo's signed_commits_percent method with the value.
    '''
        if (self.actualSignedCommits > 0):
            repo.signed_commits_percent(self.actualSignedCommits)

# Verified Merges vs. All Merges (?)
    def verified_merges(self):
     '''
    If the API object indicates that the repostory includes verified and signed merges, this will trigger a call to the Repository.full_attestation method with the percentage of merges that are verired and signed to update the repo object.
    '''
        if (self.actualVerifiedMerges > 0):
            repo.full_attestation_percent(self.actualVerifiedMerges)

# Code Reviews Required (via Branch Protection Rules)
    def code_reviews(self):
     '''
    If the API object indicates that the repostory requires code reviews for merges into the main branch, this will trigger a call to the Repository.req_code_reviews method with the value "true" to update the repo object.
    '''
        if (self.codeReviews == true):
            repo.req_code_reviews(true)

# Pull Requests Required (via Branch Protection Rules)
    def pull_requests(self):
     '''
    If the API object indicates that the repostory requires pull requests to merge code into the main branch, this will trigger a call to the Repository.req_pull_requests method with the value "true" to update the repo object.
    '''
        if (self.pullRequests == true):
            repo.req_pull_requests(true)

# Force Merges Prevented (via Branch Protection Rules)
    def no_force_merges(self):
     '''
    If the API object indicates that the repostory blocks forced merges, this will trigger a call to the Repository.block_force_merge method with the value "true" to update the repo object.
    '''
        if (self.blockForceMerges == true):
            repo.block_force_merges(true)
            
# Full run to update a repo object:
    def repo_update(self):
    '''
    This is a wrapper method which calls all the above methods in succession to trigger a full update of the repo object based on the API object. It first resets the repo values to zero/false, then updates all the values based on those in the apiObject and finally recomputes the repo's booleans based on the updated values.
    '''
        signed_commits()
        signed_commits_actual()
        verified_merges()
        code_reviews()
        pull_requests()
        no_force_merges()
