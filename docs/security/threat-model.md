# Trust boundaries

| Boundary | What can go wrong | Mitigation |
| --- | --- | --- |
| Target repository, issues, websites and connector results → agent | Embedded instructions request commands, credentials or publication. Unverified claims reach public copy. | Treat input as data. Verify claims and reject directions outside authorized scope. Review commands and destinations before using tools. |
| Target project → public README, demo and Pages artifact | Private files, real account data or local paths are exposed. | Use synthetic demo data, review public copy and recordings, and validate the allowlisted Pages artifact before deployment. |
| Contributor PR → CI | Untrusted code or PR metadata executes with credentials. | Run PR jobs with a read-only token and no repository secrets. Pass the PR title as data and disable persisted checkout credentials. |
| Main branch → release workflow | Workflow or action changes gain write access to refs, releases or PRs. | Pin workflow actions to full SHAs. Review sensitive paths. Isolate the write-scoped job and require passing verification plus human review of the release PR. |

The validator checks file and artifact boundaries. Reviewers still need to inspect text and media for private content. Report vulnerabilities using the process in [SECURITY.md](../../SECURITY.md).
