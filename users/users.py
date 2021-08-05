def allowedAuthMethods(authMethods):
    '''
    verifies that the provided list of authentication methods are valid values
    Valid values include:
    - ssh: SSH authentication
    - pat: Personal  Access Token
    - mfa: Multifactor Authentication
    - pass:  Password Authentication
    '''
    ## code goes here
    ## returns True if list checks out. otherwise, returns error message idenfying the problematic item in the list

# Primary User Entity

class User:
    def __init__(self, name, authenticationMethods, authorizations):
    '''
    Users are one of the principle entities of the sgit script. Users are a custom data object consisting of:
    name:  the users GitHub username/handle (str)
    authenticationMethods: a list of the methods the user has available to authenticate to GitHub. Can include: ssh, pat, mfa, and pass
    authorizations: a dictionary of repositories and roles (owner, admin, reviewer, committer, contributor)
    '''
        self.name = name
        self.authenticationMethods = authenticationMethods
        self.authorizations = authorizations
        
## Use Case: Allowed Authentication Methods include SSH, PAT, MFA, Passwords
    def updateAuthMethods(user, authMethods):
    '''
    Adds the listed authentication methods to those registered for a user
    '''
    if(allowedAuthMethods(authMethods) == True):
        user.authenticationMethods += authMethods
    else:
        ## return error message
        
    def removeAuthMethod(user, authMethod):
    '''
    removes an item from the list of auth methods associated with a user
    '''
    ## code goes here

## Use Case: Allowed Authorizations include: owner, reviewer, contributor

