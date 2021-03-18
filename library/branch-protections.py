get_branch_protections = {
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

update_branch_protections = {
    updateBranchProtectionRule (input:{allowsDeletions:False, allowsForcePushes:False, isAdminEnforced:True, requiresApprovingReviews:True, requiredApprovingReviewsCount:1, requiresCodeOwnerReviews:True, restrictReviewDismissals:True, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}
