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

Use indexable HTML, visible descriptive copy, stable internal links, title and description, canonical, sitemap, and meaningful alt text. Open Graph and card fields are sharing metadata. Produce a branded raster social preview (1280 × 640 is a useful GitHub-oriented starting size), verify legibility at small preview sizes, and store it in `docs/assets/`. If using a project logo, keep the approved version and render the card with a script or source file outside the public directory. Keep GitHub About/topics and social preview changes as drafts or instructions until authorized to apply them externally.

Use factual JSON-LD only if the type fits. Markup validity and rich-result eligibility are different checks. Answer-oriented copy should state what the tool does, who can use it, prerequisites, reproducible usage and observed output in visible HTML. Only add FAQ content when it answers a real question. Set `llms_txt` only as an opt-in experiment or requested documentation index. Neither schema nor an `llms.txt` file guarantees visibility or AI citations.

## Draft deployment

The workflow is manual dispatch from the default branch, passes only the explicit allowlist to the Pages upload action, and compares Pages configuration with the rendered canonical at release time. It uses pinned action versions, has no LLM call, and scopes write permissions to the deploy job. Verify a fresh local build with `python3 .agents/showcase/validate.py --stage <new-directory>`. Review the artifact before authorizing deployment. Excluded files in `docs/` stay excluded even when present in Git. To use the workflow after approval, Pages must use GitHub Actions as the source. A custom domain also requires the repository's Pages setting and correct DNS. Adapt the existing workflow instead when one already owns deployment.

[GitHub Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) · [Pages publishing source and custom domains](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [Google Search guidance for generative features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

## Social card starter

Copy `templates/social.html` and `templates/social.cjs` into the project demo or authoring directory. Tune the card CSS to the approved guidelines. Run the following from an environment where the script can resolve the existing Playwright dependency and browser. `social_tagline` is an optional shorter verified summary in the facts file.

```sh
node social.cjs .agents/product-facts.json social.html /path/to/review/social.png .
```

Review the PNG and move the approved version to `docs/assets/social.png`. Register it as `social` in the facts. Track the card source and brand inputs in the brand stage. An approved existing PNG can be reused if it still represents the project.
