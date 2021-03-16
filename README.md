# secure-GitHub

A CLI utility to secure a GitHub repo following the best practices identified in the CNCF Supply Chain Security Whitepaper.

## Recomendations Implemented:

- Require commit signing
- Enforce branch protections for defined branches
- Require code reviews and admin sign off on merges
- Ensure repo has a contributors and security policy
- Use PATs for automation agents

## Things You Still Need To Do

- Require MFA for organization members (one setting and done)
- Enforce SSH access (no setting, must be monitored and enforced manually)
