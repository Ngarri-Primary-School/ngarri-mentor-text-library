const $ = id => document.getElementById(id);
const el = (tag, text, cls) => { const n = document.createElement(tag); if(text !== undefined) n.textContent=text; if(cls)n.className=cls; return n; };
let data, state, preview=false;
const key='ngarri-fox-local-review-3-text-checked';
function message(text){$('message').textContent=text;}
function save(){try{localStorage.setItem(key,JSON.stringify(state));return true;}catch{message('Browser storage is unavailable. Download your review record before leaving.');return false;}}
function fresh(){return {version:data.version,reviewer:'',decisions:{},history:[]};}
function decision(item){return state.decisions[item.id] ?? {text:item.text,note:'',checked:false,status:'pending'};}
function record(item,changes){const prior=decision(item);state.decisions[item.id]={...prior,...changes};return save();}
function invalidate(item,changes){const prior=decision(item);if(prior.status==='approved')state.history.push({item_id:item.id,...prior,superseded_at:new Date().toISOString()});record(item,{...changes,status:'pending',reviewed_by:null,reviewed_at:null});updateProgress();}
function updateProgress(){const n=data.items.filter(i=>decision(i).status==='approved').length;$('progress').textContent=`${n} of ${data.items.length} approved for preview`;}
function setView(value){preview=value;$('review-controls').hidden=preview;$('review-tab').setAttribute('aria-pressed',String(!preview));$('preview-tab').setAttribute('aria-pressed',String(preview));$('view-heading').textContent=preview?'Your teacher page preview':'Strongest mentor-text candidates';message(preview?'Local preview only. These selections have not been published.':'');render();}
function render(){
  const content=$('content');content.replaceChildren();content.classList.toggle('teacher-grid',preview);updateProgress();
  const items=data.items.filter(i=>!preview||decision(i).status==='approved');
  if(!items.length){const box=el('div',undefined,'empty');box.append(el('h3','No approved teaching content yet'),el('p','Review a suggestion and approve it for this preview. Pending and omitted suggestions stay out of the teacher page.'));content.append(box);return;}
  for(const item of items){
    const d=decision(item), card=el('article',undefined,'card');card.dataset.category=item.category;card.dataset.item=item.id;
    const top=el('div',undefined,'card-top');top.append(el('span',item.category,'category'));const status=el('span',d.status==='approved'?'Approved for local preview':d.status==='omitted'?'Omitted':'Awaiting review','status');if(!preview)top.append(status);card.append(top,el('h3',item.title));
    const meta=el('div',undefined,'meta');meta.append(el('span',item.year,'chip'),el('span',item.minutes));card.append(meta);
    if(item.book_evidence?.length){const evidence=el('div',undefined,'book-evidence');evidence.append(el('strong','In the text'));for(const q of item.book_evidence)evidence.append(el('p',`“${q.quote}”`, 'book-quote'));if(!preview)evidence.append(el('small',`Supplied text PDF: ${[...new Set(item.book_evidence.map(q=>q.pdf_page))].map(p=>'p. '+p).join(', ')}. These are not printed-book page numbers.`));card.append(evidence);}
    if(preview){card.append(el('p',d.text,'prose'));const details=el('details');details.append(el('summary','Curriculum connection'),el('blockquote',item.curriculum.text));card.append(details);}
    else{
      card.append(el('blockquote',item.curriculum.text));
      const source=el('details');source.append(el('summary','Source and what still needs checking'),el('p',item.evidence,'source'),el('p',`Curriculum source: ${item.curriculum.source}`,'source'));if(item.source_url){const link=el('a','Publisher notes used to check this example');link.href=item.source_url;link.target='_blank';link.rel='noopener noreferrer';source.append(link);}card.append(source);
      const fields=el('div',undefined,'review-fields');const textLabel=el('label','In this book — example, explanation and teaching');const text=el('textarea');text.rows=17;text.value=d.text;textLabel.append(text);
      const noteLabel=el('label','Review notes — requests here do not automatically change the teaching text');const note=el('textarea');note.rows=3;note.value=d.note;note.placeholder='Record evidence checked or changes you want made. To change the displayed teaching text yourself, edit the larger box above.';noteLabel.append(note);
      const checkLabel=el('label',undefined,'check');const check=el('input');check.type='checkbox';check.checked=d.checked;checkLabel.append(check,el('span','I have checked the book evidence, curriculum wording and classroom suitability of this whole suggestion.'));
      fields.append(textLabel,noteLabel,checkLabel);card.append(fields);
      const feedback=el('p',d.status==='approved'?'Approved for your local preview. Your review notes are saved separately.':d.status==='omitted'?'Omitted from your teacher preview.':'','local-feedback');feedback.setAttribute('role','status');feedback.setAttribute('aria-live','polite');
      const pending=()=>{status.textContent='Awaiting review';approve.textContent='Approve for this preview';approve.disabled=false;feedback.textContent='Changes recorded. Review and approve again when ready.';};
      text.addEventListener('input',()=>{check.checked=false;invalidate(item,{text:text.value,checked:false});pending();});
      note.addEventListener('input',()=>{check.checked=false;invalidate(item,{note:note.value,checked:false});pending();});
      check.addEventListener('change',()=>{invalidate(item,{checked:check.checked});pending();});
      const actions=el('div',undefined,'actions');const approve=el('button',d.status==='approved'?'Approved for this preview':'Approve for this preview','approve');approve.disabled=d.status==='approved';approve.addEventListener('click',()=>{
        const current=decision(item);if(!state.reviewer.trim()){feedback.textContent='Add your name at the top of the page before recording an approval.';message(feedback.textContent);return;}
        if(!current.text.trim()||!current.note.trim()||!current.checked){feedback.textContent='Add your review notes and tick the confirmation box before approving. The teaching text must not be blank.';message(feedback.textContent);return;}
        const updated={...current,status:'approved',reviewed_by:state.reviewer.trim(),reviewed_at:new Date().toISOString()};state.history.push({item_id:item.id,...updated});const saved=record(item,updated);status.textContent='Approved for local preview';approve.textContent='Approved for this preview';approve.disabled=true;updateProgress();feedback.textContent=saved?'Approved for your local preview. Your review notes are saved separately; they do not automatically rewrite the teaching text.':'Approved in this session, but browser saving failed. Download your review record before leaving.';message(feedback.textContent);
      });
      const omit=el('button','Omit for now');omit.addEventListener('click',()=>{state.history.push({item_id:item.id,...decision(item),decision_at:new Date().toISOString(),action:'omit'});record(item,{status:'omitted',checked:false,reviewed_by:null,reviewed_at:null});check.checked=false;status.textContent='Omitted';approve.textContent='Approve for this preview';approve.disabled=false;feedback.textContent='Omitted from your teacher preview. Your notes are preserved.';updateProgress();message(`${item.title} is omitted. Its original suggestion is preserved.`);});
      const pendingButton=el('button','Keep pending');pendingButton.addEventListener('click',()=>{invalidate(item,{checked:false});check.checked=false;pending();message('Kept pending.');});actions.append(approve,omit,pendingButton);card.append(actions,feedback);
    }content.append(card);
  }
}
try{
  const response=await fetch('data.json');if(!response.ok)throw new Error('Content could not be loaded');data=await response.json();state=fresh();
  try{const stored=JSON.parse(localStorage.getItem(key));if(stored?.version===data.version&&typeof stored.reviewer==='string'&&stored.decisions&&Array.isArray(stored.history)){
    state=stored;
    for(const item of data.items){const d=state.decisions[item.id];if(d && (typeof d.text!=='string'||typeof d.note!=='string'||!['pending','approved','omitted'].includes(d.status)))delete state.decisions[item.id];else if(d?.status==='approved'&&(!d.checked||!d.note.trim()||!d.text.trim()||!d.reviewed_by||!d.reviewed_at))d.status='pending';}
  }}catch{message('Saved review could not be loaded. A fresh local review is displayed.');}
  $('reviewer').value=state.reviewer;$('reviewer').addEventListener('input',e=>{state.reviewer=e.target.value;save();});
  $('review-tab').addEventListener('click',()=>setView(false));$('preview-tab').addEventListener('click',()=>setView(true));
  $('export').addEventListener('click',()=>{const record={scope:'local_review_only_not_published',exported_at:new Date().toISOString(),book:data.book,version:data.version,reviewer:state.reviewer,items:data.items.map(i=>({original:i,review:decision(i)})),history:state.history};const blob=new Blob([JSON.stringify(record,null,2)],{type:'application/json'});const url=URL.createObjectURL(blob);const a=el('a');a.href=url;a.download='fox-review-record.json';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);message('Review record downloaded with original suggestions, sources and decisions.');});render();
}catch(error){message('The working example could not load. Open it through the local server described in README.md.');console.error(error);}
