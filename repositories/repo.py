# Establishes basic repository object and methods for manipulating its values.

from Decimal import *
import policies.repositories

# Define the principle "repository" object that is used
class Repository:
    def __init__(self, name: str, stub: str, location: str):
    ''' 
    Repositories are one of the principle entities  of the sgit script. Repositories are essentially a custom data object with the defined attributes of:
        Name: The name of the repo (a simple str)  
        Stub: The User/Name or Org/Name portion of the URL (another str)
        Location: The URL of the repo (another str)
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
        self.hasSignedCommits = false
        self.hasFullAttestation = false
        self.hasSecretBlocking = false
        self.hasSecurityScanning = false
        self.hasCodeReviews = false
        self.hasPullRequests = false
        self.hasNoForceMerges = false
        self.hasUserAuth = false
        self.hasAgentAuth = false
        self.hasVerification = self.hasSignedCommits && self.hasFullAttestation
        self.hasScanning = self.hasSecretBlocking && self.hasSecurityScanning
        self.hasAuthorization = self.hasCodeReviews && self.hasPullRequests && self.hasNoForceMerges
        self.hasAuthentication = self.hasUserAuth && self.hasAgentAuth
        self.signedCommitsScore = 0.0
        self.fullAttestationScore = 0.0
        self.secretBlockingScore = 0.0
        self.securityScanningScore = 0.0
        self.codeReviewsScore = 0.0
        self.pullRequestsScore = 0.0
        self.forceMergesScore = 0.0
        self.userAuthScore = 0.0
        self.agentAuthScore = 0.0
        self.verificationScore = self.signedCommitScore + self.fullAttestationScore
        self.scanningScore = self.secretBlockingScore + self.securityScanningScore
        self.authorizationScore = self.codeReviewScore + self.pullRequestScore + self.forceMergesScore
        self.authenticationScore = self.userAuthScore + self.agentAuthScore
        self.overallScore = Decimal.multiply(Decimal.add(verificationScore, scanningScore, protectionScore, authenticationScore), 1/4)
        
# Use Case: Check if Commit Signatures are Required
    def signatures_required(self, reqsSignedCommits: bool):
    '''
    Updates the hasSignedCommits value a repo based on whether that repo requires signed commits.
    '''
        if (reqsSignedCommits == Signed_Commits):
            self.hasSignedCommits = true
        else:
            self.hasSignedCommits = false
            
# Use Case: Check % of Commits Signed
    def signed_commits_percent(self, percentSignedCommits: float):
    '''
    Updates the signedCommitsScore based on the percentage of commits to main branch which are signed.
    '''
        if (percentSignedCommits > 0):
            self.signedCommitsScore = percentSignedCommits

# Use Case: Check % of Verified and Signed Merges (ie, Full Attestation)
    def full_attestation_percent(self, percentVerifiedMerges: float):
    '''
    Updates the fullAttestationScore value of the repo based on the percentage of merges in the repo which are verified and signed.
    '''
        if (percentVerifiedMerges > 0):
            self.fullAttestationScore = percentVerifiedMerges
            
# Use Case: Set hasFullAttestation value vased on fullAttestationScore
    def full_attestation_bool(self):
    '''
    Sets the hasFullAttestation value to "true" if fullAttestationScore is greater than 75%
    '''
        if (fullAttestationScore >= Merge_Attestation_Min):
            self.hasFullAttestation = true
        else:
            self.hasFullAttestation = false
            
# Use Case: Repo-Scanning -> Block Secrets Being Commmitted
    def secret_blocking(self, secretScanning: bool):
    '''
    Updates the hasSecretBlocking and secretBlockingScore value based on whether or not automated scanning exists to block the committing of secret files to the repository.
    '''
        if (secretScanning == Secret_Scanning):
            self.hasSecretBlocking = true
            self.secretBlockingScore = 1.0
        else:
            self.hasSecretBlocking = false
            self.secretBlockingScore = 0.0

## Use Case: Repo-Scanning -> Automatic Security Scanning
    def security_scanning(self, securityScanning: bool):
    '''
    Updates the hasSecurityScanning and securityScanningScore value of the repo based on whether or not automated security scanning is performed.
    '''
        if (securityScanning == Security_Scanning):
            self.hasSecurityScanning = true
            self.securityScanningScore = 1.0
        else:
            self.hasSecurityScanning = false
            self.securityScanningScore = 0.0

# Use Case: Repo-Authorizations -> Require Code Reviews
    def req_code_reviews(self, codeReviews: bool):
    '''
    Updates the hasCodeReviews and codeReviewsScore value of the repo based on whether code reviews are required for merges into the main branch.
    '''
        if (codeReviews == Code_Reviews):
            self.hasCodeReviews = true
            self.codeReviewsScore = 1.0
        else:
            self.hasCodeReviews = false
            self.codeReviewsScore = 0.0

# Use Case: Repo-Authorization -> Require Pull Requests on Main
    def req_pull_requests(self, pullRequests: bool):
    '''
    Updates the hasPullRequests and pullRequestsScore values of the repo based on whether pull requests are required to merge code into the main branch.
    '''
        if (pullRequests == Pull_Requests):
            self.hasPullRequests = true
            self.pullRequestsScore = 1.0
        else:
            self.hasPullRequests = false
            self.pullRequestsScore = 0.0

# Use Case: Repo-Authorizations -> Prevent Force-Merges 
    def block_force_merges(self, noForceMerges: bool):
    '''
    Updates the hasNoForceMerges and forceMergesScore values of the repo based on whether forced merges are blocked for all branches.
    '''
        if (noForceMerges == Blocked_Force_Merges):
            self.hasNoForceMerges = true
            self.forceMergesScore = 1.0
        else:
            self.hasNoForceMerges = false
            self.forceMergesScore = 0.0

# Use Case: Repo-Authentication -> Users Meet Authentication Requirements
    def user_authentication_score(self, users: dict):
    '''
    Updates the userAuthScore value of the repo based on the number of users who meet the authentication requirements.
    '''
        userAuthScores = []
        userCount = len(users)
        for user in users:
            if (user.AuthMethodsApproved == True):
                userAuthScores + 1
        self.userAuthScore = Decimal.multiply(userAuthScores, 1/userCount)
        
# Use Case: Agent Auth Score -> Agent Auth Bool
    def user_authentication_bool(self):
    '''
    Updates the hasUserAuth value if userAuthScore is greater than or equal to 75%
    '''
        if (self.userAuthScore >= User_Auth_Min):
            self.hasUserAuth = true
        else:
            self.hasUserAuth = false

# Use Case: Repo-Authentication -> Agents Meet Authentication Requirements
    def agent_authentication_score(self, agents: dict):
    '''
    Updates the agentAuthScore value of the repo based on the number of automation agents who meet the authentication requirements.
    '''
        agentAuthScores = []
        agentCount = len(agents)
        for agent in agents:
            if (agent.AuthMethodsApproved == True):
                agentAuthScores + 1
            self.authenticationScore = Decimall.multiply(agentAuthScores, 1/agentCount)
            
# Use Case: Agent Authentication Score -> Agent Auth Bool
    def agent_authentication_bool(self):
    '''
    Updates the hasAgentAuth value to true if the agentAuthScore is greater than or equal to 90%
    '''
        if (self.agentAuthScore >= Agent_Auth_Min):
            self.hasAgentAuth = true
        else:
            self.hasAgentAuth = false
