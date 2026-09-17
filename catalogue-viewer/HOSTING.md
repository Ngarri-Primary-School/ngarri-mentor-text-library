# Shared progress viewer handover

Site address: https://ngarri-mentor-library-progress.velveteen.chatgpt.site

The user approved a shared-password sign-in for the school principal, literacy leaders and Phill. The site retains the original search, combined filters, book detail view and missing-information indicators. The password is intentionally absent from GitHub, source code and project documents. Change it only through the hosting environment's secure settings.

As verified on 10 September 2026, Supabase contains Owl Moon as an approved revision with 7 writing, 6 reading, 1 PRIDE, 2 inquiry and 8 teaching ideas. The static collection contains 221 covers. Draft AI annotations are excluded from teacher-facing responses. Complete book and text-only resource packages now live in the private repository's `book-files/`. The Gruffalo is the first protected-deployment test: on 17 September 2026 its two buttons were published as protected website files packaged from the repository. The remaining legacy Drive-link mapping still needs replacement book by book. Credentials remain outside site assets.

`build_public.py --covers <original covers folder>` prepares the static `out/` directory. `.openai/hosting.json` records the existing Sites project; reuse it for updates rather than creating another site. The separate Sites deployment copy contains the shared sign-in worker and current link mapping. Sites keeps the published assets independent of this computer. Use the standard Sites packaging helper and credentials provided at runtime for future interface, cover or link updates.

The school GitHub repository remains the canonical project documentation/code destination. The Sites source repository is a deployment copy, not a competing editable project. The initial Site is owned by Phill's current account; school ownership/access handover for hosting remains a separate task. No automatic GitHub-to-Sites deployment has been configured.

Database content refreshes without republishing the website. Republish this Site when its interface, static cover collection or hard-coded school-resource link mapping changes. Supabase Row Level Security keeps unreviewed suggestions out of teacher-facing responses.
