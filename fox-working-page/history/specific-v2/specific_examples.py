"""Replace generic routines with located mentor-text examples; retain v1 as provenance."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent
old=json.loads((p/'history/generic-v1/data.json').read_text(encoding='utf-8'))
by_id={i['id']:i for i in old['items']}
publisher='https://s3-ap-southeast-2.amazonaws.com/dimo.allenunwin.com/assets/teaching_resource/9781864489330.pdf'
items=[]
def add(original_id,id,title,category,year,curriculum,text,evidence,minutes):
    item=dict(by_id[original_id]);item.update(id=id,title=title,category=category,year=year,curriculum=curriculum,text=text,evidence=evidence,minutes=minutes,source_url=publisher,status='ai_suggested',is_generic=False)
    item['provenance']={'draft_basis':'User-supplied fox-book-detail.html; extracted in prior-prototype-text.txt','verification':'Publisher notes checked for the stated story moments. Interpretations and lesson designs are new review drafts. Whole classroom edition has not been inspected.','supersedes_generic_item':original_id}
    items.append(item)

add('writing','word-choice-arrival','Fox’s arrival: words that make us wary','Writing','Year 3',by_id['writing']['curriculum'],
'''WHERE TO LOOK
Fox’s first arrival in the bush: the description of his eyes and the comparison of his movement to a “tongue of fire”.

WHAT MAKES THIS A MENTOR-TEXT EXAMPLE
Wild does more than tell us a new animal has arrived. The fire image connects his movement with something vivid, attractive and potentially destructive. “Haunted” gives his eyes an emotional history without explaining it. Students can investigate how a few choices build an impression of a character before his later actions unfold. These are interpretations to test against the passage.

TEACH THROUGH THE WRITING
Put this deliberately plain, teacher-written alternative beside the actual passage: “A fox came through the trees.” What information does it convey? What feeling and possible character clues does it lose? Compare the effect of “haunted” with the invented alternative “friendly”. Ask students to explain the difference, rather than list adjectives.

TRANSFER TO STUDENTS’ WRITING
Students introduce a character through a chosen movement and one revealing detail, without naming the character’s personality. A partner explains the impression created and identifies the words responsible.

NOTICE LEARNING
The student links a particular word or image to an effect on the reader and makes a purposeful choice in their own writing.''',
'Prototype: Word Choice Year 3 and Tone Through Word Choice. Cross-check: publisher notes p. 8; editor’s account pp. 11–12 confirms the deliberate choice of the eye description. The plain sentence and “friendly” comparison are new teaching examples, not book quotations. Curriculum wording remains the recovered W2 excerpt.',
'20 minutes · Model, then pairs')

add('inference','inference-final-cry','Fox’s final cry: triumph, despair, or both?','Reading','Year 4',by_id['inference']['curriculum'],
'''WHERE TO LOOK
Fox’s departure after abandoning Magpie, when his cry is heard across the desert. Revisit this alongside his earlier approach to Dog and Magpie and what he does before leaving.

WHY INFERENCE MATTERS HERE
Hearing a cry does not settle what it means. Triumph and despair suggest different understandings of Fox: satisfaction at hurting others, pain associated with isolation, or an uneasy combination. Students need to connect the sound with his actions and relationships. Their task is to justify an interpretation, not to diagnose him or guess an answer held by the teacher.

TEACH THROUGH THE BOOK
Ask: “Which reading of the cry can you support, and what makes the other reading possible?” Make two columns: what the book shows or says; what we infer. Students place a relevant action or line in the first column before offering an interpretation in the second. Revisit Brooks’ illustration of the departure and discuss whether it strengthens or complicates their reading; do not assume an unseen visual detail.

NOTICE LEARNING
Students connect a specific clue to their explanation and can acknowledge uncertainty. A response that merely labels Fox ‘bad’ has not yet explained the cry.''',
'Prototype: What Does Fox’s Cry Mean? Publisher notes pp. 6–7 support the competing interpretation of the cry. New curriculum source explicitly places this traits/motives/perspectives skill in Year 4. Removed the old draft’s unsupported speech count and references to Kookaburra.',
'20 minutes · Pairs and discussion')

add('pride','determination-home','Magpie begins the journey home','PRIDE','Class suitability to review',by_id['pride']['curriculum'],
'''WHERE TO LOOK
The ending: Magpie is alone in the desert. Thinking of Dog precedes her decision to begin the long journey home. Locate the final movement described as “jiggety-hop”.

HOW THE MOMENT SHOWS DETERMINATION
The useful example is the decision to start while the difficulty remains. Magpie has not suddenly recovered her ability to fly, and the book does not need to show an easy or completed return for the choice to matter. This makes the difference between experiencing a setback and responding to one visible. It supports the resilience aspect of Ngarri’s definition, rather than every part of it.

TEACH THROUGH THE WORDS AND ACTION
Ask: “What is still difficult for Magpie? What changes between remaining there and taking the first step?” Revisit the shift from her thoughts to her movement. Discuss how the small, awkward movement makes effort perceptible. Contrast starting a difficult task with already having succeeded: which does this ending actually show?

NOTICE LEARNING
Students explain determination using Magpie’s obstacle, decision and action. ‘She is determined because she keeps trying’ is a starting point; ask what she actually decides to do and why that costs effort.''',
'Prototype: Determination ending example. Publisher notes pp. 6 and 8 confirm the decision to start home after thinking of Dog. The short movement quotation is retained from the supplied prototype; check its exact spelling in the classroom edition. No successful reunion is asserted.',
'15 minutes · Shared reading and discussion')

add('writing','voice-opening','A frightening setting, a gentle rescuer','Writing','Year 3',
{'text':'I can create an identifiable tone such as compassionate, bittersweet, frustrated or terrified.','source':'Recovered Year 3 Voice / Audience reference, FOX-REVIEW.md W1; also present in supplied prototype.','reference_id':'FOX-REVIEW:W1'},
'''WHERE TO LOOK
The opening rescue: Dog carries the injured Magpie through the burnt forest. Compare the language of heat and damage with the description of his mouth as gentle.

WHAT THE WRITING DEMONSTRATES
Danger in the setting sits beside care in Dog’s action. That contrast gives students something concrete to investigate: a scene can feel frightening and compassionate at once. The mood is constructed through selected details, rather than an instruction telling readers what to feel.

TEACH THROUGH THE PASSAGE
Read the opening and collect the exact words that suggest danger separately from those that suggest care. Ask: “What would change if we removed the detail that makes Dog seem gentle?” Students explain how a small detail changes their reading of an animal carrying an injured bird in his mouth.

TRANSFER TO STUDENTS’ WRITING
Students write a short moment of help in an unsettling setting. They choose one setting detail and one caring action, then ask a reader to explain the resulting mood using those words as evidence.

NOTICE LEARNING
Students explain how contrasting details shape a tone. They do not need to claim that the whole book maintains one unchanging mood.''',
'New located refinement of the prototype’s Voice / Audience idea. Opening passage reproduced in publisher notes p. 6. The interpretation and transfer task are new drafts. This replaces the sweeping claim of one tone sustained throughout the whole book.',
'20 minutes · Shared analysis and individual writing')

add('inquiry','inquiry-mutual-help','Dog and Magpie: what can we make possible together?','Inquiry','Class suitability to review',by_id['inquiry']['curriculum'],
'''WHERE TO LOOK
Dog runs with Magpie on his back; compare this partnership with Magpie’s later choice to leave with Fox and her eventual decision to start home.

WHY THIS OPENS AN INQUIRY
The first partnership gives us a concrete case of people—or characters—making something possible together. The later choices complicate an easy conclusion that friendship simply solves everything. This offers a starting point within Identity, Creativity and Wellbeing: mutual support, belonging and choices in relationships.

SUGGESTED QUESTION
“What makes a relationship supportive?” This is a question for the class to investigate, not official school wording or a conclusion already settled for them.

TEACH THROUGH THE CONTRAST
In Tuning In, revisit the running partnership and ask what each character contributes and gains. Gather students’ questions. In Sorting Out, compare that relationship with the Fox episode: what actions support another character, and what actions serve one character at another’s expense? Require a story example for each suggestion.

WHERE IT MIGHT LEAD
Students can reconsider their initial ideas about support after comparing the moments. Let their questions shape any further inquiry; avoid reducing the story to a single prescribed moral.''',
'Refines the prototype’s Identity, Creativity and Wellbeing entry without claiming that Magpie’s identity is destroyed or rebuilt from nothing. Publisher notes pp. 6–8 corroborate the running partnership, departure and decision to return. The inquiry question and teaching interpretation are new drafts.',
'20 minutes · Inquiry discussion')

for item in items:
    assert all(h in item['text'] for h in ['WHERE TO LOOK','NOTICE LEARNING'] if item['category']!='Inquiry')
selected_ids={'word-choice-arrival','inference-final-cry','determination-home'}
reserve=[i for i in items if i['id'] not in selected_ids]
(p/'reserve-examples.json').write_text(json.dumps({'status':'held_back_not_selected_for_page','reason':'Select the strongest examples, with no requirement to cover every domain. Retain alternatives as working notes.','items':reserve},ensure_ascii=False,indent=2),encoding='utf-8')
items=[i for i in items if i['id'] in selected_ids]
data={'version':'fox-local-review-2-specific', 'book':old['book'], 'items':items,'previous_version':'fox-local-review-1','retired_generic_items':['prediction','speaking','vocabulary','fluency'],'revision_reason':'User correction: select only the best located mentor-text examples; no category or year-level quotas.'}
(p/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Prepared {len(items)} located mentor-text examples. Previous fixture retained in history/generic-v1.')
