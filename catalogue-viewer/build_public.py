"""Create the hosted static output from the curated snapshot and original covers."""
from pathlib import Path
import json, shutil, argparse
p=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--covers',type=Path,required=True)
parser.add_argument('--book-files',type=Path,required=True)
args=parser.parse_args()
out=p/'out';out.mkdir(exist_ok=True);(out/'covers').mkdir(exist_ok=True)
for name in ['index.html','app.js','config.js','style.css']:
    shutil.copy2(p/name,out/name)
data=json.loads((p/'data.json').read_text(encoding='utf-8'))
(out/'data.json').unlink(missing_ok=True)
available={}
for b in data['books']:
    name=b.get('cover_url') or ''
    source=args.covers/name
    ok=bool(name and Path(name).name==name and source.is_file())
    available[b['id']]=ok
    if ok: shutil.copy2(source,out/'covers'/name)
(out/'cover-status.json').write_text(json.dumps(available),encoding='utf-8')
gruffalo_files={
    'picture-book.pdf': args.book_files/'picture-books'/'Donaldson, Julia'/'The Gruffalo - Julia Donaldson.pdf',
    'text-only.pdf': args.book_files/'text-only'/'The Gruffalo'/'The Gruffalo - searchable transcript.pdf',
}
resource_dir=out/'book-files'/'the-gruffalo'
resource_dir.mkdir(parents=True,exist_ok=True)
for destination, source in gruffalo_files.items():
    if not source.is_file():
        raise FileNotFoundError(f'Missing Gruffalo resource: {source}')
    shutil.copy2(source,resource_dir/destination)
html=(out/'index.html').read_text(encoding='utf-8').replace('<title>','<meta name="robots" content="noindex, nofollow"><title>')
(out/'index.html').write_text(html,encoding='utf-8')
assert len(data['books'])==343
assert sum(available.values())==221
print(f'Static viewer ready: {len(data["books"])} books, {sum(available.values())} covers and 2 protected Gruffalo PDFs')
