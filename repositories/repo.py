# Establishes basic repository object and methods for manipulating its values.

import policies.repositories

# Define the principle "repository" object that is used
class Repository:
    def __init__(self, name: str, host: str, url: str):
    ''' 
    Repositories are one of the principle entities  of the sgit script. Repositories are essentially a custom data object with the defined attributes of:
        Name: The name of the repo (a simple str)  
        Host: The TLD for the host of the repo's remotes. Ex: github.com (another str)
        URL: The full URL of the repo. Ex: https://github.com/SorenTech/SecureGitHub (another str)
        Users: A dictionary of users authorized for the repo
        Agents: A dictionary of automation agents authorized for the repo
        reqsSignedCommits: A boolean value indicating whether the commit signing policy of the repository matches the sGit policy/config
        percentSignedCommits: A float identifying the percentage of actual commits in the repository which are validly signed
        hasFullAttestation: A boolean value indicating whether the repository meets the verified merge requirements of the sGit policy/config
        percentVerifiedMerges: A float identifying the percentage of actual merges in the repository which are validly signed and verified
        hasSecretBlocking: A boolean value indicating whether the repository meets the commit-blocking for secrets requirements of the sGit policy/config
        hasSecurityScanning: A boolean value indicating whether the repository meets the security scanning requirements of the sGit policy/config
        reqsCodeReviews: A boolean value indicating whether the the repository meets the code reviews requirements of the sGit policy/config
        reqsPullRequests: A boolean value indicating whether the repository meets the pull request requirements of the sGit policy/config
        noForceMerges: A boolean value indicating whether the repository meets the force merge blocking requirements of the sGit policy/config
        
        It is important to note that boolean values indicate adherence to the active sGit configuration. The defaults for this configuraiton line up with the CNCF recommendatiosn for a secure supply chain. However, if the defaults have been modified by the user, a value of "true" may indicate something other than adherence with CNCF policy.
    '''
        self.name = name
        self.host = host
        self.url = url
        self.users = []
        self.agents = []
        self.reqsSignedCommits = false
        self.percentSignedCommits = 0.0
        self.hasFullAttestation = false
        self.percentVerifiedMerges = 0.0
        self.hasSecretBlocking = false
        self.hasSecurityScanning = false
        self.reqsCodeReviews = false
        self.reqsPullRequests = false
        self.noForceMerges = false
       #  self.hasUserAuth = false
       #  self.hasAgentAuth = false
        
# Use Case: Check if Commit Signatures are Required
    def signatures_required(self, signedCommits: bool):
    '''
    Updates the hasSignedCommits value a repo based on whether that repo requires signed commits.
    '''
        if (signedCommits == Signed_Commits):
            self.reqsSignedCommits = true
        else:
            self.reqsSignedCommits = false
            
# Use Case: Check % of Commits Signed
    def signed_commits_percent(self, actualSignedCommits: float):
    '''
    Updates the percentSignedCommits value based on the percentage of commits to main branch which are signed.
    '''
        if (actualSignedCommits > 0):
            self.percentSignedCommits = actualSignedCommits

# Use Case: Check % of Verified and Signed Merges (ie, Full Attestation)
    def full_attestation_percent(self, actualVerifiedMerges: float):
    '''
    Updates the percentVerfifiedMerges value of the repo based on the percentage of merges in the repo which are verified and signed.
    '''
        if (actualVerifiedMerges > 0):
            self.percentVerfiedMerges = actualVerifiedMerges
            
# Use Case: Set hasFullAttestation value vased on fullAttestationScore
    def full_attestation_bool(self):
    '''
    Sets the hasFullAttestation value to "true" if percentVerifiedMerges is greater than polciy requirement
    '''
        if (percentVerifiedMerges >= Merge_Attestation_Min):
            self.hasFullAttestation = true
        else:
            self.hasFullAttestation = false
            
# Use Case: Repo-Scanning -> Block Secrets Being Commmitted
    def secret_blocking(self, secretScanning: bool):
    '''
    Updates the hasSecretBlocking value based on whether or not automated scanning exists to block the committing of secret files to the repository.
    '''
        if (secretScanning == Secret_Scanning):
            self.hasSecretBlocking = true
        else:
            self.hasSecretBlocking = false

## Use Case: Repo-Scanning -> Automatic Security Scanning
    def security_scanning(self, securityScanning: bool):
    '''
    Updates the hasSecurityScanning value of the repo based on whether or not automated security scanning is performed.
    '''
        if (securityScanning == Security_Scanning):
            self.hasSecurityScanning = true
        else:
            self.hasSecurityScanning = false

# Use Case: Repo-Authorizations -> Require Code Reviews
    def req_code_reviews(self, codeReviews: bool):
    '''
    Updates the reqsCodeReviews value of the repo based on whether code reviews are required for merges into the main branch.
    '''
        if (codeReviews == Code_Reviews):
            self.reqsCodeReviews = true
        else:
            self.reqsCodeReviews = false

# Use Case: Repo-Authorization -> Require Pull Requests on Main
    def req_pull_requests(self, pullRequests: bool):
    '''
    Updates the reqsPullRequests values of the repo based on whether pull requests are required to merge code into the main branch.
    '''
        if (pullRequests == Pull_Requests):
            self.reqsPullRequests = true
        else:
            self.reqsPullRequests = false

# Use Case: Repo-Authorizations -> Prevent Force-Merges 
    def block_force_merges(self, blockForceMerges: bool):
    '''
    Updates the noForceMerges values of the repo based on whether forced merges are blocked for all branches.
    '''
        if (blockForceMerges == Blocked_Force_Merges):
            self.noForceMerges = true
        else:
            self.noForceMerges = false
