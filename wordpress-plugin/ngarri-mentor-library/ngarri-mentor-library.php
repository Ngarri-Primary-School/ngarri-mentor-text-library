<?php
/**
 * Plugin Name: Ngarri Mentor Library
 * Description: Private school mentor-text catalogue with protected media and migration tools.
 * Version: 0.1.0
 * Requires PHP: 8.2
 * Requires at least: 6.4
 */

defined('ABSPATH') || exit;

final class Ngarri_Mentor_Library {
    const VERSION = '0.1.0';
    const OPTION_PAGE_ID = 'ngarri_library_page_id';
    const NONCE = 'ngarri_library_admin';

    public static function boot() {
        add_action('init', [__CLASS__, 'register_routes']);
        add_action('template_redirect', [__CLASS__, 'protect_frontend']);
        add_action('admin_menu', [__CLASS__, 'admin_menu']);
        add_action('admin_post_ngarri_import_json', [__CLASS__, 'import_json']);
        add_action('admin_post_ngarri_save_book', [__CLASS__, 'save_book']);
        add_action('wp_enqueue_scripts', [__CLASS__, 'enqueue_assets']);
        add_shortcode('ngarri_mentor_library', [__CLASS__, 'shortcode']);
    }

    public static function activate() {
        self::install_schema();
        self::create_private_upload_dir();
        self::register_routes();
        flush_rewrite_rules();
    }

    public static function deactivate() { flush_rewrite_rules(); }

    private static function table($name) { global $wpdb; return $wpdb->prefix . 'ngarri_' . $name; }

    public static function install_schema() {
        global $wpdb;
        require_once ABSPATH . 'wp-admin/includes/upgrade.php';
        $charset = $wpdb->get_charset_collate();
        $sql = [];
        $sql[] = 'CREATE TABLE ' . self::table('books') . " (id bigint unsigned NOT NULL AUTO_INCREMENT, source_id varchar(64) NULL, title varchar(255) NOT NULL, author text NULL, illustrator text NULL, blurb longtext NULL, blurb_status varchar(50) NULL, cover_attachment_id bigint unsigned NULL, text_type varchar(100) NULL, genre varchar(255) NULL, year_level_min varchar(20) NULL, year_level_max varchar(20) NULL, review_status varchar(40) NOT NULL DEFAULT 'ai_suggested', reviewer varchar(255) NULL, reviewed_at datetime NULL, created_at datetime NOT NULL, updated_at datetime NOT NULL, PRIMARY KEY (id), KEY source_id (source_id), KEY review_status (review_status), KEY title (title(191))) $charset;";
        foreach ([
            'writing_traits' => 'slug varchar(100) NOT NULL, name varchar(255) NOT NULL, display_order int NOT NULL DEFAULT 0',
            'reading_strategies' => 'slug varchar(100) NOT NULL, name varchar(255) NOT NULL, category varchar(100) NULL',
            'pride_values' => 'slug varchar(100) NOT NULL, name varchar(255) NOT NULL, one_liner text NULL',
            'inquiry_lenses' => 'slug varchar(100) NOT NULL, name varchar(255) NOT NULL, description text NULL',
        ] as $table => $fields) {
            $sql[] = 'CREATE TABLE ' . self::table($table) . " (id bigint unsigned NOT NULL AUTO_INCREMENT, $fields, PRIMARY KEY (id), UNIQUE KEY slug (slug)) $charset;";
        }
        $sql[] = 'CREATE TABLE ' . self::table('connections') . " (id bigint unsigned NOT NULL AUTO_INCREMENT, book_id bigint unsigned NOT NULL, group_name varchar(30) NOT NULL, reference_slug varchar(100) NOT NULL, in_this_book_text longtext NULL, source_name varchar(255) NULL, status varchar(50) NULL, applicable_year_levels text NULL, year_level varchar(40) NULL, key_understanding_text text NULL, key_skill_text text NULL, display_order int NOT NULL DEFAULT 0, created_at datetime NOT NULL, updated_at datetime NOT NULL, PRIMARY KEY (id), KEY book_group (book_id, group_name), KEY reference_slug (reference_slug)) $charset;";
        $sql[] = 'CREATE TABLE ' . self::table('teaching_ideas') . " (id bigint unsigned NOT NULL AUTO_INCREMENT, book_id bigint unsigned NOT NULL, title varchar(255) NOT NULL, description longtext NULL, linked_focus text NULL, year_levels text NULL, where_to_look text NULL, learning_focus text NULL, teaching_sequence longtext NULL, student_application longtext NULL, notice_learning longtext NULL, time_minutes int NULL, grouping varchar(100) NULL, difficulty varchar(100) NULL, status varchar(50) NOT NULL DEFAULT 'ai_suggested', display_order int NOT NULL DEFAULT 0, created_at datetime NOT NULL, updated_at datetime NOT NULL, PRIMARY KEY (id), KEY book_id (book_id), KEY status (status)) $charset;";
        $sql[] = 'CREATE TABLE ' . self::table('resources') . " (id bigint unsigned NOT NULL AUTO_INCREMENT, book_id bigint unsigned NOT NULL, original_attachment_id bigint unsigned NULL, text_only_attachment_id bigint unsigned NULL, cover_attachment_id bigint unsigned NULL, PRIMARY KEY (id), UNIQUE KEY book_id (book_id)) $charset;";
        foreach ($sql as $statement) { dbDelta($statement); }
        update_option('ngarri_library_schema_version', self::VERSION);
    }

    public static function register_routes() {
        add_rewrite_rule('^ngarri-file/([0-9]+)/?$', 'index.php?ngarri_file=$matches[1]', 'top');
        add_rewrite_tag('%ngarri_file%', '([0-9]+)');
    }

    private static function create_private_upload_dir() {
        $dir = wp_upload_dir()['basedir'] . '/ngarri-private';
        wp_mkdir_p($dir);
        $htaccess = $dir . '/.htaccess';
        if (!file_exists($htaccess)) {
            file_put_contents($htaccess, "Options -Indexes\n<IfModule mod_authz_core.c>\nRequire all denied\n</IfModule>\n<IfModule !mod_authz_core.c>\nDeny from all\n</IfModule>\n");
        }
    }

    public static function protect_frontend() {
        if (is_admin() || wp_doing_ajax() || wp_doing_cron()) return;
        $file_id = absint(get_query_var('ngarri_file'));
        if ($file_id) { self::serve_file($file_id); exit; }
        $page_id = absint(get_option(self::OPTION_PAGE_ID));
        if ($page_id && is_page($page_id) && !is_user_logged_in()) {
            auth_redirect();
        }
    }

    private static function serve_file($attachment_id) {
        if (!is_user_logged_in()) { status_header(401); auth_redirect(); exit; }
        $path = get_attached_file($attachment_id);
        if (!$path || !is_readable($path) || !self::is_private_attachment($attachment_id)) { status_header(404); exit; }
        $mime = get_post_mime_type($attachment_id) ?: 'application/octet-stream';
        $size = filesize($path); $start = 0; $end = $size - 1;
        header('Content-Type: ' . $mime); header('Accept-Ranges: bytes'); header('Cache-Control: private, no-store');
        if (!empty($_SERVER['HTTP_RANGE']) && preg_match('/bytes=(\d*)-(\d*)/', $_SERVER['HTTP_RANGE'], $match)) {
            $start = $match[1] === '' ? max(0, $size - (int)$match[2]) : (int)$match[1];
            $end = $match[2] === '' ? $end : min($end, (int)$match[2]);
            if ($start > $end || $start >= $size) { status_header(416); header("Content-Range: bytes */$size"); exit; }
            status_header(206); header("Content-Range: bytes $start-$end/$size");
        }
        header('Content-Length: ' . ($end - $start + 1));
        header('Content-Disposition: inline; filename="' . sanitize_file_name(get_the_title($attachment_id)) . '"');
        $handle = fopen($path, 'rb'); fseek($handle, $start); $remaining = $end - $start + 1;
        while ($remaining > 0 && !feof($handle)) { $chunk = fread($handle, min(1024 * 1024, $remaining)); echo $chunk; $remaining -= strlen($chunk); if (connection_aborted()) break; }
        fclose($handle); exit;
    }

    private static function is_private_attachment($attachment_id) {
        return str_contains((string) get_attached_file($attachment_id), '/ngarri-private/');
    }

    public static function enqueue_assets() {
        if (!is_page(absint(get_option(self::OPTION_PAGE_ID)))) return;
        wp_enqueue_style('ngarri-mentor-library', plugins_url('assets/library.css', __FILE__), [], self::VERSION);
        wp_enqueue_script('ngarri-mentor-library', plugins_url('assets/library.js', __FILE__), [], self::VERSION, true);
        wp_localize_script('ngarri-mentor-library', 'NgarriLibrary', ['data' => self::catalogue_json()]);
    }

    public static function shortcode() {
        update_option(self::OPTION_PAGE_ID, get_the_ID());
        ob_start(); include __DIR__ . '/templates/library.php'; return ob_get_clean();
    }

    private static function catalogue_json() {
        global $wpdb;
        $approved = " AND review_status IN ('teacher_reviewed','imported_teacher','imported_ozlit','teacher_added','approved')";
        $books = $wpdb->get_results('SELECT * FROM ' . self::table('books') . " WHERE 1=1 $approved ORDER BY title ASC", ARRAY_A);
        $refs = [];
        foreach (['writing_traits' => 'writing', 'reading_strategies' => 'reading', 'pride_values' => 'pride', 'inquiry_lenses' => 'inquiry'] as $table => $group) $refs[$group] = $wpdb->get_results('SELECT * FROM ' . self::table($table) . ' ORDER BY name ASC', ARRAY_A);
        foreach ($books as &$book) {
            $book['writing'] = $book['reading'] = $book['pride'] = $book['inquiry'] = [];
            $book['teaching_ideas'] = [];
            $connections = $wpdb->get_results($wpdb->prepare('SELECT * FROM ' . self::table('connections') . ' WHERE book_id=%d ORDER BY display_order, id', $book['id']), ARRAY_A);
            foreach ($connections as $connection) $book[$connection['group_name']][] = ['slug' => $connection['reference_slug'], 'text' => $connection['in_this_book_text'], 'source' => $connection['source_name'], 'status' => $connection['status'], 'years' => $connection['applicable_year_levels'], 'year' => $connection['year_level'], 'keyUnderstanding' => $connection['key_understanding_text'], 'keySkill' => $connection['key_skill_text'], 'displayOrder' => $connection['display_order']];
            $book['cover_url'] = $book['cover_attachment_id'] ? home_url('/ngarri-file/' . absint($book['cover_attachment_id'])) : '';
            $resource = $wpdb->get_row($wpdb->prepare('SELECT * FROM ' . self::table('resources') . ' WHERE book_id=%d', $book['id']), ARRAY_A);
            $book['files'] = $resource ? ['original' => $resource['original_attachment_id'] ? home_url('/ngarri-file/' . absint($resource['original_attachment_id'])) : '', 'textOnly' => $resource['text_only_attachment_id'] ? home_url('/ngarri-file/' . absint($resource['text_only_attachment_id'])) : ''] : [];
            $book['teaching_ideas'] = $wpdb->get_results($wpdb->prepare('SELECT * FROM ' . self::table('teaching_ideas') . ' WHERE book_id=%d AND status IN ("teacher_reviewed","approved","teacher_added") ORDER BY display_order, id', $book['id']), ARRAY_A);
        }
        return ['references' => $refs, 'books' => $books];
    }

    public static function admin_menu() {
        add_menu_page('Mentor Library', 'Mentor Library', 'manage_options', 'ngarri-mentor-library', [__CLASS__, 'admin_books'], 'dashicons-book-alt');
        add_submenu_page('ngarri-mentor-library', 'Import catalogue', 'Import catalogue', 'manage_options', 'ngarri-import', [__CLASS__, 'admin_import']);
    }

    public static function admin_books() {
        global $wpdb; $books = $wpdb->get_results('SELECT id,title,author,review_status,updated_at FROM ' . self::table('books') . ' ORDER BY title ASC');
        echo '<div class="wrap"><h1>Ngarri Mentor Library</h1><p>Approved content is shown to staff. Use Import catalogue for the first migration; book editing screens will be added in Phase 2.</p><table class="widefat"><thead><tr><th>Title</th><th>Author</th><th>Status</th><th>Updated</th></tr></thead><tbody>';
        foreach ($books as $book) echo '<tr><td>' . esc_html($book->title) . '</td><td>' . esc_html($book->author) . '</td><td>' . esc_html($book->review_status) . '</td><td>' . esc_html($book->updated_at) . '</td></tr>';
        echo '</tbody></table></div>';
    }

    public static function admin_import() {
        if (!current_user_can('manage_options')) wp_die('Not allowed.');
        echo '<div class="wrap"><h1>Import catalogue JSON</h1><p>Use an owner-generated JSON export containing books, references, annotations and teaching ideas. Existing rows with the same source IDs are replaced.</p><form method="post" action="' . esc_url(admin_url('admin-post.php')) . '" enctype="multipart/form-data"><input type="hidden" name="action" value="ngarri_import_json"><input type="hidden" name="_wpnonce" value="' . esc_attr(wp_create_nonce(self::NONCE)) . '"><input type="file" name="catalogue" accept="application/json,.json" required><p><button class="button button-primary">Import catalogue</button></p></form></div>';
    }

    public static function import_json() {
        if (!current_user_can('manage_options')) wp_die('Not allowed.'); check_admin_referer(self::NONCE);
        if (empty($_FILES['catalogue']['tmp_name'])) wp_die('No file supplied.');
        $json = json_decode(file_get_contents($_FILES['catalogue']['tmp_name']), true);
        if (!is_array($json)) wp_die('The JSON file is invalid.');
        self::import_catalogue($json);
        wp_safe_redirect(add_query_arg(['page' => 'ngarri-mentor-library', 'imported' => 1], admin_url('admin.php'))); exit;
    }

    public static function import_catalogue(array $data) {
        global $wpdb; $now = current_time('mysql');
        foreach (['writing_traits','reading_strategies','pride_values','inquiry_lenses'] as $table) {
            foreach (($data[$table] ?? []) as $row) { $wpdb->replace(self::table($table), array_intersect_key($row, array_flip(['id','slug','name','display_order','category','one_liner','description']))); }
        }
        $book_ids = [];
        foreach (($data['books'] ?? []) as $row) {
            $fields = ['source_id','title','author','illustrator','blurb','blurb_status','cover_attachment_id','text_type','genre','year_level_min','year_level_max','review_status','reviewer','reviewed_at','created_at','updated_at'];
            $payload = array_intersect_key($row, array_flip($fields)); $payload['updated_at'] = $now; $payload['created_at'] = $payload['created_at'] ?? $now;
            $existing = !empty($row['source_id']) ? $wpdb->get_var($wpdb->prepare('SELECT id FROM ' . self::table('books') . ' WHERE source_id=%s', $row['source_id'])) : 0;
            if ($existing) { $wpdb->update(self::table('books'), $payload, ['id' => $existing]); $book_ids[$row['id'] ?? $row['source_id']] = (int)$existing; } else { $wpdb->insert(self::table('books'), $payload); $book_ids[$row['id'] ?? $row['source_id']] = (int)$wpdb->insert_id; }
        }
        $connection_rows = $data['connections'] ?? [];
        foreach ([
            'writing_trait_annotations' => ['group' => 'writing', 'slug' => 'trait_slug'],
            'reading_strategy_annotations' => ['group' => 'reading', 'slug' => 'strategy_slug'],
            'pride_value_annotations' => ['group' => 'pride', 'slug' => 'value_slug'],
            'inquiry_lens_annotations' => ['group' => 'inquiry', 'slug' => 'lens_slug'],
        ] as $key => $definition) {
            foreach (($data[$key] ?? []) as $row) {
                $row['group_name'] = $definition['group'];
                $row['reference_slug'] = $row[$definition['slug']] ?? '';
                $connection_rows[] = $row;
            }
        }
        foreach ($connection_rows as $row) {
            $row['book_id'] = $book_ids[$row['book_id']] ?? $row['book_id']; $row['updated_at'] = $now; $row['created_at'] = $row['created_at'] ?? $now;
            $wpdb->insert(self::table('connections'), array_intersect_key($row, array_flip(['book_id','group_name','reference_slug','in_this_book_text','source_name','status','applicable_year_levels','year_level','key_understanding_text','key_skill_text','display_order','created_at','updated_at'])));
        }
        foreach (($data['teaching_ideas'] ?? []) as $row) { $row['book_id'] = $book_ids[$row['book_id']] ?? $row['book_id']; $row['updated_at'] = $now; $row['created_at'] = $row['created_at'] ?? $now; $wpdb->insert(self::table('teaching_ideas'), array_intersect_key($row, array_flip(['book_id','title','description','linked_focus','year_levels','where_to_look','learning_focus','teaching_sequence','student_application','notice_learning','time_minutes','grouping','difficulty','status','display_order','created_at','updated_at']))); }
    }
}

register_activation_hook(__FILE__, ['Ngarri_Mentor_Library', 'activate']);
register_deactivation_hook(__FILE__, ['Ngarri_Mentor_Library', 'deactivate']);
Ngarri_Mentor_Library::boot();
