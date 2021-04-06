# Base CLI command. Intent here is to parse arguments and handle reporting to the user
import sys
from library.gh_graphql import construct_graphql_header
from library.gh_rest import construct_rest_header


# Get user authorization (PAT)
def get_authorization():
    # Option 1: check for configuration file
    # Option 2: check for environmental variable
    # Option 3: request an access token interactively
    return token

# Contruct GraphQL heaaders using PAT
headers = []
def new_header(this, token):
    headers[0] = construct_graphql_header(this.token)
    headers[1] = construct_rest_header(this.token)

# Parse command
def parse(this):
    sub = None
    command = this.argv[0]
    target = command.split('-')
    if len(target) > 1:
        sub = target[1]
        try:
            mycli = import("library.%s", % sub) # we need a helper function here
    args = this.argv[1:]
    return mycli(args)

# Parse Output

# Report Output to User
