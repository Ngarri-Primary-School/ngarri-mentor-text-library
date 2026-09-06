import {PGlite} from './runtime/package/dist/index.js';
import {readFileSync,readdirSync,writeFileSync} from 'node:fs';
import assert from 'node:assert/strict';
const base=new URL('../mentor-database-recovery-2026-09-05/',import.meta.url);
const read=p=>readFileSync(new URL(p,import.meta.url),'utf8');
const db=new PGlite();
const results=[];
const check=(name,actual,expected)=>{assert.deepEqual(actual,expected,name);results.push({name,passed:true});};
await db.exec('CREATE ROLE anon; CREATE ROLE authenticated; CREATE ROLE service_role BYPASSRLS; GRANT USAGE ON SCHEMA public TO anon, authenticated, service_role;');
// PGlite uses built-in gen_random_uuid. Only pgcrypto extension registration is omitted.
for(const f of readdirSync(new URL('migrations/',base)).filter(x=>x.endsWith('.sql')).sort()){
 let sql=readFileSync(new URL('migrations/'+f,base),'utf8').replace(/create extension if not exists pgcrypto;/i,'');
 await db.exec(sql);
}
await db.exec('GRANT ALL ON ALL TABLES IN SCHEMA public TO anon, authenticated, service_role; ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES TO anon, authenticated;');
const tables=JSON.parse(read('table-acls.json')).map(x=>x.relname);
const snapshot=async()=>JSON.stringify((await db.query("SELECT c.relname,ARRAY(SELECT x::text FROM unnest(c.relacl) x ORDER BY x::text) AS acl,(SELECT jsonb_agg(jsonb_build_object('name',polname,'roles',polroles::text,'qual',pg_get_expr(polqual,polrelid)) ORDER BY polname) FROM pg_policy p WHERE p.polrelid=c.oid) AS policies FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname='public' AND c.relkind='r' ORDER BY 1")).rows);
const before=await snapshot();
const beforeRows={};for(const t of tables)beforeRows[t]=(await db.query(`SELECT count(*)::int AS n FROM public.${t}`)).rows[0].n;
check('historical migrations restore 343 books',beforeRows.books,343);
check('historical writing annotations',beforeRows.writing_trait_annotations,391);
check('historical reading annotations',beforeRows.reading_strategy_annotations,260);
await db.exec(read('candidate.sql'));
for(const role of ['anon','authenticated']){
 await db.exec(`SET ROLE ${role}`);
 for(const [t,n] of Object.entries(beforeRows)){
  if(t==='teaching_resources')continue;
  check(`${role} existing ${t} remains visible`,(await db.query(`SELECT count(*)::int AS n FROM public.${t}`)).rows[0].n,n);
 }
 for(const t of tables)for(const privilege of ['INSERT','UPDATE','DELETE','TRUNCATE','REFERENCES','TRIGGER','MAINTAIN'])
  check(`${role} ${t} denies ${privilege}`,(await db.query('SELECT has_table_privilege(current_user,$1,$2) AS ok',[`public.${t}`,privilege])).rows[0].ok,false);
 for(const query of ["INSERT INTO books (title,blurb) VALUES ('denied','denied')","UPDATE books SET title=title WHERE false","DELETE FROM books WHERE false","SELECT * FROM teaching_resources LIMIT 1"]){
  let code;try{await db.exec(query)}catch(e){code=e.code}check(`${role} actual denied operation ${query.split(' ')[0]}`,code,'42501');
 }
 await db.exec('RESET ROLE');
}
// Mutate only isolated fixtures inside a transaction, then discard them.
await db.exec('BEGIN');
const id=(await db.query('SELECT id FROM books ORDER BY id LIMIT 1')).rows[0].id;
const trait=(await db.query('SELECT slug FROM writing_traits LIMIT 1')).rows[0].slug;
const strategy=(await db.query('SELECT slug FROM reading_strategies LIMIT 1')).rows[0].slug;
const pride=(await db.query('SELECT slug FROM pride_values LIMIT 1')).rows[0].slug;
const lens=(await db.query('SELECT slug FROM inquiry_lenses LIMIT 1')).rows[0].slug;
await db.query('DELETE FROM writing_trait_annotations WHERE book_id=$1',[id]);
await db.query('DELETE FROM reading_strategy_annotations WHERE book_id=$1',[id]);
const specs=[['writing_trait_annotations','trait_slug',trait,4],['reading_strategy_annotations','strategy_slug',strategy,4],['pride_value_annotations','value_slug',pride,2],['inquiry_lens_annotations','lens_slug',lens,2],['teaching_ideas',null,null,2],['why_use_bullets',null,null,2]];
for(const [table,col,slug,expected] of specs){
 const statuses=table.startsWith('writing_')||table.startsWith('reading_')?['blank','imported_teacher','imported_ozlit','ai_suggested','teacher_reviewed','teacher_added','rejected']:table.endsWith('_annotations')?['blank','ai_suggested','teacher_reviewed','teacher_added','rejected']:['ai_suggested','teacher_reviewed','teacher_added','rejected'];
 for(const status of statuses){
  // UNIQUE constraints on PRIDE/inquiry allow only one fixture at a time.
  if(table==='pride_value_annotations'||table==='inquiry_lens_annotations')await db.query(`DELETE FROM ${table} WHERE book_id=$1`,[id]);
  const obj={book_id:id,status};if(col)obj[col]=slug;
  if(table.startsWith('writing_')||table.startsWith('reading_'))obj.source_type='teacher_spreadsheet';
  if(table==='teaching_ideas'){obj.title='test';obj.description='test';}
  if(table==='why_use_bullets')obj.text='test';
  const keys=Object.keys(obj);await db.query(`INSERT INTO ${table} (${keys.join(',')}) VALUES (${keys.map((_,i)=>'$'+(i+1)).join(',')})`,Object.values(obj));
  for(const role of ['anon','authenticated']){
   await db.exec(`SET ROLE ${role}`);
   const count=(await db.query(`SELECT count(*)::int AS n FROM ${table} WHERE book_id=$1 AND status=$2`,[id,status])).rows[0].n;
   check(`${role} ${table} status ${status}`,count,['imported_teacher','imported_ozlit','teacher_reviewed','teacher_added'].includes(status)?1:0);
   await db.exec('RESET ROLE');
  }
 }
}
await db.query("UPDATE books SET status='archived' WHERE id=$1",[id]);
for(const role of ['anon','authenticated']){
 await db.exec(`SET ROLE ${role}`);
 for(const table of ['books',...specs.map(x=>x[0])])check(`${role} hides archived parent ${table}`,(await db.query(`SELECT count(*)::int AS n FROM ${table} WHERE ${table==='books'?'id':'book_id'}=$1`,[id])).rows[0].n,0);
 await db.exec('RESET ROLE');
}
await db.exec('ROLLBACK');
await db.exec('CREATE TABLE public.future_table_probe (id int)');
for(const role of ['anon','authenticated'])check(`${role} no automatic future-table privileges`,(await db.query("SELECT has_table_privilege($1,'public.future_table_probe','SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER,MAINTAIN') AS ok",[role])).rows[0].ok,false);
await db.exec('DROP TABLE public.future_table_probe');
await db.exec(read('rollback.sql'));
check('rollback restores exact local table grants and policies',await snapshot(),before);
for(const t of tables)check(`no row-count change ${t}`,(await db.query(`SELECT count(*)::int AS n FROM ${t}`)).rows[0].n,beforeRows[t]);
writeFileSync(new URL('test-results.json',import.meta.url),JSON.stringify({tested_at:new Date().toISOString(),engine:(await db.query('SELECT version()')).rows[0].version,checks:results.length,results,limitations:['PGlite PostgreSQL; not the hosted Supabase API stack','pgcrypto registration omitted; built-in gen_random_uuid used','Supabase-admin default privileges outside this candidate scope']},null,2));
console.log(JSON.stringify({passed:results.length,restored_rows:beforeRows}));
await db.close();
