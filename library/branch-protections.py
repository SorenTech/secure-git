# GraphQL query for getting current branch protection rules, mutations for setting branch protections based on pattern of most protection around main, slightly loosened protections around develop, baseline protections for all other branches

get_branch_protections = """
query($owner:Str!, $name:Str!) {
    repository(owner: $owner, name $name) {
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
                                    ... on User {
                                        login
                                        name
                                    }
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
                                    ... on User {
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
}
"""

update_branch_protections_main = """
mutation ($main_review_count:Int!) {
    updateBranchProtectionRule (input:{pattern:this.main_branch_pattern, allowsDeletions:False, allowsForcePushes:False, isAdminEnforced:True, requiresApprovingReviews:True, requiredApprovingReviewsCount:$main_review_count, requiresCodeOwnerReviews:True, restrictReviewDismissals:True, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}
"""

update_branch_protections_develop = """
mutation($dev_review_count:Int!) {
    updateBranchProtectionRule (input:{pattern:this.dev_branch_pattern, allowsDeletions:False, allowsForcePushes:False, requiresApprovingReviews:True, requiredApprovingReviewsCount:$dev_review_count, requireCommitSignatures:True, requiresLinearHistory:False, restrictPushes:True}) {
        branchProtectionRule
    }
}
"""

update_branch_protections_baseline = """
mutation {
    updateBranchProtectionRule (input:{pattern:"*", allowsForcePushes:False, requireCommitSignatures:True}) {
        branchProtectionRule
    }
}
"""
