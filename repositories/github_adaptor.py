from .repo import Repository as repository

# Translates GitHub API return values into values pertaining to Repository objects

# Intermediary GitHub API Object:
class GitHubRepoAPIValues:
    def __init__(self, repo, signedCommits: bool, verfiedMerges: float, secretBlocking: bool, securityScanning: bool, codeReviews: bool, pullRequests: bool, noForceMerges: bool):
    '''
    Defines an object that (a) references a repo object (the repo being examined) and (b) contains the results of a GitHub API request in the format we need to populate the values of the repo through the Repository class's included methods.
    '''
        self.repo = repo
        self.signedCommits = signedCommits
        self.verifiedMerges = verifiedMerges
        self.secretBlocking = secretBlocking
        self.securityScanning = securityScanning
        self.codeReviews = codeReviews
        self.pullRequests = pullRequests
        self.noForceMerges = noForceMerges

# Signature Verification (via Branch Protection Rules)
    def signed_commits(self):
    '''
    If the GitHub API object indicates that the repostory requires signed commits, this will trigger a call to the Repository.signature_verification method with the value "true" to update the repo object.
    '''
        if (self.signedCommits == true): 
            repository.signature_verification(repo, true)

# Verified Merges vs. All Merges (?)
    def verified_merges(self):
     '''
    If the GitHub API object indicates that the repostory includes verified and signed merges, this will trigger a call to the Repository.full_attestation method with the percentage of merges that are verired and signed to update the repo object.
    '''
        if (self.verifiedMerges > 0):
            repository.full_attestation(repo, verifiedMerges)

# Secret Blocking (?)
    def secret_scanning(self):
     '''
    If the GitHub API object indicates that the repostory performs scanning to block committing secrets, this will trigger a call to the Repository.secret_blocking method with the value "true" to update the repo object.
    '''
        if (self.secretBlocking == true):
            repository.secret_blocking(repo, true)

# Security Scanning (?)
    def security_scanning(self):
     '''
    If the GitHub API object indicates that the repostory performas automatic security scanning, this will trigger a call to the Repository.security_scanning method with the value "true" to update the repo object.
    '''
        if (self.securityScanning = true)
            repository.security_scanning(repo, true)

# Code Reviews Required (via Branch Protection Rules)
    def code_reviews(self):
     '''
    If the GitHub API object indicates that the repostory requires code reviews for merges into the main branch, this will trigger a call to the Repository.req_code_reviews method with the value "true" to update the repo object.
    '''
        if (self.codeReviews == true):
            repository.req_code_reviews(repo, true)

# Pull Requests Required (via Branch Protection Rules)
    def pull_requests(self):
     '''
    If the GitHub API object indicates that the repostory requires pull requests to merge code into the main branch, this will trigger a call to the Repository.req_pull_requests method with the value "true" to update the repo object.
    '''
        if (self.pullRequests == true):
            repository.req_pull_requests(repo, true)

# Force Merges Prevented (via Branch Protection Rules)
    def no_force_merges(self):
     '''
    If the GitHub API object indicates that the repostory blocks forced merges, this will trigger a call to the Repository.block_force_merge method with the value "true" to update the repo object.
    '''
        if (self.noForceMerges == true):
            repository.block_force_merges(repo, true)
            
# Full run to update a repo object:
    def repo_update(self):
    '''
    This is a wrapper method which calls all the above methods in succession to trigger a full update of the repo object based on the API object.
    '''
        signed_commits(self)
        verified_merges(self)
        secret_scanning(self)
        security_scanning(self)
        code_reviews(self)
        pull_requests(self)
        no_force_merges(self)
