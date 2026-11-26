# Publishing and discovery

The starter outputs one semantic page with native CSS and zero client JavaScript. Add sections or pages only when users need them and when the repository's validator and sitemap cover those routes.

| Site type | Canonical example | Asset URL strategy |
| --- | --- | --- |
| GitHub project Pages | `https://owner.github.io/repo/` | Relative `assets/…` in the site and `docs/assets/…` in README. Convert social preview URLs to absolute. |
| GitHub user or org Pages | `https://owner.github.io/` | Same strategy. Generate root `robots.txt`. |
| Custom domain with site at root | `https://tool.example.org/` | Same strategy. Configure Pages and DNS only with authorization. |
| Site under a custom-domain base path | `https://projects.example.org/tool/` | Same strategy. Confirm the actual path from the Pages configuration or hosting convention. |

Use HTTPS and one trailing slash for the homepage canonical. Keep the sitemap under the project path for project Pages and reference it from an origin-wide robots file only if that origin is under the user's control. A project-local `robots.txt` cannot govern an entire host. If the public destination is unknown, prepare local materials and leave canonical and deployment approval pending. The generator requires a real target URL.

## Discovery

Use the supported search and answer intents from the [market memo](research.md). Review the existing public URL when reachable, then check the staged candidate before channel selection. Use **copy-editing** for existing prose or **copywriting** for new copy. Lead with the user task, a verified result, and an install path.

- **SEO.** Check HTTPS, crawl directives, canonical, title and description, sitemap, headings, links and alt text. Keep title, description and social metadata consistent. Use a reviewed preview image, typically 1280 × 640, under `docs/assets/`. Check it at small sizes. Apply GitHub About, topics and social preview settings only after approval.
- **AEO and GEO.** Answer real questions in visible HTML. Name the product, who it helps, prerequisites, the exact command and an observed result. Link to source, tests or the demo for consequential claims. Use JSON-LD only when its type fits and its facts match the visible page. Treat `llms_txt` as opt-in.
- **Verification.** Record the ref, checked URLs, fixes and any unmeasured indexing or AI citations. Separate local checks from live crawl or citation data. Recheck the deployed site and use Search Console or Bing Webmaster Tools when verified access is available. Page readiness can be checked before launch without promising placement or citations.

[Google AI Search guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [Bing AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)

## Draft deployment

The workflow is manual dispatch from the default branch, passes only the explicit allowlist to the Pages upload action, and compares Pages configuration with the rendered canonical at release time. It uses pinned action versions, has no LLM call, and scopes write permissions to the deploy job. Verify a fresh local build with `python3 .agents/showcase/validate.py --stage <new-directory>`. Review the artifact before authorizing deployment. Excluded files in `docs/` stay excluded even when present in Git. To use the workflow after approval, Pages must use GitHub Actions as the source. If the project already publishes Pages, follow its existing deployment path.

[GitHub Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) · [Pages publishing source and custom domains](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## Publish to GitHub Pages

Use this procedure for an approved Pages step in guided or `publish` mode. Follow the [publication rules](execution.md#publication). Resolve the exact repository and current publishing source, Pages URL, custom domain and repository homepage. Prefer the GitHub connector for supported operations. Use authenticated GitHub CLI or Settings for missing operations after confirming the account and its permission. If the Pages endpoint returns 404, also check the repository's `has_pages` or Settings before treating Pages as disabled.

1. Reuse the existing Pages workflow or branch. When setting up the generated showcase workflow, use GitHub Actions as the publishing source. For an approved prebuilt static site without a workflow, a dedicated `gh-pages` branch with the validated files and `.nojekyll` is sufficient. Preserve the active source unless the user authorizes a migration.
2. Compare the staged public files and target with the approved plan. Use the GitHub Pages hostname by default. Obtain explicit confirmation for the exact custom hostname before configuring it or using it in the repository homepage. Verify domain ownership, the Pages association and the intended DNS target. Record the hostname, record type, target and proxy setting before changing DNS. The default Pages URL needs no Cloudflare setup. If a preexisting custom domain prevents use of the default URL, preserve that configuration and ask before choosing the custom URL. Change DNS only with authorization.
3. Enable Pages if it is disabled. For a branch deployment, publish the reviewed files to the approved source and check Pages settings again because a push to `gh-pages` can enable Pages automatically. When a hostname is approved, configure its Pages binding and authorized DNS before deploying the custom canonical. For Actions, dispatch the approved workflow on the default branch. Verify the deployment result, HTTPS, redirects, canonical URL, sitemap and key assets. Confirm the final hostname still matches the approved destination.
4. Set the repository's `homepage` to the verified URL and read it back. Skip the update if it already matches. If verification fails, preserve the homepage and report the blocker.

For the authenticated CLI fallback, set `repo` to the confirmed `owner/repo` and `site_url` to the verified URL. Run only the creation command appropriate for a site that is still disabled.

```sh
gh api "repos/$repo/pages"
gh api --method POST "repos/$repo/pages" -f build_type=workflow
gh api --method POST "repos/$repo/pages" -f 'source[branch]=gh-pages' -f 'source[path]=/'
gh api --method PATCH "repos/$repo" -f "homepage=$site_url"
gh api "repos/$repo" --jq .homepage
```

Record the live URL, source, deployment result and homepage value. [Pages API](https://docs.github.com/en/rest/pages/pages) · [Custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) · [Repository homepage API](https://docs.github.com/en/rest/repos/repos#update-a-repository)

## Social card starter

Copy `templates/social.html` and `templates/social.cjs` into the project demo or authoring directory. Tune the card CSS to the approved guidelines. Run the following from an environment where the script can resolve the existing Playwright dependency and browser. `social_tagline` is an optional shorter verified summary in the facts file.

```sh
node social.cjs .agents/product-facts.json social.html /path/to/review/social.png .
```

Review the PNG and move the approved version to `docs/assets/social.png`. Register it as `social` in the facts. Track the card source and brand inputs in the brand stage. An approved existing PNG can be reused if it still represents the project.
