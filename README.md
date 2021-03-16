# secure-GitHub

A CLI utility to secure a GitHub repo following the best practices identified in the CNCF Supply Chain Security Whitepaper.

## Recomendations Implemented:

- Require commit signing (can also generate and upload gpg keys if needed)
- Enforce branch protections for defined branches
- Require code reviews and admin sign off on merges
- Ensure repo has a contributors and security policy
- Use PATs for automation agents
- Set up SSH access for authenticated user (if no key, generate and add key, ensure .gitconfig prefers SSH for github repos)

## Things You Still Need To Do

- Require MFA for organization members (one setting and done)
- Enforce SSH access (no setting, must be monitored and enforced manually)
