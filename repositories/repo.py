# Define the principle "repository" object that is used

class Repository:
    def __init__(self, name, stub, location, hasVerification: bool, hasScanning: bool, hasProtection: bool):
        self.name = name
        self.stub = stub
        self.location = location
        self.hasVerification = hasVerification
        self.hasScanning = hasScanning
        self.hasProtection = hasProtection
        
# Use Case: Repo-Verification -> Commit Signatures are Required
    def signatureVerification(Repository, reqs_signed_commits):
        if (reqs_signed_commits == true):
            Repository.hasVerification = true
            
# Use Case: Repo-Scanning -> Block Secrets Being Commmitted


## Use Case: Repo-Scanning -> Automatic Security Scanning


## Use Case: Repo-Protections -> Require Code Reviews


## Use Case: Repo-Protections -> Require PUll Requests on Main


## Use Case: Repo-Protections -> Prevent Force-Merges 