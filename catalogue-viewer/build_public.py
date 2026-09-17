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
protected_books={
    'crickwing': ('Cannon, Janell/Crickwing_Cannon,_Janell,_1957_z_library_sk,_1lib_sk,_z_lib.pdf', 'Crickwing/Crickwing - searchable transcript.pdf'),
    'night-tree': ('Bunting, Eve/Night Tree (Eve Bunting).pdf', 'Night Tree/Night Tree - searchable transcript.pdf'),
    'the-alphabet-tree': ('Leonni, Leo/The alphabet tree - Lionni,Leo.pdf', 'The Alphabet Tree/The Alphabet Tree - searchable transcript.pdf'),
    'little-blue-and-little-yellow': ('Leonni, Leo/Little_blue_and_little_yellow - Leo Lionni.pdf', 'Little Blue and Little Yellow/Little Blue and Little Yellow - searchable transcript.pdf'),
    'owl-moon': ('Yolen, Jane/Owl Moon - Jane Yolen.pdf', 'Owl Moon/Owl Moon - searchable transcript.pdf'),
    'the-gruffalo': ('Donaldson, Julia/The Gruffalo - Julia Donaldson.pdf', 'The Gruffalo/The Gruffalo - searchable transcript.pdf'),
}
for slug, (picture_book, text_only) in protected_books.items():
    resource_dir=out/'book-files'/slug
    resource_dir.mkdir(parents=True,exist_ok=True)
    for destination, source in {
        'picture-book.pdf': args.book_files/'picture-books'/picture_book,
        'text-only.pdf': args.book_files/'text-only'/text_only,
    }.items():
        if not source.is_file():
            raise FileNotFoundError(f'Missing protected book resource: {source}')
        shutil.copy2(source,resource_dir/destination)
html=(out/'index.html').read_text(encoding='utf-8').replace('<title>','<meta name="robots" content="noindex, nofollow"><title>')
(out/'index.html').write_text(html,encoding='utf-8')
assert len(data['books'])==343
assert sum(available.values())==221
print(f'Static viewer ready: {len(data["books"])} books, {sum(available.values())} covers and {len(protected_books) * 2} protected book PDFs')
