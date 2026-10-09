# Ngarri Mentor Library WordPress plugin

This is the first implementation of the school-hosted WordPress conversion. It provides the `[ngarri_mentor_library]` shortcode, dedicated catalogue tables, an approved-content importer, protected private-media routes and the current catalogue browsing experience.

## Installation

1. Zip `ngarri-mentor-library/` and upload it under WordPress Plugins, or deploy it through the school cPanel Git workflow.
2. Activate the plugin.
3. Create a WordPress page containing `[ngarri_mentor_library]`.
4. Create the shared school WordPress user and give approved staff the login separately.
5. Use **Mentor Library > Import catalogue** to load an owner-generated JSON export.

The plugin stores plugin-managed files under `wp-content/uploads/ngarri-private/` and creates an Apache deny rule there. PDFs and covers should be uploaded into this private folder through the Phase 2 media-management screen before they are linked to books. The public catalogue uses `/ngarri-file/<attachment-id>` routes, which require a signed-in WordPress user and support byte-range PDF requests.

The current prototype does not yet provide all Phase 2 editing screens or an automated Supabase export. Those are the next migration tasks.
