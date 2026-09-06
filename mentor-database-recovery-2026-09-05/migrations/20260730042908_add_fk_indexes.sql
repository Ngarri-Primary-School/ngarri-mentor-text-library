create index if not exists idx_inquiry_lens_annotations_lens_slug on inquiry_lens_annotations(lens_slug);
create index if not exists idx_pride_value_annotations_value_slug on pride_value_annotations(value_slug);
create index if not exists idx_reading_strategy_annotations_strategy_slug on reading_strategy_annotations(strategy_slug);
create index if not exists idx_teaching_ideas_book_id on teaching_ideas(book_id);
create index if not exists idx_teaching_resources_book_id on teaching_resources(book_id);
create index if not exists idx_why_use_bullets_book_id on why_use_bullets(book_id);
create index if not exists idx_writing_trait_annotations_trait_slug on writing_trait_annotations(trait_slug);
