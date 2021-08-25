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
        Verification Status (hasVerification): Whether the repo meets the verification requirements of the script (bool)
        Scanning Status (hasScanning): Whether the repo meets the scanning requirements of the script (bool)
        Authorization Status (hasAuthorization): Whether the repo meets the protection/authorization requirements of the script (bool)
        Authentication Status (hasAuthentication): Whether the repo's users and automation agents meet the authentication requirements of the script (bool)
        Verfication Score: The percentage of the verification requirements met by the repo (float)
        Scanning Score: The percentage of the scanning requirements met by the repo (float)
        Authorization Score: The percentage of the authorization requirements met by the repo (float)
        Authentication Score: The percentage of users and automation agents meeting the authentication requirements of the script (float)
        Overall Score: The average of the verification, scanning, authorization, and authentication scores (float)
    '''
        self.name = name
        self.stub = stub
        self.location = location
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
