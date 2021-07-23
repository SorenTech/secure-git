# secure-GitHub

A CLI utility to secure a GitHub repo following the best practices identified in the CNCF Supply Chain Security Whitepaper.

## Recomendations For a Secure Source Code Repository:

The Cloud Native Computing Foundation published the Software Supply Chain Best Practices paper in May of 2021. Part one of this paper deals with source code repositories. In this section, CNCF makes the following recommendations:

1. Require signed commits
2. Verify commits in merges (to achieve "full attestation")
3. Use automated tooling to block the committing of secrets to a repository
4. Use automation to enforce coding conventions
5. Automatically perform security scanning of code and dependencies
6. Establish and adhere to contribution policies
7. Define roles/responsibilities and corresponding access controls for contributors
8. Require code reviews before merges
9. Prevent "force pushes" and otherwise implement branch protection rules
10. Require MFA for contributors
11. Require SSH for repository access
12. Have a key rotation policy
13. Use short lived/ephemeral certificates for automation agents

You can read more detailed explanations of each of these recommendations in the CNCF paper.

## What this Project Does:

This utility attempts to update as many of the settings as possible around a git repository to meet the above recommendations. It was originally conceived as being focused on GitHub, but is being designed to be platform agnostic so that, through the use of a simple API wrapper, it can work with any Git hosting platform. Different platforms enable different features differently, and not every recommendation can be implemented through code (some will have to be enforced manually by the project's organization). For example, with GitHub the utility can do the following:

1. Create branch protection rules which require:
   a. signed commits
   b. pull requests for certain branches (ie, main)
   c. code reviews for pull requests
   d. block force merges
2. Create a CODEOWNERS file that defines who can sign off of code reviews
3. Report what percentage of the project's merge commits are signed
4. Verify that users on a project have SSH keys for their account
5. Generate and revoke access tokens that can be used for automation agents

In addition, using git and the local system itself, the utility can:
1. Generate SSH and GPG keys and add them to a user account on GitHub
2. Verify the presence of certain git hooks (ie, awslabs/git-secrets), which speak to secret blocking, code convention enforcement, and automatic security scanning
3. Update the local .gitconfig file for a user to prefer SSH and automate commit signing

However, there are certain things that cannot be done on GitHub automatically. For example, we cannot enforce MFA (though this is easy enough for an organization to turn on). And though we can check for SSH keys on user accounts, we can't enforce their use of SSH to access the repo (this just has to be an organizational policy). The closest we can get is changing the local .gitconfig, but this can be undone by a user and/or bypassed at the CLI.

After completing this project for GitHub, the plan is to add support for GitLab and Bitbucket, followed possibly by some other git hosting platforms.

## Current Status: Infancy
This project has most of its skeleton, some of the graphql queries/mutations, and none of the actual commands written. As it is updated, we'll update the status here.
