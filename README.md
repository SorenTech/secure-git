# secure-GitHub

A CLI utility to secure a GitHub repo following the best practices identified in the CNCF Supply Chain Security Whitepaper.

## Recomendations Implemented:

- Require commit signing (future goal: ability to generate and upload gpg keys if needed)
- Use branch protections for defined branches
- Require code reviews and admin sign off on merges
- Use PATs for automation agents
- Use SSH access for authenticated user (future goal: if no key, generate and add key, ensure .gitconfig prefers SSH for github repos)

## Things You Still Need To Do

- Require MFA for organization members (one setting and done)
- Enforce SSH access (no setting, must be monitored and enforced manually)

## What It Does:
- Sets branch protections block direct pushes to main and release branches, require merge reviews on main, release, and development branches, block force pushes on all branches, and require commit signing on all branches
- Verifies that new collaborators on a project have public keys (not an enforcement of SSH access, but verifies the theoretical capability of these by your collaborator)
- Creates a CODEOWNERS file from a template that lists owners required for reviews before merging into Main or Release branches
- Can add new collaborators or owners to an existing project
- Creates new projects following all guidelines (collecting variables either from a file, CLI flags, or interactive prompts)
- Updates existing projects to follow guidelines
- Validates settings on a repository and tells you where you are lacking
- Updates your local `.gitconfig` file to prefer SSH and automatically sign commits if those settings are not already your defaults

## How It Does It:
- It uses the GitHub GraphQL API wherever possible
- When not possible (a few things that aren't in the GraphQL API), falls back to the REST API
- Written in Python with no dependencies
- Authenticates to GitHub using a PAT, provided either in a config file, environmental variables, or via a CLI flag

## What It Will Do Someday:
- Generate CONTRIBUTING, CODE_OF_CONDUCT, and SECURITY policies for repository from a template
- Verify license compliance
- Create a pre-commit hook to block addition of dependencies that do not meet established security threshholds

## Current Status: Infancy
This project has most of its skeleton, some of the graphql queries/mutations, and none of the actual commands written. As it is updated, we'll update the status here.
