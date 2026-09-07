"""Loopback-only viewer; no database writes or credentials. Python standard library."""
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, unquote
import argparse, json
p=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--port',type=int,default=8766)
parser.add_argument('--covers',type=Path,required=True,help='Original School Library/Covers folder')
args=parser.parse_args()
covers=args.covers.resolve()
allowed={'/':'index.html','/index.html':'index.html','/app.js':'app.js','/style.css':'style.css','/data.json':'data.json'}
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        route=unquote(urlsplit(self.path).path)
        if route=='/cover-status.json':
            books=json.loads((p/'data.json').read_text(encoding='utf-8'))['books']
            available={b['id']: bool(b.get('cover_url') and Path(b['cover_url']).name==b['cover_url'] and (covers/b['cover_url']).is_file()) for b in books}
            payload=json.dumps(available).encode()
            self.send_response(200); self.send_header('Content-Type','application/json'); self.send_header('Cache-Control','no-store'); self.end_headers(); self.wfile.write(payload); return
        if route.startswith('/covers/'):
            name=route[len('/covers/'):]
            target=(covers/name).resolve()
            if target.parent!=covers or target.suffix.lower() not in {'.jpg','.jpeg','.png','.webp'}:
                self.send_error(404); return
        elif route in allowed: target=p/allowed[route]
        else: self.send_error(404); return
        if not target.is_file(): self.send_error(404); return
        self.send_response(200); self.send_header('Content-Type',self.guess_type(str(target))); self.send_header('Cache-Control','no-store'); self.send_header('X-Content-Type-Options','nosniff'); self.end_headers(); self.wfile.write(target.read_bytes())
print(f'Catalogue viewer: http://127.0.0.1:{args.port}/',flush=True)
ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
