"""Build a read-only catalogue snapshot. Source records are never changed."""
from pathlib import Path
import json
p=Path(__file__).resolve().parent
s=json.loads((p/'source-snapshot.json').read_text(encoding='utf-8'))
groups={'writing':('writing_traits','writing_trait_annotations','trait_slug'),'reading':('reading_strategies','reading_strategy_annotations','strategy_slug'),'pride':('pride_values','pride_value_annotations','value_slug'),'inquiry':('inquiry_lenses','inquiry_lens_annotations','lens_slug')}
refs={g:[{'slug':x['slug'],'name':x['name']} for x in s[conf[0]]] for g,conf in groups.items()}
books=[]
for b in s['books']:
    if b['status']!='active': continue
    item={k:b.get(k) for k in ['id','title','author','illustrator','blurb','blurb_status','cover_url','text_type','genre','year_level_min','year_level_max']}
    for g,(_,table,key) in groups.items():
        item[g]=[{'slug':a.get(key),'text':a.get('in_this_book_text'),'source':a.get('source_name') or a.get('source_type'),'status':a.get('status'),'years':a.get('applicable_year_levels') or a.get('year_level')} for a in s[table] if a['book_id']==b['id']]
    item['teaching_ideas']=[a for a in s['teaching_ideas'] if a['book_id']==b['id']]
    books.append(item)
(p/'data.json').write_text(json.dumps({'checked_at':s['checked_at'],'references':refs,'books':sorted(books,key=lambda b:b['title'].casefold())},ensure_ascii=False),encoding='utf-8')
print(f'Built {len(books)} books')
