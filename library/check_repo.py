# Checks if a repository meets requirements. Returns updated scoring and bool values.

import repositories

# Step 1: verify we have a valid repo object
# - Get repo remote
# - Check repo object storage for matching repo

# Step 2: Run requisite query to get values from remote
# - Determine remote host
# - Run query based on remote host
# - Run local queries

# Step 3: Update repo values
# - Pass return values to relevant adaptors
# - Store updated values in the repo object storage

# Step 4: Return results
# - Determine areas where repo is deficient
# - Format message
# - Return message