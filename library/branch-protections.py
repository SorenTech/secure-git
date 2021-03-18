get_branch_protections = """
{
    repository(owner: self.owner, name self.name) {
        branchProtectionRules {
            edges {
                node {
                    pattern
                    allowsDeletions
                    allowsForcePushes
                    isAdminEnforced
                    requiresApprovingReviews
                    requiredReviewingApproveCount
                    requiresCodeOwnerReviews
                    restrictsReviewDismissals
                    reviewDismissalAllowances {
                        edges {
                            node {
                                actor {
                                    login
                                    name
                                    }
                                }
                            }
                        }
                    requiresCommitSignatures
                    requiresLinearHistory
                    restrictsPushes
                    pushAllowances {
                        edges {
                            node {
                                actor {
                                    login
                                    name
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
}
"""

