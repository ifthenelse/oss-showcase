# Optional integrations

Discover tools in the active host only when a matching stage needs them. A plugin installed in ChatGPT Work, Codex or Claude Code is available in another host only if that host exposes the capability. Track each used capability, query scope, date, result and any fallback in the relevant private stage notes. Continue with local evidence when a tool, account, permission or plan is unavailable. Avoid duplicate queries and reuse research until the target, market, launch date or evidence changes.

| Plugin | Stage and capability | Fallback |
| --- | --- | --- |
| GitHub | 1, 4 and prepare-release: resolve the repository and exact ref; read remote files, commits and release evidence where available. Use local source and tests for working-tree behavior. 9: inspect workflow runs, jobs and artifacts for an already authorized deployment. Report config or release metadata separately from locally verified behavior. | Use local Git and manifests, or read the public repo and release pages. Mark remote workflow status unverified if inaccessible. |
| Ahrefs | 1 and 6: compare relevant organic competitors and keywords by target country and language. Use matching terms, keyword overview and SERP overview to identify intent before choosing copy and page scope. For an existing verified project, use Site Audit or Search Console reports within the authorized scope. Brand Radar may supply a dated baseline when the plan exposes it. | Use public search results and available first-party data. Leave volumes and AI visibility unknown when unmeasured. |
| Product Hunt | 1 and 10: where the active host exposes search or listing reads, inspect relevant launches, related products and the project's existing listing. Use official submission guidance to draft tagline, description, topics, gallery, demo link and maker comment. Treat rankings and engagement as dated observations. | Read public listings and the official launch guide. Keep the entire submission as local drafts when the host exposes no listing tool. |
| Cloudflare | 9, only when relevant: use the documentation tools for DNS and TLS requirements. Where the host exposes authorized account reads, verify the target zone, current record and proxy status. Use existing hosting conventions; a Cloudflare-managed domain can point at GitHub Pages. | Resolve public DNS and HTTP/TLS behavior and read the official docs. Note account settings that could not be verified. |

Ahrefs estimates describe the selected market and date. Keep them separate from observed Search Console data, public feature claims and adoption metrics. Batch a short keyword set where possible. Check plan access or paid usage before requesting broad reports. Do not create a project, start a paid crawl or connect Search Console as part of routine analysis.

Use the [service preflight and publication rules](execution.md) before using connected services. The generated workflow stages a local allowlist and runs independently of connectors.

[Product Hunt submission guide](https://help.producthunt.com/en/articles/17834537-4-build-your-product-page) · [Cloudflare proxy status](https://developers.cloudflare.com/dns/proxy-status/)
