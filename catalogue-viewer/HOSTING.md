# Shared progress viewer

Site address: https://ngarri-mentor-library-progress.velveteen.chatgpt.site

The user explicitly approved publishing the 343-book catalogue, blurbs, existing writing/reading links and 221 covers to OpenAI Sites for anyone with the link. No sign-in is required. It retains the original search, combined filters, book detail view and missing-information indicators. The viewer reads approved catalogue data directly from Supabase and checks for changes every 15 seconds.

As verified on 9 September 2026, Supabase contains 343 active books, 458 publicly readable writing records, 296 reading records, 10 PRIDE connections, 10 inquiry connections and 32 teaching ideas. The static collection contains 221 covers. Draft AI annotations are excluded from public responses. Book PDFs, raw snapshots, credentials, vault notes and review exports are not part of the public site.

`build_public.py --covers <original covers folder>` prepares the static `out/` directory. `.openai/hosting.json` records the existing Sites project; reuse it for updates rather than creating another site. The live Supabase connection and collapsible detail interface were published through version 4 of the Site. Sites keeps the published assets independent of this computer. Use the standard Sites packaging helper and credentials provided at runtime for future interface or cover updates.

The school GitHub repository remains the canonical project documentation/code destination. The Sites source repository is a deployment copy, not a competing editable project. The initial Site is owned by Phill's current account; school ownership/access handover for hosting remains a separate task. No automatic GitHub-to-Sites deployment has been configured.

Database content refreshes without republishing the website. Republish this Site only when its interface or static cover collection changes. Supabase Row Level Security keeps unreviewed suggestions out of the public response.
