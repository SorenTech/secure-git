# Query: List all the current contributors on a project
get_current_contributors = {
    repository(owner:self.owner, name:self.name) {
        collaborators {
            edges {
                node {
                    login
                    name
                }
            }
        }
    }
}

# Query: Check if proposed new contributor matches our security profile
check_new_contributor = {
    user(login:this.user_login) {
        publickeys {
            edges {
                node {
                    fingerprint
                }
            }
        }
    }
}

# REST API Object: Add a Contributor to our Project
new_contributor = {
    owner: self.authenticated_user
    repo: self.repo
    user: self.collaborator
    permission: self.permission
}
