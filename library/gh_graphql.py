# Main functions for sending graphql queries and mutations

import requests

# construct request header
def construct_header(token)
    header = {"Authorization": "bearer " + token}
    return header

# construct Query Payload
def construct_payload(this, request, variables)
    request = this.request
    variables = this.variables
    data = [request, variables]
    return data

# GrpahQL query:
r = requests.post('https://api.github.com/graphql', header, data)

# recieve query response
def graphql_query(this, header, data):
    header = this.header
    data = this.data
    return r.json()

# recieve mutation response
def graphql_mutation(this, header, data):
    header = this.header
    data = this.data
    return r.status_code