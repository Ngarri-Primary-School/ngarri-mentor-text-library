-- Public read on every teacher-facing table. No insert/update/delete policies
-- for anon/authenticated — the admin area writes via the service_role key
-- server-side (behind the shared passcode), which bypasses RLS by design.

alter table writing_traits enable row level security;
alter table writing_trait_detail enable row level security;
alter table reading_strategies enable row level security;
alter table reading_strategy_detail enable row level security;
alter table pride_values enable row level security;
alter table inquiry_lenses enable row level security;
alter table books enable row level security;
alter table writing_trait_annotations enable row level security;
alter table reading_strategy_annotations enable row level security;
alter table pride_value_annotations enable row level security;
alter table inquiry_lens_annotations enable row level security;
alter table teaching_ideas enable row level security;
alter table why_use_bullets enable row level security;
alter table teaching_resources enable row level security;

create policy "public read" on writing_traits for select using (true);
create policy "public read" on writing_trait_detail for select using (true);
create policy "public read" on reading_strategies for select using (true);
create policy "public read" on reading_strategy_detail for select using (true);
create policy "public read" on pride_values for select using (true);
create policy "public read" on inquiry_lenses for select using (true);
create policy "public read" on books for select using (true);
create policy "public read" on writing_trait_annotations for select using (true);
create policy "public read" on reading_strategy_annotations for select using (true);
create policy "public read" on pride_value_annotations for select using (true);
create policy "public read" on inquiry_lens_annotations for select using (true);
create policy "public read" on teaching_ideas for select using (true);
create policy "public read" on why_use_bullets for select using (true);
create policy "public read" on teaching_resources for select using (true);

