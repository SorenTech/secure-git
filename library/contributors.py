# Query: List all the current contributors on a project
get_current_contributors = """
{
    repository(owner: $repo_owner, name: $repo_name) {
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
"""

# Query: Check if proposed new contributor matches our security profile
check_new_contributor = """
{
    user(login: $user_login) {
        publickeys {
            totalcount
        }
    }
}
"""

# REST API Object: Add a Contributor to our Project
new_contributor = {
    owner: self.authenticated_user
    repo: self.repo_name
    user: self.collaborator_login
    permission: self.permission_level
}
