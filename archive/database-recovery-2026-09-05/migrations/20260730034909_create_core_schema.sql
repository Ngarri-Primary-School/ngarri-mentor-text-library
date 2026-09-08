-- Ngarri Mentor Text Library — Core Schema
-- Normalized annotation tables per BOOK_DETAIL_FIELDS.md / APP_DESIGN.md.
-- No per-user accounts (no login for teachers; admin area uses a shared
-- passcode checked server-side, not modeled in the DB).

create extension if not exists pgcrypto;

-- ── Reference tables (populated once from Ngarri's own curriculum docs) ────

create table writing_traits (
  slug text primary key,
  name text not null,
  display_order int
);

create table writing_trait_detail (
  trait_slug text not null references writing_traits(slug) on delete cascade,
  year_level text not null, -- 'F','1'..'6'
  ku_verbatim text[] not null default '{}',
  ks_verbatim text[] not null default '{}',
  vocab text[] not null default '{}',
  primary key (trait_slug, year_level)
);

create table reading_strategies (
  slug text primary key,
  name text not null,
  category text not null -- monitoring_self_correcting | thinking_within_text | thinking_beyond_text | thinking_about_text
);

create table reading_strategy_detail (
  strategy_slug text not null references reading_strategies(slug) on delete cascade,
  year_level text not null,
  ku_verbatim text[] not null default '{}',
  ks_verbatim text[] not null default '{}',
  primary key (strategy_slug, year_level)
);

create table pride_values (
  slug text primary key,
  name text not null,
  one_liner text,
  we_will text[] not null default '{}',
  selection_indicators text[] not null default '{}'
);

create table inquiry_lenses (
  slug text primary key,
  name text not null,
  description text,
  selection_indicators text[] not null default '{}'
);

-- ── Core book table ─────────────────────────────────────────────────────

create table books (
  id uuid primary key default gen_random_uuid(),
  source_row int unique not null, -- traceability back to the migration spreadsheet
  title text not null,
  author text not null,
  illustrator text,
  publisher text,
  year_published int,
  text_type text,       -- Picture Book / Novel / Non-fiction / Poetry — not yet populated, needs Pass-1 enrichment
  genre text,            -- not yet populated, needs Pass-1 enrichment
  year_level_min int,    -- Foundation = 0 — not yet populated, needs Pass-1 enrichment
  year_level_max int,
  is_australian boolean, -- not yet populated, needs Pass-1 enrichment
  blurb text not null,
  blurb_status text not null default 'verified' check (blurb_status in ('verified','needs_review')),
  cover_url text,
  ozlit_calibrated boolean not null default false,
  status text not null default 'active' check (status in ('active','archived')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index books_title_idx on books using gin (to_tsvector('english', title));

-- ── Annotation tables (normalized, one row per book × trait/strategy/etc) ──

create table writing_trait_annotations (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  trait_slug text not null references writing_traits(slug),
  year_level text, -- specific year this note applies to; NULL until per-year AI enrichment
  in_this_book_text text, -- NULL until AI enrichment
  applicable_year_levels text, -- informational summary from source (e.g. OzLit's overall range), not a substitute for per-year rows
  source_type text not null check (source_type in ('teacher_spreadsheet','ozlit','ai_suggested','teacher_override')),
  source_name text,
  confidence text check (confidence in ('high','medium','low')),
  status text not null default 'blank' check (status in ('blank','imported_teacher','imported_ozlit','ai_suggested','teacher_reviewed','teacher_added','rejected')),
  reviewed_by text,
  reviewed_at timestamptz,
  created_at timestamptz not null default now(),
  unique (book_id, trait_slug, year_level)
);

create table reading_strategy_annotations (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  strategy_slug text not null references reading_strategies(slug),
  year_level text,
  in_this_book_text text,
  applicable_year_levels text,
  source_type text not null check (source_type in ('teacher_spreadsheet','ozlit','ai_suggested','teacher_override')),
  source_name text,
  confidence text check (confidence in ('high','medium','low')),
  status text not null default 'blank' check (status in ('blank','imported_teacher','imported_ozlit','ai_suggested','teacher_reviewed','teacher_added','rejected')),
  reviewed_by text,
  reviewed_at timestamptz,
  created_at timestamptz not null default now(),
  unique (book_id, strategy_slug, year_level)
);

create table pride_value_annotations (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  value_slug text not null references pride_values(slug),
  in_this_book_text text,
  confidence text check (confidence in ('high','medium','low')),
  status text not null default 'blank' check (status in ('blank','ai_suggested','teacher_reviewed','teacher_added','rejected')),
  reviewed_by text,
  reviewed_at timestamptz,
  created_at timestamptz not null default now(),
  unique (book_id, value_slug)
);

create table inquiry_lens_annotations (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  lens_slug text not null references inquiry_lenses(slug),
  big_question_addressed text,
  in_this_book_text text,
  confidence text check (confidence in ('high','medium','low')),
  status text not null default 'blank' check (status in ('blank','ai_suggested','teacher_reviewed','teacher_added','rejected')),
  reviewed_by text,
  reviewed_at timestamptz,
  created_at timestamptz not null default now(),
  unique (book_id, lens_slug)
);

create table teaching_ideas (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  title text not null,
  description text not null,
  time_minutes int,
  grouping text check (grouping in ('Individual','Pairs','Small group','Whole class')),
  difficulty text check (difficulty in ('Entry','Medium','Discussion','Extension')),
  colour_tag text,
  is_generic boolean not null default false,
  status text not null default 'ai_suggested' check (status in ('ai_suggested','teacher_reviewed','teacher_added','rejected')),
  created_at timestamptz not null default now()
);

create table why_use_bullets (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  text text not null,
  display_order int not null default 0,
  status text not null default 'ai_suggested' check (status in ('ai_suggested','teacher_reviewed','teacher_added','rejected')),
  created_at timestamptz not null default now()
);

create table teaching_resources (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references books(id) on delete cascade,
  type text not null check (type in ('PDF','DOC','VIDEO','LINK')),
  title text not null,
  description text,
  url text not null,
  created_at timestamptz not null default now()
);
