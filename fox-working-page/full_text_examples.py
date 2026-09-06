"""Build the expanded, text-checked Fox review without modifying original sources."""
import json, hashlib, unicodedata
from pathlib import Path
from pypdf import PdfReader
p=Path(__file__).resolve().parent
root=p.parent
manifest=json.loads((root/'fox-source-review/manifest.json').read_text())
src=Path(manifest['source'])
assert hashlib.sha256(src.read_bytes()).hexdigest()==manifest['sha256']
pages=[unicodedata.normalize('NFKC',x.extract_text() or '') for x in PdfReader(src).pages]
def quote(page,text):
    assert ' '.join(text.split()) in ' '.join(pages[page-1].split()), (page,text)
    return {'pdf_page':page,'quote':text}
previous=json.loads((p/'history/specific-v2/data.json').read_text(encoding='utf-8'))
reserved=json.loads((p/'history/specific-v2/reserve-examples.json').read_text(encoding='utf-8'))
items=previous['items']+reserved['items']
by={x['id']:x for x in items}
refs=json.loads((root/'curriculum-review-2026-09-06/curriculum-reference-records.json').read_text(encoding='utf-8'))
def comprehension(column,skill):
    row=next(x for x in refs if x['reference_id']==f'Comprehension_Throughlines_Victorian_English_2.0:table3:column{column}')
    assert skill in row['key_skills']
    return {'text':skill,'source':row['source_file'],'reference_id':row['reference_id'],'sha256':row['source_sha256']}
def add(id,title,category,year,curriculum,text,excerpts,relation='demonstrates'):
    item={'id':id,'title':title,'category':category,'year':year,'minutes':'20–30 minutes · Suggested teaching time','curriculum':curriculum,'text':text,'book_evidence':excerpts,'relation':relation}
    items.append(item);return item

by['word-choice-arrival']['book_evidence']=[quote(2,'He flickers through the trees like a tongue of fire, and Magpie trembles.')]
by['word-choice-arrival']['text']=by['word-choice-arrival']['text'].replace('Fox’s first arrival in the bush:', 'PDF page 2, Fox’s first arrival in the bush:')
by['voice-opening']['book_evidence']=[quote(1,'with a bird clamped in his big, gentle mouth.')]
by['voice-opening']['text']=by['voice-opening']['text'].replace('The opening rescue:', 'PDF page 1, the opening rescue:')
by['inference-final-cry']['book_evidence']=[quote(4,'She cannot tell if it is a scream of triumph or despair.')]
by['inference-final-cry']['text']=by['inference-final-cry']['text'].replace('Fox’s departure after abandoning Magpie,','PDF page 4: Fox’s departure after abandoning Magpie,').replace('Revisit Brooks’ illustration of the departure and discuss whether it strengthens or complicates their reading; do not assume an unseen visual detail.','Use Fox’s final statement about making Dog and Magpie know loneliness alongside his earlier watching and persuasion. How does each clue support or complicate the interpretation?')
by['determination-home']['book_evidence']=[quote(4,'Slowly, jiggety-hop, she begins the long journey home.')]
by['determination-home']['text']=by['determination-home']['text'].replace('The ending:', 'PDF page 4, the ending:')
by['inquiry-mutual-help']['title']='Identity and wellbeing: what can we make possible together?'
by['inquiry-mutual-help']['book_evidence']=[quote(2,'I will be your missing eye, and you will be my wings.')]
by['inquiry-mutual-help']['text']=by['inquiry-mutual-help']['text'].replace('Dog runs with Magpie on his back;', 'PDF page 2: Dog runs with Magpie on his back;').replace('her eventual decision to start home.', 'her eventual decision to start home on PDF page 4.')

add('organisation-pacing','Organisation: seasons in a sentence, seconds held still','Writing','Year 3',
{'text':'I can include spotlights and speed throughs in my text to highlight key ideas and pace.','source':'Recovered Organisation Year 3 skill, FOX-REVIEW.md W3 and original prototype.','reference_id':'FOX-REVIEW:W3'},
'''WHERE TO LOOK
PDF page 2: Dog and Magpie’s daily runs are compressed into the sentence that moves through summer and winter. Compare PDF page 3: after Fox’s rapid run into the desert, he stops; the narration dwells on stillness before he shakes Magpie off.

WHAT THE WRITING DEMONSTRATES
The amount of story time covered is different from the amount of reading time given to it. Months of an established routine pass quickly. A few seconds at a turning point receive several separate statements. The contrast makes the pause conspicuous and can build anticipation before the betrayal.

TEACH THROUGH THE CONTRAST
Read the seasonal summary, then the desert sequence. Ask students to estimate the time passing in each and compare how much attention the writing gives it. Underline the rapid movement verbs before the stop. Then examine “Neither moves, neither speaks.” What does the repetition and absence of action make us wait for?

TRANSFER TO STUDENTS’ WRITING
Students choose a turning point in their own narrative. Compress the routine leading up to it, then linger on a pause, gesture or thought before the change. They explain why that moment deserves the reader’s attention.

NOTICE LEARNING
Students distinguish passing time from reading time and vary the detail deliberately. Short sentences alone do not prove that a writer is speeding up; here they can hold our attention on stillness.''',
[quote(2,'every day, through summer, through winter.'),quote(3,'He stops, scarcely panting. There is silence between them. Neither moves, neither speaks.')])

add('connections-reciprocity','Making connections: the promise of eyes and wings','Reading','Year 4',
comprehension(5,"I can explain how a text's message connects to life or experience."),
'''WHERE TO LOOK
PDF page 2: after riding on Dog’s back, Magpie offers to be his missing eye and calls him her wings. On page 3 she repeats this promise while refusing Fox, then changes her mind.

WHY THIS IS A STRONG CONNECTION OPPORTUNITY
The promise gives a precise representation of mutual support: each contributes something the other needs. Connecting that relationship with a familiar example of interdependence can deepen students’ understanding of why leaving matters. The connection should explain the text, rather than become an unrelated story about a pet or a friend.

TEACH THROUGH THE PROMISE
Ask: “What can they do together that would be harder alone?” Consider a hypothetical partnership, such as two students completing a task using different strengths. Map what each contributes, then return to the repeated promise: how does understanding dependence help explain its importance and the cost of breaking it? Identify a difference between the hypothetical example and the story as well as a similarity. Personal disclosure is optional.

NOTICE LEARNING
Students explain how the connection changes their understanding of the promise. A relevant response returns to Dog and Magpie and cites their words or actions; it does more than identify a shared theme.''',
[quote(2,'I will be your missing eye, and you will be my wings.'),quote(3,'I will never leave Dog. I am his missing eye, and he is my wings.')])

add('synthesis-flying','Synthesising: what changes about “flying”?','Reading','Year 3',
comprehension(4,'I can synthesise prior knowledge and new information.'),
'''WHERE TO LOOK
PDF page 2: Magpie celebrates running with Dog as flying. Page 3: after Fox’s persuasion, she dismisses that experience, then celebrates Fox’s speed as real flying. Page 4: despite that exhilarating ride, she is abandoned and starts home towards Dog.

WHY SYNTHESIS MATTERS HERE
The repeated idea takes on different meanings as new events unfold. An early reading might understand flying as freedom restored through friendship. Later language makes speed seem like the missing answer. The ending challenges that account of what Magpie needs. Bringing these stages together can produce a more complex understanding than retelling one event or declaring a single moral.

TEACH THROUGH THE CHANGING LANGUAGE
At each point, record “What might flying mean to Magpie now?” and a supporting phrase. After the ending, revisit the earlier responses: what new information changes or complicates them? Ask students to develop an explanation that draws on at least two stages. They may interpret the changing need differently if they support the reading.

NOTICE LEARNING
Students explain how later evidence revises an earlier understanding. Listing three events in order is retelling; synthesis explains the new understanding that comes from considering them together.''',
[quote(2,'FLY, DOG, FLY!'),quote(3,'This is nothing like flying. Nothing!'),quote(3,'At last I am flying. Really flying!')])

pride=json.loads((root/'mentor-database-recovery-2026-09-05/data/pride_values.json').read_text(encoding='utf-8'))
integrity=next(x for x in pride if x['slug']=='integrity')
add('integrity-promises','Integrity: promises and choices when Dog is absent','PRIDE','Discussion through a counterexample',
{'text':integrity['one_liner'],'source':'Recovered Ngarri PRIDE reference: Integrity.','reference_id':'pride_values:integrity'},
'''WHERE TO LOOK
PDF page 3: Fox approaches when Dog is asleep or away. Magpie twice promises that she will never leave Dog, then agrees to go. On page 4 Fox declares that Dog and Magpie will now know loneliness.

HOW THIS HELPS TEACH INTEGRITY
This is a discussion of a value through choices that undermine it, rather than an example of Fox demonstrating integrity. The contrast between a stated commitment and a later action makes honesty, fairness and responsibility concrete. Dog’s absence also makes the question of conduct without an observer relevant.

TEACH THROUGH THE DECISIONS
Place Magpie’s repeated promise beside her later agreement. Ask what changed, who is affected, and whether explaining a choice is the same as justifying it. Examine Fox’s timing and final statement separately: what do these suggest about the purpose of his approach? Students propose a more honest or fair alternative at one decision point and explain the difference.

NOTICE LEARNING
Students use a specific action to explain the value and distinguish understanding a motive from excusing harm. The ending suggests a first step towards Dog; it does not show an apology, forgiveness or completed repair.

CONNECTION TYPE
Counterexample for discussion. Do not present this as a positive example of a character embodying integrity.''',
[quote(3,'I will never leave Dog.'),quote(3,'I am ready.'),quote(4,'Now you and Dog will know what it is like to be truly alone.')],relation='counterexample_for_discussion')

lenses=json.loads((root/'mentor-database-recovery-2026-09-05/data/inquiry_lenses.json').read_text(encoding='utf-8'))
social=next(x for x in lenses if x['slug']=='social_responsibility')
add('inquiry-responsibility','Social responsibility: who is affected by a private choice?','Inquiry','Class suitability to review',
{'text':social['description'],'source':'Recovered Ngarri inquiry lens: Social Responsibility.','reference_id':'inquiry_lenses:social_responsibility'},
'''WHERE TO LOOK
PDF page 2: Dog offers Fox food and shelter. Page 3: Fox persuades Magpie when Dog is absent. Page 4: Fox explicitly includes Dog in the loneliness he intends, and Magpie thinks of Dog waking to find her gone before she starts home.

WHY THIS OPENS A DISTINCT INQUIRY
Choices between two characters affect a third who is not present. That gives the class a concrete way into responsibility and interdependence, beyond the individual wellbeing focus of the other lens.

SUGGESTED QUESTION
“What responsibilities do we have to people affected by our choices?” This is a draft inquiry question, not a quotation from the school framework.

TEACH THROUGH THE CHAIN OF CONSEQUENCES
In Tuning In, ask whose interests are present in each decision and whose voice is absent. In Sorting Out, draw a consequence map from one choice to its effects on all three characters. Separate what the story confirms from what students imagine Dog may feel. Revisit the ending: why might thinking about someone who is not there change a decision?

WHERE IT MIGHT LEAD
Students can explore a hypothetical shared-resource or group-work decision, then reconsider their ideas about responsibility. Let their questions determine the next investigation; this book does not need to supply an entire inquiry unit.''',
[quote(2,'Welcome. We can offer you food and shelter.'),quote(4,'But then she thinks of Dog waking to find her gone.')],relation='inquiry_entry_point')

for item in items:
    item.pop('source_url',None)
    item.update(status='ai_suggested',source_type='ai_suggested',is_generic=False,confidence=None,
        evidence='Directly checked against the supplied four-page text-only PDF. Page numbers refer to this PDF, not a printed edition. Original illustrations and typography are not present. The teaching interpretation remains a draft for review.',
        provenance={'source_path':str(src),'source_sha256':manifest['sha256'],'source_type':'user_supplied_text_copy','review_scope':'All four pages read and visually inspected; no original illustrations supplied.'})
    item.setdefault('relation','demonstrates')
    item['source_label']='Fox Margaret Wild.pdf — supplied text copy'
    item['evidence']=' '.join([item['evidence'],'Located evidence:']+[f"PDF p. {e['pdf_page']}: {e['quote']}" for e in item['book_evidence']])
order=['voice-opening','word-choice-arrival','organisation-pacing','inference-final-cry','connections-reciprocity','synthesis-flying','determination-home','integrity-promises','inquiry-mutual-help','inquiry-responsibility']
items.sort(key=lambda x:order.index(x['id']))
data={'version':'fox-local-review-3-text-checked','book':previous['book'],'items':items,'source':manifest,'selection_rule':'Include every strong distinct supported connection; no minimum or maximum count. Integrity is explicitly a counterexample discussion, not a positive value annotation.'}
(p/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(items)==10 and all(x['book_evidence'] for x in items)
print('Built 10 individually supported connections; all quoted book excerpts checked against the supplied PDF.')
