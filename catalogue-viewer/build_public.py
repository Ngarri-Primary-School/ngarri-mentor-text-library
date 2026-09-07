"""Create the hosted static output from the curated snapshot and original covers."""
from pathlib import Path
import json, shutil, argparse
p=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--covers',type=Path,required=True);args=parser.parse_args()
out=p/'out';out.mkdir(exist_ok=True);(out/'covers').mkdir(exist_ok=True)
for name in ['index.html','app.js','style.css','data.json']:
    shutil.copy2(p/name,out/name)
data=json.loads((out/'data.json').read_text(encoding='utf-8'))
# This public progress snapshot must not include unreviewed AI drafts.
allowed={'imported_teacher','imported_ozlit','reviewed_added'}
for b in data['books']:
    for group in ['writing','reading','pride','inquiry']:
        b[group]=[a for a in b[group] if a['status'] in allowed]
    b['teaching_ideas']=[a for a in b['teaching_ideas'] if a.get('status')=='reviewed_added']
(out/'data.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
available={}
for b in data['books']:
    name=b.get('cover_url') or ''
    source=args.covers/name
    ok=bool(name and Path(name).name==name and source.is_file())
    available[b['id']]=ok
    if ok: shutil.copy2(source,out/'covers'/name)
(out/'cover-status.json').write_text(json.dumps(available),encoding='utf-8')
html=(out/'index.html').read_text(encoding='utf-8').replace('<title>','<meta name="robots" content="noindex, nofollow"><title>')
(out/'index.html').write_text(html,encoding='utf-8')
assert len(data['books'])==343
assert sum(available.values())==221
print(f'Static viewer ready: {len(data["books"])} books, {sum(available.values())} covers')
