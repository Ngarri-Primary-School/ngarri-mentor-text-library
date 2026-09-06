"""Build a local review fixture from preserved curriculum records; no database writes."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
refs = json.loads((ROOT / 'curriculum-review-2026-09-06/curriculum-reference-records.json').read_text(encoding='utf-8'))
def ref(prefix, table, column, skill):
    row = next(r for r in refs if r['reference_id'] == f'{prefix}:table{table}:column{column}')
    assert skill in row['key_skills']
    return {'text': skill, 'source': row['source_file'], 'reference_id': row['reference_id'], 'sha256': row['source_sha256']}
C = 'Comprehension_Throughlines_Victorian_English_2.0'
S = 'Speaking_and_Listening_Throughlines_Victorian_English_2.0'
F = 'Phonics_Fluency_Decoding_Vocabulary_Throughlines_Condensed_Same_Format'
items = [
    dict(id='prediction', category='Reading', title='Revise a prediction', year='Year 3', minutes='15 minutes · Shared reading',
         curriculum=ref(C,3,4,'I can confirm or modify predictions using evidence.'),
         text='Learning intention: Explain why we keep or change a prediction.\n\nPause at a teacher-selected moment during a first reading. Students predict what might happen and identify a clue. Read further, then revisit predictions and explain what the new evidence changes.\n\nNotice learning: Students explain a confirmation or revision using relevant evidence. Guessing correctly is not the success criterion.\n\nIf students already know the ending, use an unfamiliar text to assess prediction.',
         evidence='New curriculum addendum, pathway A. A reusable routine; a suitable stopping point in Fox still needs selection. This is not a verified claim that prediction is a distinctive strength of the book.'),
    dict(id='inference', category='Reading', title='Evidence, interpretation, alternative', year='Year 4', minutes='20 minutes · Pairs and discussion',
         curriculum=ref(C,3,5,'I can infer character traits, motives and perspectives using evidence.'),
         text='Learning intention: Explain an interpretation of a character using clues.\n\nRevisit a teacher-selected spread. Model separating observation from interpretation. Partners propose a motive or perspective, point to supporting clues, and consider another possible interpretation. Discuss which explanation the evidence supports and what remains uncertain.\n\nNotice learning: Students support an inference with words or image details and consider an alternative.',
         evidence='Original Fox review R1/T2 and new addendum pathway B. The new source places this wording in Year 4; the older recovered Year 3 reference is preserved separately. Select and verify the actual spread.'),
    dict(id='speaking', category='Speaking and listening', title='Build on a partner’s thinking', year='Year 3', minutes='Within a class discussion',
         curriculum=ref(S,1,4,"I can confirm, build on and prompt others' ideas."),
         text='Learning intention: Respond to another person’s idea before adding our own.\n\nWithin a discussion of a selected spread, model “I would add … because …” and “What makes you think …?” Students practise building on or questioning a partner’s interpretation.\n\nNotice learning: The response connects to what the partner actually said. Sentence frames are optional support.',
         evidence='New curriculum addendum, speaking and listening. Generic discussion scaffold; the reviewer must select a suitable book discussion.'),
    dict(id='vocabulary', category='Vocabulary', title='Investigate a word in context', year='Year 3', minutes='10 minutes · Shared investigation',
         curriculum=ref(F,4,4,'I can use context and word parts to infer meaning.'),
         text='Learning intention: Use clues to investigate an unfamiliar word.\n\nSelect a word from the actual text. Students propose a meaning using the surrounding language. Examine useful word parts where the word supports this, check the meaning and reread.\n\nNotice learning: Students explain which clues helped and revise their thinking when needed. If the word has no useful word-part example, this activity practises only the contextual part of the skill.',
         evidence='New curriculum addendum, vocabulary. Word and passage selection pending. No example words have been invented.'),
    dict(id='fluency', category='Fluency', title='Read with meaning', year='Year 3', minutes='10 minutes · Supported excerpt practice',
         curriculum=ref(F,3,4,'I can adjust pace, pitch, tone and expression using punctuation.'),
         text='Learning intention: Use our voice to convey meaning.\n\nChoose a short, accessible excerpt. Model phrasing, then support students to rehearse an expressive reading. Compare two readings and explain how punctuation and meaning informed one adjustment.\n\nNotice learning: Phrasing or expression responds to punctuation and understanding. This is supported excerpt practice, not a claim that the whole book is independently readable or decodable for Year 3.',
         evidence='New curriculum addendum, fluency. Accessible excerpt selection pending.'),
    dict(id='writing', category='Writing', title='Change two words, explain the effect', year='Year 3 candidate', minutes='20 minutes · Model, then pairs',
         curriculum={'text':'I can choose specific words and phrases for a desired effect.', 'source':'Recovered school reference quoted in FOX-REVIEW.md, W2; original school PDF comparison pending.', 'reference_id':'FOX-REVIEW:W2'},
         text='Learning intention: Explain the effect of a word choice.\n\nRevisit a selected passage. Model replacing two words with alternatives and discuss how the effect changes. Pairs try another replacement and explain their choices. Students then revise a sentence from their own writing for a chosen effect.\n\nNotice learning: Students explain what a word does for the reader, rather than just calling it a better word.',
         evidence='Original Fox review W2/T1. The reviewer must check the source curriculum wording and the passage before approving this candidate. The prototype’s separate spotlight/pacing claim remains pending and is not included.'),
    dict(id='pride', category='PRIDE', title='Determination', year='Class suitability to review', minutes='Discussion connection',
         curriculum={'text':'We show determination by using a growth mindset to overcome challenges, and use new and innovative ways to achieve our personal best.', 'source':'Recovered Ngarri definition quoted in FOX-REVIEW.md, P1.', 'reference_id':'FOX-REVIEW:P1'},
         text='Possible connection: Magpie’s decision to begin returning to Dog offers a resilience connection.\n\nRevisit the decision and discuss what students notice about responding to a setback. Ask them to point to evidence for their interpretation.\n\nThis candidate addresses resilience; it does not establish every part of Ngarri’s Determination definition.',
         evidence='Original Fox review P1. Confirm the event in the classroom copy and the exact school definition. No additional Integrity tag has been inferred.'),
    dict(id='inquiry', category='Inquiry', title='Relationships and choices', year='Class suitability to review', minutes='10–20 minutes · Discussion',
         curriculum={'text':'This lens focuses on how we can work towards our potential, develop resilience, build healthy relationships and make wise choices.', 'source':'Recovered Ngarri Identity, Creativity and Wellbeing lens excerpt, FOX-REVIEW.md I1.', 'reference_id':'FOX-REVIEW:I1'},
         text='Possible inquiry question: How can our choices strengthen or damage a friendship?\n\nTuning In: Following an initial reading, gather students’ questions about the relationships. Group related questions and invite students to choose what they would like to investigate.\n\nSorting Out: Revisit two selected moments. Partners record a character choice, evidence and their interpretation of its effect on a relationship. Compare interpretations and identify further questions.\n\nListen for: Students distinguish events from interpretations and consider another perspective. Let their questions shape what comes next. A full inquiry unit or personal disclosure is not required.',
         evidence='Original Fox review I1, superseded by the inquiry addendum. The question is newly drafted, not official school wording. The lens, question and selected moments all need review.')
]
for item in items:
    item.update(status='ai_suggested', source_type='ai_suggested', confidence=None, confidence_note='Not scored; evidence limitations are listed for review.')
data = {'version':'fox-local-review-1', 'book':{'id':'fox-calibration', 'title':'Fox', 'author':'Margaret Wild', 'illustrator':'Ron Brooks'}, 'items':items}
(Path(__file__).parent/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Prepared {len(items)} unapproved review items; verified five curriculum quotations.')
