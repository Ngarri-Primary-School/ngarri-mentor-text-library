from pathlib import Path
import json,hashlib
from docx import Document
import pypdfium2 as pdfium

out=Path(__file__).resolve().parent
manifest=json.loads((out/'source-manifest.json').read_text())
vault=Path('C:/Users/09187270/iCloudDrive/iCloud~md~obsidian/Education/Curriculum/Ngarri Documents')
records=[]
for source in manifest:
 p=Path(source['source_path']);copy=vault/p.name
 source['vault_path']=str(copy)
 source['vault_matches_download']=copy.exists() and hashlib.sha256(copy.read_bytes()).hexdigest()==source['sha256']
 if p.suffix=='.docx':
  doc=Document(p);heading='';table_num=0
  for block in doc.iter_inner_content():
   if not hasattr(block,'rows'):
    if block.text.strip():heading=block.text.strip()
    continue
   table_num+=1
   assert len(block.rows)==2,(p.name,table_num,len(block.rows))
   assert len(block.columns)==7
   for col,(h,c) in enumerate(zip(block.rows[0].cells,block.rows[1].cells)):
    raw=c.text
    ku,ks=raw.split('Key Skills',1)
    ku=ku.removeprefix('Key Understandings').strip()
    records.append({'reference_id':f'{p.stem}:table{table_num}:column{col+1}','source_file':p.name,'source_sha256':source['sha256'],'section':heading,'year_label':h.text,'year_numeric':col,'key_understandings':[x for x in ku.splitlines() if x.strip()],'key_skills':[x for x in ks.strip().splitlines() if x.strip()],'raw_cell':raw,'status':'extracted_reference_not_imported'})
 else:
  doc=pdfium.PdfDocument(str(p))
  pages=range(len(doc)) if len(doc)==5 else [48,77,79,80,81,82,90]
  for i in pages:
   page=doc[i];bitmap=page.render(scale=1.3);img=bitmap.to_pil()
   img.save(out/f'{"murdoch" if len(doc)>5 else "stages"}-page-{i+1}.png')
   bitmap.close();page.close()
  doc.close()
(out/'source-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(out/'curriculum-reference-records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(records)==77
print(json.dumps({'records':len(records),'all_five_vault_copies_match':all(s['vault_matches_download'] for s in manifest),'sections':list(dict.fromkeys(r['section'] for r in records))},indent=2))
