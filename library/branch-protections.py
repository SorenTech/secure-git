# GraphQL query for getting current branch protection rules, mutations for setting branch protections based on pattern of most protection around main, slightly loosened protections around develop, baseline protections for all other branches

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
    updateBranchProtectionRule (input:{pattern:this.main_branch_pattern, allowsDeletions:False, allowsForcePushes:False, isAdminEnforced:True, requiresApprovingReviews:True, requiredApprovingReviewsCount:this.main_review_count, requiresCodeOwnerReviews:True, restrictReviewDismissals:True, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}

update_branch_protections_develop = {
    updateBranchProtectionRule (input:{pattern:this.dev_branch_pattern, allowsDeletions:False, allowsForcePushes:False, requiresApprovingReviews:True, requiredApprovingReviewsCount:this.dev_review_count, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}

update_branch_protections_baseline = {
    updateBranchProtectionRule (input:{pattern:"*", allowsForcePushes:False, requireCommitSignatures:True}) {
        branchProtectionRule
    }
}
