import json
from pathlib import Path
p=Path(__file__).resolve().parent
tables=[x['relname'] for x in json.loads((p/'table-acls.json').read_text())]
refs=['writing_traits','writing_trait_detail','reading_strategies','reading_strategy_detail','pride_values','inquiry_lenses']
imports=['writing_trait_annotations','reading_strategy_annotations']
reviewed=['pride_value_annotations','inquiry_lens_annotations','teaching_ideas','why_use_bullets']
sql=['-- Candidate SQL for isolated testing; not deployed or registered as a migration.','BEGIN;','SET LOCAL lock_timeout = \'5s\';']
rollback=['-- Restores the observed pre-change public access; use only to reverse this exact change.','BEGIN;']
for t in tables:
    sql += [f'REVOKE ALL PRIVILEGES ON TABLE public.{t} FROM anon, authenticated;',f'ALTER TABLE public.{t} ENABLE ROW LEVEL SECURITY;',f'DROP POLICY "public read" ON public.{t};']
    if t=='teaching_resources':continue
    expr='true'
    if t=='books':expr="status = 'active'"
    if t in imports:expr="status IN ('imported_teacher','imported_ozlit','teacher_reviewed','teacher_added')"
    if t in reviewed:expr="status IN ('teacher_reviewed','teacher_added')"
    if t in imports+reviewed:expr+=f' AND EXISTS (SELECT 1 FROM public.books b WHERE b.id = {t}.book_id AND b.status = \'active\')'
    sql += [f'GRANT SELECT ON TABLE public.{t} TO anon, authenticated;',f'CREATE POLICY "pilot trusted read" ON public.{t} FOR SELECT TO anon, authenticated USING ({expr});']
for t in tables:
    rollback += [f'DROP POLICY IF EXISTS "pilot trusted read" ON public.{t};',f'GRANT ALL PRIVILEGES ON TABLE public.{t} TO anon, authenticated;',f'CREATE POLICY "public read" ON public.{t} FOR SELECT TO public USING (true);']
sql += ['ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON TABLES FROM anon, authenticated;','COMMIT;']
rollback += ['ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES TO anon, authenticated;','COMMIT;']
(p/'candidate.sql').write_text('\n'.join(sql)+'\n')
(p/'rollback.sql').write_text('\n'.join(rollback)+'\n')
