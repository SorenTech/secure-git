from github import Github

default_protected_branches = ["main", "develop"]

org_contributors = self.Github.organization.get_public_members()

admin_collaborators = self.Github.get_user()
