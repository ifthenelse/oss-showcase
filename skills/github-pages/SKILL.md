---
name: github-pages
description: Create and deploy a static site on GitHub Pages, enable Pages on the target repository when needed, and set the repository homepage to the verified public URL. Use for GitHub Pages setup, publishing, homepage synchronization, or confirmed custom-domain changes.
---

# GitHub Pages

Resolve the exact GitHub owner and repository from the request and the remote. Read the repository and Pages settings, including visibility, publishing source, `html_url`, `cname`, and current repository `homepage`. Prefer the GitHub connector for supported actions. If an operation is missing, use the authenticated official GitHub CLI or GitHub settings with the same authorized scope. Confirm the acting account and repository permission. A Pages API 404 can mean insufficient access. Treat it as disabled only when confirmed by repository metadata or Settings.

## Build and enable

1. Reuse the site's existing build and Pages workflow or branch. For a new site, choose the repository's published workflow convention. For an already built static site with no Pages workflow, a dedicated `gh-pages` branch containing only validated public output and a `.nojekyll` marker is sufficient. Keep source projects with a build step on their existing GitHub Actions workflow or use the official Pages actions. Preserve an active site's source unless the user authorizes migration.
2. Review the exact output. Publish an explicit public directory with `index.html`, exclude source, secrets, local files and private assets, and use project-path-safe links. Use the repository's static build and validation checks where available. For Actions, upload only the validated directory and scope `pages: write` and `id-token: write` to deployment.
3. When the user requests live publication, create Pages only if it is disabled. For branch publishing, push the reviewed artifact through the authorized Git path, then read Pages settings again because GitHub can enable Pages automatically on push. Create Pages with the existing branch and source path only if it remains disabled. For workflow publishing, use GitHub Actions as the source and deploy the approved ref. Inspect build and deployment results. After any ambiguous write failure, read GitHub state before retrying.
4. Read the published URL from Pages or the deployment result. Verify the final HTTPS response, expected site content, and important assets. Then set the repository's `homepage` to the working URL and read it back. If the deployment or URL check fails, report the exact blocker and record the current homepage.

## Domain choice

The default is the GitHub Pages project or owner URL returned by GitHub. Before configuring a custom domain or using it as the repository homepage, obtain explicit confirmation for the exact hostname. A domain found in a remote, DNS record, `CNAME`, or existing Pages configuration is not confirmation. If an existing custom domain prevents a verified default URL, keep its configuration and request confirmation before proceeding with the homepage change. Verify ownership, DNS, Pages setup, and HTTPS before selecting an approved custom URL. Change DNS only when that action is authorized.

## GitHub CLI fallback

Use these forms with a verified `owner/repo` in `repo` and the verified site URL in `site_url`.

```sh
gh api "repos/$repo/pages"
gh api --method POST "repos/$repo/pages" -f build_type=workflow
gh api --method POST "repos/$repo/pages" -f 'source[branch]=gh-pages' -f 'source[path]=/'
gh api --method PATCH "repos/$repo" -f "homepage=$site_url" --jq .homepage
```

Choose only one create operation for a disabled site. When reporting completion, include the live URL, the Pages source, the homepage readback, and any remaining deployment or domain issue.

[Pages REST API](https://docs.github.com/en/rest/pages/pages) · [Publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [Custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) · [Repository homepage API](https://docs.github.com/en/rest/repos/repos#update-a-repository)
