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

update_branch_protections_main = {
    updateBranchProtectionRule (input:{pattern:"main, master, release*, beta*", allowsDeletions:False, allowsForcePushes:False, isAdminEnforced:True, requiresApprovingReviews:True, requiredApprovingReviewsCount:this.mainReviewsCount, requiresCodeOwnerReviews:True, restrictReviewDismissals:True, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}

update_branch_protections_develop = {
    updateBranchProtectionRule (input:{pattern:"dev, develop", allowsDeletions:False, allowsForcePushes:False, requiresApprovingReviews:True, requiredApprovingReviewsCount:this.devReviewsCount, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}

update_branch_protections_baseline = {
    updateBranchProtectionRule (input:{pattern:"*", allowsForcePushes:False, requireCommitSignatures:True}) {
        branchProtectionRule
    }
}
