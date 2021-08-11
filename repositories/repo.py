from Decimal import *

# Define the principle "repository" object that is used
class Repository:
    def __init__(self, name: str, stub: str, location: str, users: dict, agents: dict, hasVerification: bool = false, hasScanning: bool = false, hasAuthorization: bool = false, hasAuthentication: bool = false, verificationScore: float = 0.0, scanningScore: float = 0.0, authorizationScore: float = 0.0, authenticationScore: float = 0.0, overallScore: float = 0.0):
    ''' 
    Repositories are one of the principle entities  of the sgit script. Repositories are essentially a custom data object with the defined attributes of:
        Name: The name of the repo (a simple str)  
        Stub: The User/Name or Org/Name portion of the URL (another str)
        Location: The URL of the repo (another str)
        Users: A dictionary of users authorized for the repo
        Agents: A dictionary of authentication agents authorized for the repo
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
        self.users = users
        self.agents = agents
        self.hasVerification = hasVerification
        self.hasScanning = hasScanning
        self.hasAuthorization = hasAuthorization
        self.hasAuthentication = hasAuthentication
        self.verificationScore = verificationScore
        self.scanningScore = scanningScore
        self.authorizationScore = authorizationScore
        self.authenticationScore = authenticationScore
        self.overallScore = Decimal.multiply(Decimal.add(verificationScore, scanningScore, protectionScore, authenticationScore), 1/4)
        
# Use Case: Repo-Verification -> Commit Signatures are Required
    def signature_verification(self, reqsSignedCommits: bool) -> float:
    '''
    Updates the verificationScore value a repo based on whether that repo requires signed commits.
    '''
        if (reqsSignedCommits == true):
            self.verificationScore = Decimal.add(self.verificationScore, 0.5)
            
# Use Case: Repo-Verificattion -> Verified and Signed Merges (ie, Full Attestation)
    def full_attestation(self, percentVerifiedMerges: float) -> float:
    '''
    Updates the verificationScore value of the repo based on the percentage of merges in the repo which are verified and signed.
    '''
        if (percentVerifiedMerges > 0):
            self.verificationScore = Decimal.add(self.verificationScore, Decimal.multiply(percentVerifiedMerges, 0.5))
            
# Use Case: Repo-Scanning -> Block Secrets Being Commmitted
    def secret_blocking(self, hasSecretScanning: bool) -> float:
    '''
    Updates the scanningScore value of the repo based on whether or not automated scanning exists to block the committing of secret files to the repository.
    '''
        if (hasSecretScanning == true):
            self.scanningScore = Decimal.add(self.scanningScore, 0.5)

## Use Case: Repo-Scanning -> Automatic Security Scanning
    def security_scanning(self, hasSecurityScanning: bool) -> float:
    '''
    Updates the scanningScore value of the repo based on whether or not automated security scanning is performed.
    '''
        if (hasSecurityScanning == true):
            self.scanningScore = Decimal.add(self.scanningScore, 0.5)

# Use Case: Repo-Authorizations -> Require Code Reviews
    def req_code_reviews(self, reqsCodeReviews: bool) -> float:
    '''
    Updates the authorizationScore value of the repo based on whether code reviews are required for merges into the main branch.
    '''
        if (reqsCodeReviews == true):
            self.authorizationScore = Decimal.add(self.authorizationScore, 1/3)

# Use Case: Repo-Authorization -> Require Pull Requests on Main
    def req_pull_requests(self, reqsPullRequests: bool) -> float:
    '''
    Updates the authorizationScore value of the repo based on whether pull requests are required to merge code into the main branch.
    '''
        if (reqsPullRequests == true):
            self.authorizationScore = Decimal.add(self.authorizationScore, 1/3)

# Use Case: Repo-Authorizations -> Prevent Force-Merges 
    def block_force_merges(self, noForceMerges: bool) -> float:
    '''
    Updates the authorizationScore value of the repo based on whether forced merges are blocked for all branches.
    '''
        if (noForceMerges == true):
            self.authorizationScore = Decimal.add(self.authorizationScore, 1/3)

# Use Case: Repo-Authentication -> Users Meet Authentication Requirements
    def user_authentication_reqs(self, users: dict) -> float:
    '''
    Updates the authenticationScore value of the repo based on the number of users who meet the authentication requirements.
    '''
        userAuthScores = []
        for user in users:
            if (userAuthMethodsApproved == True):
                userAuthScores + 1
            else:
                userAuthScores + 0
        self.authenticationScore = Decimal.add(self.authenticationScore, Decimal.multiply(average(userAuthScores), 0.5))

# Use Case: Repo-Authentication -> Agents Meet Authentication Requirements
    def agent_authentication_reqs(self, agents: dict) -> float:
    '''
    Updates the authenticationScore value of the repo based on the number of automation agents who meet the authentication requirements.
    '''
        agentAuthScores = []
        for agent in agents:
            if (agentAuthMethodsApproved == True):
                agentAuthScores + 1
            else:
                agentAuthScores + 0
            self.authenticationScore = Decimall.add(self.authenticationScore, Decimal.multiply(average(agentAuthScores), 0.5))

# Use Case: Update repo bool values based on decimal scores
    def verification_status(self):
    '''
    Updates the hasVerification state of the repo based on its verificationScore
    '''
        if (self.verificationScore == 1):
            self.hasVerification = true
        else: self.hasVerification = false
        
    def scanning_status(self):
    '''
    Updates the hasScanning state of the repo based on its scanningScore
    '''
        if (self.scanningScore == 1):
            self.hasScanning = true
        else: self.hasScanning = false
    
    def authorization_status(self):
    '''
    Updates the hasAuthorization state of the repo based on its authorizationScore
    '''
        if (self.authorizationScore == 1):
            self.hasAuthorization = true
        else: self.hasAuthorization = false

    def authentication_status(self):
    '''
    Updates the hasAuthentication state of the repo based on its authenticationScore
    '''
        if (self.authenticaitonScore == 1):
            self.hasAuthenticaiton = true
        else: self.hasAuthenticaiton = false

    def status_check(sef):
    '''
    Updates all boolean flags.
    '''
        verification_status()
        scanning_status()
        authorization_status()
        authentication_status()

# Use Case: Reset all scores to zero and recompute booleans before an update
    def repo_score_reset(self):
    '''
    Reset all scores to zero and all booleans to false. Can be used prior to an ensure values all add up.
    '''
        self.verificationScore = 0
        self.scanningScore = 0
        self.authorizationScore = 0
        self.authenticationScore = 0
        status_check()
