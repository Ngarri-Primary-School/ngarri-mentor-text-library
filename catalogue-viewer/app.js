'use strict';

const $ = id => document.getElementById(id);
const groups = ['writing', 'reading', 'pride', 'inquiry'];
const titles = {writing:'Writing purposes',reading:'Reading purposes',pride:'PRIDE values',inquiry:'Inquiry lenses'};
const refreshEveryMs = 15000;
let data, covers = {}, lastFocus, isLoading = false;
const bookFiles = Object.freeze({
  'Night Tree': {
    original: 'https://drive.google.com/file/d/1H57nA7LWzyjrRv8WdI-y4NMW5adf7mwB/view',
    textOnly: 'https://drive.google.com/file/d/1EFyZQqNg-Mtniwndukg5xGzFdg7U2pR1/view'
  }
});
const node = (tag,text,cls) => {const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;};
const hasText = value => typeof value === 'string' && value.trim().length > 0;
const allLinks = book => groups.flatMap(group => book[group]);

function image(book){
  if(!book.cover_url || covers[book.id]===false) return node('div','No cover available','cover placeholder');
  const img=node('img',undefined,'cover');img.src='/covers/'+encodeURIComponent(book.cover_url);img.alt='Cover of '+book.title;img.loading='lazy';
  img.addEventListener('error',()=>{covers[book.id]=false;img.replaceWith(node('div','Cover unavailable','cover placeholder'));});return img;
}
function badge(text,cls){return node('span',text,'badge '+cls);}
function fileLink(text,url){const link=node('a',text,'file-link');link.href=url;link.target='_blank';link.rel='noopener noreferrer';return link;}
function label(group,slug){return data.references[group].find(item=>item.slug===slug)?.name||slug||'Unlabelled connection';}

async function api(table,select,query=''){
  const url=`${SUPABASE_CONFIG.url}/rest/v1/${table}?select=${encodeURIComponent(select)}${query}`;
  const response=await fetch(url,{headers:{apikey:SUPABASE_CONFIG.publishableKey},cache:'no-store'});
  if(!response.ok) throw new Error(`${table} returned ${response.status}`);
  return response.json();
}
function groupByBook(rows,slugKey){
  const grouped=new Map();
  for(const row of rows){
    if(!grouped.has(row.book_id)) grouped.set(row.book_id,[]);
    grouped.get(row.book_id).push({slug:row[slugKey],text:row.in_this_book_text,source:row.source_name||row.source_type,status:row.status,years:row.applicable_year_levels||row.year_level,year:row.year_level,keyUnderstanding:row.key_understanding_text,keySkill:row.key_skill_text,displayOrder:row.display_order});
  }
  return grouped;
}
async function fetchCatalogue(){
  const [books,writingTraits,readingStrategies,prideValues,inquiryLenses,writingRows,readingRows,prideRows,inquiryRows,teachingIdeas]=await Promise.all([
    api('books','id,title,author,illustrator,blurb,blurb_status,cover_url,text_type,genre,year_level_min,year_level_max','&order=title.asc'),
    api('writing_traits','slug,name,display_order','&order=display_order.asc'),api('reading_strategies','slug,name,category','&order=name.asc'),
    api('pride_values','slug,name,one_liner','&order=name.asc'),api('inquiry_lenses','slug,name,description','&order=name.asc'),
    api('writing_trait_annotations','*','&order=created_at.asc'),api('reading_strategy_annotations','*','&order=created_at.asc'),
    api('pride_value_annotations','*','&order=created_at.asc'),api('inquiry_lens_annotations','*','&order=created_at.asc'),api('teaching_ideas','*','&order=created_at.asc')
  ]);
  const writing=groupByBook(writingRows,'trait_slug'),reading=groupByBook(readingRows,'strategy_slug'),pride=groupByBook(prideRows,'value_slug'),inquiry=groupByBook(inquiryRows,'lens_slug'),ideas=new Map();
  for(const idea of teachingIdeas){if(!ideas.has(idea.book_id))ideas.set(idea.book_id,[]);ideas.get(idea.book_id).push(idea);}
  return {checked_at:new Date().toISOString(),references:{writing:writingTraits,reading:readingStrategies,pride:prideValues,inquiry:inquiryLenses},books:books.map(book=>({...book,writing:writing.get(book.id)||[],reading:reading.get(book.id)||[],pride:pride.get(book.id)||[],inquiry:inquiry.get(book.id)||[],teaching_ideas:ideas.get(book.id)||[]}))};
}
function filtered(){
  const query=$('search').value.trim().toLocaleLowerCase();
  return data.books.filter(book=>{
    if(query&&!`${book.title} ${book.author||''}`.toLocaleLowerCase().includes(query))return false;
    for(const group of groups){const value=$(group).value;if(value==='any'&&!book[group].length)return false;if(value==='none'&&book[group].length)return false;if(value&&value!=='any'&&value!=='none'&&!book[group].some(item=>item.slug===value))return false;}
    const links=allLinks(book),purposes=book.writing.length+book.reading.length;
    return ({'':true,cover:covers[book.id]!==false&&!!book.cover_url,'no-cover':covers[book.id]===false||!book.cover_url,blurb:hasText(book.blurb),'no-blurb':!hasText(book.blurb),purposes:purposes>0,'no-purposes':!purposes,explanation:links.some(item=>hasText(item.text)),'needs-explanation':links.length>0&&links.some(item=>!hasText(item.text))})[$('availability').value];
  });
}
function renderStats(){
  const stats=[['Books',data.books.length],['With writing purposes',data.books.filter(b=>b.writing.length).length],['With reading purposes',data.books.filter(b=>b.reading.length).length],['With PRIDE values',data.books.filter(b=>b.pride.length).length],['With inquiry lenses',data.books.filter(b=>b.inquiry.length).length]];
  $('stats').replaceChildren();for(const [labelText,value] of stats){const e=node('div',undefined,'stat');e.append(node('strong',String(value)),node('span',labelText));$('stats').append(e);}
}
function renderFilters(){
  for(const group of groups){const select=$(group),previous=select.value;select.replaceChildren(new Option('All books',''),new Option('Has any recorded connection','any'),new Option('No connections recorded','none'));
    for(const ref of data.references[group]){const count=data.books.filter(book=>book[group].some(item=>item.slug===ref.slug)).length;select.append(new Option(`${ref.name} (${count})`,ref.slug));}
    if([...select.options].some(option=>option.value===previous))select.value=previous;
  }
}
function render(){
  const books=filtered();$('count').textContent=`${books.length} of ${data.books.length} books`;$('results').replaceChildren();
  if(!books.length){const box=node('div',undefined,'empty');box.append(node('h3','No books match these filters.'),node('p','Try clearing one of the filters.'));$('results').append(box);return;}
  const frag=document.createDocumentFragment();for(const book of books){const card=node('button',undefined,'book');card.setAttribute('aria-label','View '+book.title);const top=node('div',undefined,'book-top'),info=node('div');info.append(node('h3',book.title),node('p',book.author||'Author not recorded','author'));top.append(image(book),info);card.append(top);const tags=node('div',undefined,'badges');for(const group of groups){const name=group==='pride'?'PRIDE':group[0].toUpperCase()+group.slice(1);tags.append(badge(`${name} · ${book[group].length}`,book[group].length?group:'missing'));}card.append(tags,node('p',`${hasText(book.blurb)?'Blurb recorded':'Blurb missing'} · ${covers[book.id]!==false&&book.cover_url?'Cover available':'Cover missing'}`,'small'));const total=allLinks(book).length,explained=allLinks(book).filter(item=>hasText(item.text)).length;card.append(node('p',total?`${explained} of ${total} connections have explanations`:'No teaching connections recorded','small'));card.onclick=()=>openBook(book,card);frag.append(card);}$('results').append(frag);
}
function appendStructuredIdea(section,idea){
  const card=node('details',undefined,'idea-card'),summary=node('summary'),meta=[idea.time_minutes&&`${idea.time_minutes} min`,idea.grouping,idea.difficulty].filter(Boolean).join(' · ');summary.append(node('strong',idea.title),node('span',meta,'small'));card.append(summary);
  const fields=[['Linked focus',idea.linked_focus],['Suggested years',idea.year_levels],['Where to look',idea.where_to_look],['Learning focus',idea.learning_focus],['Teaching sequence',idea.teaching_sequence],['Student application',idea.student_application],['Notice learning',idea.notice_learning]].filter(([,value])=>hasText(value));
  if(fields.length){for(const [heading,value] of fields)card.append(node('h4',heading),node('p',value));}else card.append(node('p',idea.description));section.append(card);
}
function appendConnectionEntry(parent,item,group){
  const entry=node('details',undefined,'connection-entry'),summary=node('summary');
  const year=item.year&&(item.year.startsWith('Year')?item.year:`Year ${item.year}`);
  summary.append(badge(year||'How this book connects',year?'year':group));
  entry.append(summary);
  const body=node('div',undefined,'entry-body');
  if(hasText(item.keyUnderstanding))body.append(node('p',`Key Understanding: “${item.keyUnderstanding}”`,'curriculum-line'));
  if(hasText(item.keySkill))body.append(node('p',`Key Skill: “${item.keySkill}”`,'curriculum-line'));
  body.append(node('p',hasText(item.text)?item.text:'Purpose recorded. The book-specific teaching explanation has not been added yet.'));
  const status={imported_teacher:'Imported teacher selection',imported_ozlit:'Imported OzLit selection',teacher_reviewed:'Teacher reviewed',teacher_added:'Teacher added'}[item.status]||item.status||'Not recorded';
  const provenance=[hasText(item.source)?`Source: ${item.source}`:null,`Status: ${status}`,item.years?`Years: ${item.years}`:null].filter(Boolean).join(' · ');
  body.append(node('p',provenance,'small'));entry.append(body);parent.append(entry);
}
function appendConnectionGroups(section,items,group){
  const grouped=new Map();
  for(const item of items){if(!grouped.has(item.slug))grouped.set(item.slug,[]);grouped.get(item.slug).push(item);}
  for(const [slug,connections] of grouped){
    const panel=node('details',undefined,`connection-group ${group}`),summary=node('summary');
    summary.append(node('strong',label(group,slug)),node('span',`${connections.length} ${connections.length===1?'connection':'connections'}`,'connection-count'));
    panel.append(summary);
    connections.sort((a,b)=>(a.displayOrder??999)-(b.displayOrder??999)||String(a.year||'').localeCompare(String(b.year||''),undefined,{numeric:true}));
    for(const item of connections)appendConnectionEntry(panel,item,group);
    section.append(panel);
  }
}
function openBook(book,trigger){
  lastFocus=trigger;const content=$('detail-content');content.replaceChildren();const hero=node('div',undefined,'detail-hero'),heading=node('div');heading.append(node('h2',book.title),node('p',book.author||'Author not recorded'));if(book.illustrator)heading.append(node('p','Illustrated by '+book.illustrator,'small'));hero.append(image(book),heading);content.append(hero);const meta=node('div',undefined,'meta');meta.append(badge(book.text_type||'Text type not recorded','missing'),badge(book.genre||'Genre not recorded','missing'));content.append(meta);
  const files=node('section',undefined,'detail-section book-files'),fileSet=bookFiles[book.title];files.append(node('h3','Book files'));if(fileSet){const links=node('div',undefined,'file-links');links.append(fileLink('Open picture book PDF',fileSet.original),fileLink('Open text-only PDF',fileSet.textOnly));files.append(links,node('p','Opens in the school Google Drive.','small'));}else files.append(node('p','Book files have not been linked yet.','small'));content.append(files);
  const blurb=node('details',undefined,'detail-section blurb-panel'),blurbSummary=node('summary');blurbSummary.append(node('h3','Blurb'));blurb.append(blurbSummary,node('p',book.blurb||'No blurb recorded.','blurb'));if(book.blurb)blurb.append(node('p','Recorded status: '+(book.blurb_status||'Not recorded'),'small'));content.append(blurb);
  for(const group of groups){const section=node('section',undefined,'detail-section connection-section');section.append(node('h3',`${titles[group]} (${book[group].length})`));if(!book[group].length)section.append(node('p','No approved connections recorded yet.','small'));else appendConnectionGroups(section,book[group],group);content.append(section);}
  const ideas=node('section',undefined,'detail-section teaching-ideas');ideas.append(node('h3',`Teaching ideas (${book.teaching_ideas.length})`),node('p','Classroom-ready activities linked to this book’s strongest traits, strategies, values and inquiry themes.','small'));if(!book.teaching_ideas.length)ideas.append(node('p','No approved teaching ideas recorded yet.','small'));for(const idea of book.teaching_ideas)appendStructuredIdea(ideas,idea);content.append(ideas);$('detail').showModal();$('close').focus();
}
function liveMessage(prefix='Live from Supabase'){return `${prefix} · Updated ${new Date(data.checked_at).toLocaleTimeString('en-AU',{hour:'numeric',minute:'2-digit',second:'2-digit'})} · Refreshes every 15 seconds`;}
async function refreshCatalogue({initial=false}={}){
  if(isLoading)return;isLoading=true;$('refresh').disabled=true;$('snapshot').textContent=initial?'Connecting to Supabase…':'Checking Supabase for updates…';
  try{const next=await fetchCatalogue(),changed=data&&JSON.stringify(data.books)!==JSON.stringify(next.books);data=next;renderFilters();renderStats();render();$('snapshot').textContent=liveMessage(changed?'Updated from Supabase':'Live from Supabase');$('snapshot').classList.remove('error');}
  catch(error){$('snapshot').textContent=data?'Live update unavailable · Showing the last successful result':'The live catalogue could not be loaded';$('snapshot').classList.add('error');if(!data)$('results').replaceChildren(node('p','Please try Refresh now. If the problem continues, the database connection needs attention.','empty'));}
  finally{isLoading=false;$('refresh').disabled=false;}
}
$('close').onclick=()=>$('detail').close();$('detail').addEventListener('close',()=>lastFocus?.focus());for(const id of ['search',...groups,'availability'])$(id).addEventListener(id==='search'?'input':'change',()=>data&&render());$('reset').onclick=()=>{for(const id of ['search',...groups,'availability'])$(id).value='';render();};$('refresh').onclick=()=>refreshCatalogue();
async function init(){try{const response=await fetch('cover-status.json',{cache:'no-store'});if(response.ok)covers=await response.json();}catch(_){covers={};}await refreshCatalogue({initial:true});window.setInterval(()=>refreshCatalogue(),refreshEveryMs);}
document.addEventListener('visibilitychange',()=>{if(!document.hidden&&data&&Date.now()-new Date(data.checked_at).getTime()>refreshEveryMs)refreshCatalogue();});init();
