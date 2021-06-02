# Primary User Entity

class User:
    def __init__(self, name, authenticationMethods, authorizations):
        self.name = name
        self.authenticationMethods = authenticationMethods
        self.authorizations = authorizations
        
## Use Case: Allowed Authentication Methods include SSH, PAT, MFA


## Use Case: Allowed Authorizations include: owner, reviewer, contributor

