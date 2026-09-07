# Shared progress viewer

Site address: https://ngarri-mentor-library-progress.velveteen.chatgpt.site

The user explicitly approved publishing the 343-book catalogue, blurbs, existing writing/reading links and 221 covers to OpenAI Sites for anyone with the link. No sign-in is required. It retains the original search, combined filters, book detail view and missing-information indicators. This is a dated read-only snapshot, not a live database connection.

The hosted output has 343 books, 391 writing links, 260 reading links and 221 available covers. Draft AI annotations are excluded from public output; the current snapshot contained no PRIDE/inquiry connections or teaching ideas. Book PDFs, raw snapshots, credentials, vault notes and review exports are not part of the public site.

`build_public.py --covers <original covers folder>` prepares the static `out/` directory. `.openai/hosting.json` records the existing Sites project; reuse it for updates rather than creating another site. The source used for initial publication was pushed to the Sites source repository at commit `0c2ca26fa3eab5c1e9a66f5203f9effafcac4fb5`. Sites keeps the published assets independent of this computer. Use the standard Sites packaging helper and credentials provided at runtime for future publication.

The school GitHub repository remains the canonical project documentation/code destination. The Sites source repository is a deployment copy, not a competing editable project. The initial Site is owned by Phill's current account; school ownership/access handover for hosting remains a separate task. No automatic GitHub-to-Sites deployment or automatic database refresh has been configured.

To refresh progress: obtain an authorised database snapshot, rebuild the viewer and public output, validate the counts and filters, save code/documentation in school GitHub, then publish an updated version of this same Site. Keep unreviewed suggestions out of the public output.

