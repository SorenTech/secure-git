from Decimal import *

# Define the principle "repository" object that is used
class Repository:
    def __init__(self, name: str, stub: str, location: str, hasVerification: bool = false, hasScanning: bool = false, hasProtection: bool = false, verificationScore: float = 0.0, scanningScore: float = 0.0, protectionScore: float = 0.0, overallScore: float = 0.0):
    ''' 
    Repositories are one of the principle entities  of the sgit script. Repositories are essentially a custom data object with the defined attributes of:
        Name: The name of the repo (a simple str)  
        Stub: The User/Name or Org/Name portion of the URL (another str)
        Location: The URL of the repo (another str)
        Verification Status (hasVerification): Whether the repo meets the verification requirements of the script (bool)
        Scanning Status (hasScanning): Whether the repo meets the scanning requirements of the script (bool)
        Protection Status (hasProtection): Whether the repo meets the protection/authorization requirements of the script (bool)
        Verfication Score: The percentage of the verification requirements met by the repo (float)
        Scanning Score: The percentage of the scanning requirements met by the repo (float)
        Protection Score: The percentage of the protection requirements met by the repo (float)
        Overall Score: The average of the verification, scanning, and protection scores (float)
    '''
        self.name = name
        self.stub = stub
        self.location = location
        self.hasVerification = hasVerification
        self.hasScanning = hasScanning
        self.hasProtection = hasProtection
        self.verificationScore = verificationScore
        self.scanningScore = scanningScore
        self.protectionScore = protectionScore
        self.overallScore = Decimal.multiply(Decimal.add(verificationScore, scanningScore, protectionScore), 1/3)
        
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

# Use Case: Repo-Protections -> Require Code Reviews
    def req_code_reviews(self, reqsCodeReviews: bool) -> float:
    '''
    Updates the protectionScore value of the repo based on whether code reviews are required for merges into the main branch.
    '''
        if (reqsCodeReviews == true):
            self.protectionScore = Decimal.add(self.protectionScore, 1/3)

# Use Case: Repo-Protections -> Require Pull Requests on Main
    def req_pull_requests(self, reqsPullRequests: bool) -> float:
    '''
    Updates the prtoectionScore value of the repo based on whether pull requests are required to merge code into the main branch.
    '''
        if (reqsPullRequests == true):
            self.protectionScore = Decimal.add(self.protectionScore, 1/3)

# Use Case: Repo-Protections -> Prevent Force-Merges 
    def block_force_merges(self, noForceMerges: bool) -> float:
    '''
    Updates the protectionScore value of the repo based on whether forced merges are blocked for all branches.
    '''
        if (noForceMerges == true):
            self.protectionScore = Decimal.add(self.protectionScore, 1/3)
            
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
    
    def protection_status(self):
    '''
    Updates the hasProtection state of the repo based on its protectionScore
    '''
        if (self.protectionScore == 1):
            self.hasProtection = true
        else: self.hasProtection = false