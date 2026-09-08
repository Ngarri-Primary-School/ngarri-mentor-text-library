-- Teacher-approved replacement content for The Alphabet Tree.
-- Approved by Phill in conversation on 9 September 2026.
-- Earlier teacher-reviewed rows are retained as rejected/superseded provenance.

begin;

do $block$
declare
  v_book_id uuid;
begin
  select id into strict v_book_id
  from public.books
  where title = 'The Alphabet Tree' and status = 'active';

  update public.writing_trait_annotations
  set status = 'rejected',
      source_name = 'Superseded teacher-reviewed pilot record; retained for provenance'
  where book_id = v_book_id and status = 'teacher_reviewed';

  update public.reading_strategy_annotations
  set status = 'rejected',
      source_name = 'Superseded teacher-reviewed pilot record; retained for provenance'
  where book_id = v_book_id and status = 'teacher_reviewed';

  update public.pride_value_annotations
  set status = 'rejected'
  where book_id = v_book_id and status = 'teacher_reviewed';

  update public.inquiry_lens_annotations
  set status = 'rejected'
  where book_id = v_book_id and status = 'teacher_reviewed';

  update public.teaching_ideas
  set status = 'rejected'
  where book_id = v_book_id and status = 'teacher_reviewed';

  insert into public.writing_trait_annotations
    (book_id, trait_slug, year_level, applicable_year_levels, key_understanding_text, key_skill_text,
     in_this_book_text, book_evidence, source_type, source_name, confidence, status,
     reviewed_by, reviewed_at, display_order)
  values
    (v_book_id,'organisation','Year 2','Year 2',
     'how different types of texts are organised differently',
     'I can include my ideas in a logical sequence.',
     $$Lionni makes the sequence easy to trace: the storm scatters the letters; the word-bug teaches them to combine into words; the caterpillar asks the words to form sentences; the letters choose an important message; and the caterpillar carries it to a named audience. Students can explain how each event prepares the next one, then use a similarly logical chain in their own narrative.$$
     ,$$The storm, the word-bug's lesson, the caterpillar's challenge, the chosen message and the final journey.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),21),
    (v_book_id,'organisation','Year 3','Year 3',
     'different text types have different language features and structures to suit purpose.',
     'I can describe the structure of different text types.',
     $$The narrative structure also explains an idea. The opening happiness and sudden gale establish the problem; the word-bug provides a first solution; the caterpillar sets a more demanding challenge; and the final journey turns language into action. Students can describe how this beginning, problem, linked solutions and ending allow a story to entertain while explaining how written language builds meaning.$$
     ,$$The opening, gale, first solution, harder challenge and final journey.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),22),
    (v_book_id,'organisation','Year 4','Year 4',
     'different text types have different structures to suit the purpose',
     'I can identify/explain the organisational features of a range of texts.',
     $$Lionni uses a cumulative challenge–instruction–transformation pattern. The letters first learn that grouping creates physical strength, then that words must be organised into sentences, and finally that a sentence can carry an important purpose. Students can identify this repeated pattern and explain how it teaches a hierarchy of language without interrupting the narrative.$$
     ,$$The repeated challenges and transformations from letters to words, sentences and message.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),23),
    (v_book_id,'organisation','Year 5','Year 5',
     'there are a range of devices used to create cohesion in a text',
     'I can use a range of devices to create cohesion within a text. (synonyms, cause and effect, conditionals).',
     $$Cause and effect holds the whole narrative together: the gale causes fear and scattering; joining creates strength; making sentences creates meaning; and selecting a message creates a reason to travel. The recurring progression from letters to words to sentences to message also forms a lexical chain. Students can trace these devices and use recurrence and cause and effect to make their own text cohere.$$
     ,$$The cause-and-effect chain and the recurring progression from letters to words to sentences to message.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),24),

    (v_book_id,'ideas','Year 2','Year 2',
     'ideas are used to convey meaning',
     'I can elaborate on at least one idea.',
     $$Lionni begins with one idea—individual letters become stronger together—and elaborates it in stages. Togetherness first protects the letters from the wind, then allows them to make meaning, and finally gives them a shared public purpose. Students can notice how each stage adds something new to the original idea and plan two or three details that develop one idea of their own.$$
     ,$$Togetherness develops from physical protection to shared meaning and public purpose.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),11),
    (v_book_id,'ideas','Year 3','Year 3',
     'ideas and details from mentor texts help when creating written and spoken texts',
     'I can create related ideas that are clear, coherent and in a logical sequence.',
     $$The vulnerable letters, the word-bug's lesson, the caterpillar's challenge and the journey to the President are related ideas rather than separate episodes. Each changes what the letters understand and can do. Students can borrow this staged pattern from Lionni to create a sequence in which a character's learning develops through connected events.$$
     ,$$The linked stages of vulnerability, teaching, challenge and purposeful journey.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),12),
    (v_book_id,'ideas','Year 4','Year 4',
     'how details support my idea',
     'I can elaborate on an idea using details.',
     $$The letters can already make correct statements about the wind, leaves and word-bug, but the caterpillar presses them to say something important. These deliberately limited examples help readers see the difference between supplying details and choosing details that develop a worthwhile idea. Students can test each detail in their own writing by asking what it helps the reader understand.$$
     ,$$The early sentences about the tree world compared with the caterpillar's demand for an important message.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),13),
    (v_book_id,'ideas','Year 5','Year 5',
     'how relevant details and elaborations support my idea',
     'I can use relevant details to elaborate on an idea.',
     $$Lionni selects only events that sharpen the central movement from cooperation for safety to communication for social purpose. The gale, the groupings, the first simple sentences, the demand for importance and the final destination all contribute; an unrelated adventure would weaken the design. Students can rank possible details by relevance and retain those that extend the intended meaning.$$
     ,$$The gale, groupings, simple sentences, demand for importance and final destination.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),14),

    (v_book_id,'presentation','Year 2','Year 2',
     'visuals can enhance my writing',
     'I can use different types of visuals to enhance my presentation with my audience in mind (e.g diagram, pictures, caption)',
     $$The illustrations make an abstract progression visible. Separate letters appear vulnerable, grouped letters become readable words, and ordered words become sentences and a message. Students can explain what the images teach that the narration alone would make harder to see, then choose a visual arrangement that clarifies an idea in their own work.$$
     ,$$Compare the separate letters, readable word groups, sentences and final message.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),71),
    (v_book_id,'presentation','Year 3','Year 3',
     'that a visuals can enhance my writing',
     'I can include visuals to enhance the understanding and effect of my writing.',
     $$Lionni changes the visual arrangement as the letters' understanding changes. Scattered symbols create disorder, while recognisable groupings let the reader experience increasing order and shared strength. Students can compare two contrasting spreads and explain how layout and illustration change both understanding and effect.$$
     ,$$Contrast a spread of scattered letters with one showing recognisable groupings.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),72),
    (v_book_id,'presentation','Year 5','Year 5',
     'visuals can enhance my writing',
     'I can include relevant illustrations, labelled diagrams, graphs, charts or tables to enhance my writing.',
     $$The images do conceptual work: the characters remain alphabet letters while their physical arrangement represents word and sentence structure, cooperation and collective voice. Students can evaluate why this visual metaphor belongs in the book and design an illustration or diagram that carries part of an idea rather than merely decorating the text.$$
     ,$$The letters remain characters while their arrangement represents linguistic structure and collective voice.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),73),

    (v_book_id,'voice_audience','Year 1','Year 1',
     'I am writing for a purpose and intended audience.',
     'I can describe the audience and purpose of my writing.',
     $$The letters eventually choose both an audience—the President—and a purpose—to carry a message about peace and goodwill. Students can name who the message is for and what the writers want it to achieve, then choose an audience and purpose before composing a short message of their own.$$
     ,$$The letters choose the President as audience and peace and goodwill as their purpose.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),31),
    (v_book_id,'voice_audience','Year 2','Year 2',
     'I am writing for a purpose and intended audience (express an opinion, explore an idea, narrate)',
     'I can explain that an author writes for one of the following purposes: to persuade, to inform, to entertain',
     $$Lionni's whole work is a narrative that entertains and explores an idea, while the sentence created inside the story is intended to influence a public leader. Students can compare these two layers, explain how their purposes differ and decide whether their own writing is meant to entertain, inform or persuade.$$
     ,$$Compare the purpose of Lionni's narrative with the purpose of the message inside it.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),32),
    (v_book_id,'voice_audience','Year 3','Year 3',
     'I am writing for a purpose and intended audience (express an opinion, explore an idea, narrate)',
     'I can write with a specific reader or audience in mind.',
     $$The caterpillar shifts the letters from making statements about nearby objects to creating a message for someone with public power. Naming the President as audience changes what is worth saying and why the message must travel. Students can revise a general statement for a specific recipient and explain which choices changed.$$
     ,$$The shift from statements about nearby objects to a message for the President.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),33),

    (v_book_id,'word_choice','Year 2','Year 2',
     'word choices enhance the reader''s experience',
     'I can identify and use memorable words and phrases.',
     $$The movement from breeze to strong gust to gale intensifies the weather in three memorable steps. The choices build sound, rhythm and danger more effectively than repeating a general word such as wind. Students can order words by intensity and select a progression that lets a reader feel a change.$$
     ,$$The weather intensifies from breeze to strong gust to gale.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),41),
    (v_book_id,'word_choice','Year 3','Year 3',
     'word choices are selected and refined, allowing the writer to communicate a message clearly',
     'I can choose specific words and phrases for a desired effect.',
     $$The letters' early sentences are meaningful but limited; their final choice, “PEACE ON EARTH AND GOODWILL TOWARD ALL MEN,” is selected to influence a powerful audience. Students can compare a correct sentence with a purposeful one and refine words according to the effect they want their own message to have. Teachers can also discuss whether the historical expression all men now communicates the inclusive meaning it intends.$$
     ,$$Compare the early sentences with the final message selected for a powerful audience.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),42),

    (v_book_id,'sentence_fluency','Foundation','Foundation',
     'sentences are made up of words',
     'I can identify the words in my sentence.',
     $$The story makes the relationship among letters, words and sentences concrete: individual letters combine, spaces distinguish word groups, and the word groups are ordered to express an idea. Students can rebuild one short sentence with movable letters or word cards, identify each word and check that the complete sentence makes sense.$$
     ,$$The visible transformation from individual letters to word groups and a complete sentence.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),51)
  on conflict (book_id,trait_slug,year_level) do update set
    applicable_year_levels=excluded.applicable_year_levels,
    key_understanding_text=excluded.key_understanding_text,
    key_skill_text=excluded.key_skill_text,
    in_this_book_text=excluded.in_this_book_text,
    book_evidence=excluded.book_evidence,
    source_type=excluded.source_type,
    source_name=excluded.source_name,
    confidence=excluded.confidence,
    status=excluded.status,
    reviewed_by=excluded.reviewed_by,
    reviewed_at=excluded.reviewed_at,
    display_order=excluded.display_order;

  insert into public.reading_strategy_annotations
    (book_id, strategy_slug, year_level, applicable_year_levels, key_understanding_text, key_skill_text,
     in_this_book_text, book_evidence, source_type, source_name, confidence, status,
     reviewed_by, reviewed_at, display_order)
  values
    (v_book_id,'synthesising','Year 2','Year 2',
     'That synthesis is when we use our prior knowledge and the text to build deeper understandings. (Synthesising)',
     'I can identify how the new knowledge developed my thinking. (synthesising)',
     $$After the word-bug's lesson, readers may understand together mainly as physical safety because grouped letters withstand the wind. The caterpillar's challenge adds meaning and the final journey adds public purpose. Students can pause after each stage and state how the new event changes or enlarges their first understanding of what being together can achieve.$$
     ,$$Pause after the letters form words, after they form sentences and when their destination is revealed.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),51),
    (v_book_id,'synthesising','Year 3','Year 3',
     'Synthesising helps us develop new understandings of a topic or subject.',
     'I can identify what was new information and how I now better understand my topic/subject.',
     $$Readers combine the complete sequence to develop a more complex understanding of written communication: knowing letters is only a beginning; words carry ideas, sentences organise meaning, and audience and purpose make language consequential. Students can compare an early statement about how writing works with a revised statement after the final destination is revealed.$$
     ,$$Use the complete progression from letters to a purposeful message for a public audience.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),52),

    (v_book_id,'determining_importance','Year 2','Year 2',
     'The main idea of the text is most important point/part the author wants us to understand',
     'I can identify and justify what the main idea of the text is.',
     $$The text contains many true details about wind, leaves and insects, yet the caterpillar distinguishes a sentence that merely says something from one that matters. Students can propose the story's main idea and justify it with the letters' movement from isolation to cooperation, then from cooperation to purposeful communication.$$
     ,$$Compare true details about the tree world with the story's complete development.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),21),
    (v_book_id,'determining_importance','Year 3','Year 3',
     'Summaries are more precise when we retell only the most important ideas, events or details',
     'I can identify important and un-important ideas, events or details',
     $$A precise summary needs the gale, the word-bug, the caterpillar's challenge, the chosen message and its destination because each changes what the letters can do. Details such as the appearance of a particular leaf may be memorable but are unnecessary unless they support the summary's purpose. Students can justify every retained or omitted detail.$$
     ,$$Sort the major turning points and minor visual details according to their role in a concise summary.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),22),
    (v_book_id,'determining_importance','Year 4','Year 4',
     'The main and supporting ideas of a text help us identify and elaborate on our understanding of the text.',
     'I can identify the main idea of the text and their supporting details.',
     $$A defensible main idea is that shared language can turn separate voices into purposeful collective action. The letters' vulnerability when isolated, the strength gained through words, the move to meaningful sentences and the decision to address a leader all support it. Students can distinguish the sentence carried to the President from the broader idea developed by the whole narrative.$$
     ,$$The letters' isolation, grouping, meaningful sentences and decision to address a leader.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),23),

    (v_book_id,'analysing','Year 4','Year 4',
     'Different text types have typical stages and language features dependent on their purpose.',
     'I can explain how author''s use different literary devices to add to the meaning of the text. (grammar, word choices, free verse, symbolism, personification, metaphor etc.)',
     $$Lionni personifies alphabet letters as characters that fear, learn, cooperate and decide. Their literal arrangement into words and sentences becomes a metaphor for people combining their voices. Students can explain how personification lets the narrative demonstrate the mechanics of writing and the social meaning of cooperation at the same time.$$
     ,$$The personified letters behave as characters while also combining into written language.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),31),
    (v_book_id,'analysing','Year 5','Year 5',
     'Author''s use literary devices to shape the meaning of the text. (grammar, word choices, free verse, symbolism, personification, metaphor etc.)',
     'I can explain how author''s use different literary devices to add to the meaning of the text. (grammar, word choices, free verse, symbolism, personification, metaphor etc.)',
     $$The alphabet tree operates as an extended allegory. Separate letters can represent isolated individuals, their groupings suggest cooperation, the caterpillar demands purpose, and the President represents an audience able to act. Students can test an interpretation across this whole pattern, revising it when a symbolic claim fits only one detail.$$
     ,$$Test symbolic readings of the letters, their groupings, the caterpillar and the President across the whole story.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),32),
    (v_book_id,'analysing','Year 6','Year 6',
     'The text structures and language features of a text work together to meet the purpose of, engage and influence the audience.',
     'I can explain how the text structure and language features engage or influence the audience.',
     $$The repeated instruction-and-transformation structure, the escalating vocabulary of letters, words, sentences and message, the direct dialogue and the final public destination work together. They move the reader from a playful lesson about language to a claim that communication can influence the wider world. Students can explain how removing one of these elements would weaken that effect.$$
     ,$$The repeated structure, escalating metalanguage, dialogue and public destination.$$
     ,'ai_suggested','Ngarri curriculum and complete-text review; approved revision 9 September 2026','high','teacher_reviewed','Phill',now(),33)
  on conflict (book_id,strategy_slug,year_level) do update set
    applicable_year_levels=excluded.applicable_year_levels,
    key_understanding_text=excluded.key_understanding_text,
    key_skill_text=excluded.key_skill_text,
    in_this_book_text=excluded.in_this_book_text,
    book_evidence=excluded.book_evidence,
    source_type=excluded.source_type,
    source_name=excluded.source_name,
    confidence=excluded.confidence,
    status=excluded.status,
    reviewed_by=excluded.reviewed_by,
    reviewed_at=excluded.reviewed_at,
    display_order=excluded.display_order;

  insert into public.pride_value_annotations
    (book_id,value_slug,in_this_book_text,book_evidence,confidence,status,reviewed_by,reviewed_at,display_order)
  values
    (v_book_id,'determination',
     $$After the gale scatters and frightens them, the letters do more than return to their old positions and hope. They accept the word-bug's teaching, practise a new way of grouping, climb back into danger and then respond to the caterpillar's harder challenge. Determination here means learning and changing strategy after a setback, rather than merely repeating the same attempt.$$
     ,$$After the gale, the letters learn to group, return to the high leaves and accept a harder challenge.$$
     ,'high','teacher_reviewed','Phill',now(),1),
    (v_book_id,'respect',
     $$The letters move beyond statements about their immediate surroundings and choose a message concerned with peace and goodwill for others. Their decision offers a way to discuss respect as using a shared voice for care and fairness beyond one's own group. The dated phrase all men also lets a teacher ask whether respectful language should be revised when contemporary readers may not hear the intended inclusion.$$
     ,$$The letters choose a public message about peace and goodwill; discuss its historical wording.$$
     ,'high','teacher_reviewed','Phill',now(),2)
  on conflict (book_id,value_slug) do update set
    in_this_book_text=excluded.in_this_book_text,
    book_evidence=excluded.book_evidence,
    confidence=excluded.confidence,
    status=excluded.status,
    reviewed_by=excluded.reviewed_by,
    reviewed_at=excluded.reviewed_at,
    display_order=excluded.display_order;

  insert into public.inquiry_lens_annotations
    (book_id,lens_slug,big_question_addressed,in_this_book_text,book_evidence,confidence,status,reviewed_by,reviewed_at,display_order)
  values
    (v_book_id,'social_responsibility',
     'How can people combine their voices responsibly to influence decisions?',
     $$The story moves from private survival to shared communication and then toward public action. The letters become stronger by organising themselves, decide that their words should matter, and carry their message to a leader. This supports inquiry into why voices may become more powerful together, who gets heard by decision-makers and what responsibility accompanies the ability to communicate.$$
     ,$$The movement from private survival through collective language to a message for a public leader.$$
     ,'high','teacher_reviewed','Phill',now(),1),
    (v_book_id,'identity_creativity_wellbeing',
     'How can belonging to a group strengthen individual identity and creative expression?',
     $$Each letter remains recognisably itself while also contributing to something it could not create alone. The book uses visual and verbal play to connect individual identity, belonging and creative expression. Students can inquire into how people retain their uniqueness in a group, how collaboration can increase rather than erase individual capacity, and how communication helps a community act on shared concerns.$$
     ,$$Individual letters retain their identity while contributing to words, sentences and a shared message.$$
     ,'high','teacher_reviewed','Phill',now(),2)
  on conflict (book_id,lens_slug) do update set
    big_question_addressed=excluded.big_question_addressed,
    in_this_book_text=excluded.in_this_book_text,
    book_evidence=excluded.book_evidence,
    confidence=excluded.confidence,
    status=excluded.status,
    reviewed_by=excluded.reviewed_by,
    reviewed_at=excluded.reviewed_at,
    display_order=excluded.display_order;

  insert into public.teaching_ideas
    (book_id,title,description,time_minutes,grouping,difficulty,colour_tag,is_generic,status,
     year_levels,linked_focus,where_to_look,learning_focus,teaching_sequence,student_application,
     notice_learning,display_order,reviewed_by,reviewed_at)
  values
    (v_book_id,'Build a Sentence the Word-Bug Way',
     'Use the book’s visible progression to distinguish letters, words and complete sentences.',30,'Pairs','Entry','green',false,'teacher_reviewed',
     'Foundation–Year 2','Foundation Sentence Fluency; Year 2 Organisation',
     'Revisit the transformation from separate letters to words and from words to a sentence.',
     'Letters form words; words separated and ordered together form a sentence that communicates a complete idea.',
     'Model choosing letter tiles to build one word, then place two or three prepared word cards in an order that sounds sensible. Think aloud when an arrangement contains real words but does not yet communicate a clear idea. Students rebuild a short sentence and mark each word boundary.',
     'Students compose a new short sentence with cards, read it aloud, revise its order if needed and copy it with spaces.',
     'Students distinguish letters from words, point to each word in the sentence and explain why word order and spacing matter.',1,'Phill',now()),
    (v_book_id,'The Chain That Holds the Story Together',
     'Trace how each event causes the next and use the pattern to plan a cohesive narrative.',40,'Pairs','Medium','green',false,'teacher_reviewed',
     'Years 2–5','Organisation; cause-and-effect cohesion',
     'Trace the gale, the word-bug’s solution, the caterpillar’s challenge, the chosen message and the final journey.',
     'A cohesive narrative makes later events grow from earlier causes and consequences.',
     'Arrange five verified event cards. Model replacing and then with a precise cause-and-effect explanation. Pairs connect each event to the next and identify any step that cannot be removed without breaking the story’s logic.',
     'Students plan a short narrative in which each consequence creates the next problem, decision or solution.',
     'Students explain causal relationships rather than merely retelling chronology, and their own plan has no disconnected episode.',2,'Phill',now()),
    (v_book_id,'From a True Sentence to an Important Message',
     'Compare correct statements with purposeful communication for a named audience.',40,'Small group','Medium','green',false,'teacher_reviewed',
     'Years 2–5','Ideas; Audience/Voice; Social Responsibility',
     'Compare the sentences about the immediate tree world with the caterpillar’s demand for something important and the message chosen for the President.',
     'A sentence can be correct yet still need a clearer purpose, stronger idea or more relevant audience.',
     'Sort the book’s sentence types under says something and has a purpose, making clear that both can be grammatically correct. Think aloud through three questions: Who needs to hear this? What should they understand or do? Which detail matters to them? Groups revise one neutral observation into a purposeful message.',
     'Students write a short message for a real school audience and annotate one choice made for that audience.',
     'Students can name audience and purpose, and their revision changes content or wording for a reason rather than simply adding adjectives.',3,'Phill',now()),
    (v_book_id,'Three Words for a Growing Storm',
     'Examine how breeze, gust and gale create a deliberate progression of intensity.',25,'Pairs','Entry','green',false,'teacher_reviewed',
     'Years 2–3','Word Choice',
     'Revisit the escalation from breeze to gust to gale.',
     'Precise vocabulary can show changing intensity and shape a reader’s experience.',
     'Place the three weather words on an intensity line and use the surrounding event to justify their order. Substitute one general word in all three places and compare the effect. Pairs build a three-word progression for another change, such as sound, movement or emotion.',
     'Students write three connected sentences using their progression to intensify a moment.',
     'Students choose words by degree and desired effect and can explain why the words are not interchangeable.',4,'Phill',now()),
    (v_book_id,'How Our Understanding of Together Changes',
     'Revise an interpretation of together as each stage of the story adds meaning.',35,'Whole class','Medium','blue',false,'teacher_reviewed',
     'Years 2–3','Synthesising; Determination',
     'Pause after the letters first group as words, after they form sentences and when their destination is revealed.',
     'Readers revise an idea as later events add new meaning.',
     'Before each pause, students complete Together means… using current evidence. Model noticing when the earlier statement is still partly true but no longer sufficient. Keep all three statements visible and connect each revision to the new event.',
     'Students write a final synthesis using At first… Later… Now I understand… and cite the event that caused each change.',
     'Students show an actual development in understanding rather than list three events or repeat the same claim.',5,'Phill',now()),
    (v_book_id,'Main Idea or Memorable Detail?',
     'Sort events by the work they do in the plot and in the book’s larger meaning.',35,'Small group','Medium','blue',false,'teacher_reviewed',
     'Years 2–4','Determining Importance',
     'Use the complete event sequence, including the early life in the tree, the gale, both teachers and the final destination.',
     'Important information earns its place in a summary because it carries plot, character learning or the book’s larger meaning.',
     'Groups sort verified event cards into must keep, could mention and leave out. Ask them to defend every must keep card by naming what would become unclear without it. Compare the final message itself with the broader main idea developed across the narrative.',
     'Students write a concise summary and underline the detail that best supports their proposed main idea.',
     'Students justify importance by function and meaning, not by personal preference or because a detail appears near the end.',6,'Phill',now()),
    (v_book_id,'Reading the Tree as an Allegory',
     'Test a symbolic interpretation against a pattern of evidence across the complete story.',45,'Small group','Extension','purple',false,'teacher_reviewed',
     'Years 4–6','Analysing; Social Responsibility',
     'Revisit the isolated letters, their groupings, the caterpillar’s challenge and the choice to approach the President.',
     'An allegorical interpretation must be supported by a pattern across the text rather than a single guessed symbol.',
     'Model a two-column record: what happens literally and what it might represent. Deliberately test one weak interpretation and reject it when later evidence does not fit. Groups develop a claim about collective voice, education or citizenship and test it against at least three moments.',
     'Students write a short interpretation that includes evidence, reasoning and one alternative possibility.',
     'Students connect several details into a defensible pattern, distinguish literal event from interpretation and revise a claim that the text does not sustain.',7,'Phill',now()),
    (v_book_id,'Make an Idea Visible',
     'Use visual arrangement to communicate an abstract change rather than decorate a page.',35,'Pairs','Medium','green',false,'teacher_reviewed',
     'Years 2–5','Presentation',
     'Compare an image of scattered letters with an image in which the letters form readable words or sentences.',
     'Layout and illustration can explain a relationship or change that words alone may not show as efficiently.',
     'Cover the narration and ask what the two visual arrangements communicate. Reveal the words and identify what each mode contributes. Model choosing an arrangement to represent an abstract idea such as confusion becoming clarity.',
     'Students design a small visual explanation of an abstract change, then add only the words needed to clarify it.',
     'Students can explain the conceptual work done by their placement, spacing or image choice; the visual adds meaning rather than decoration.',8,'Phill',now());

  update public.books set updated_at = now() where id = v_book_id;

  if (select count(*) from public.writing_trait_annotations where book_id=v_book_id and status='teacher_reviewed') <> 17 then
    raise exception 'Expected 17 active writing records';
  end if;
  if (select count(*) from public.reading_strategy_annotations where book_id=v_book_id and status='teacher_reviewed') <> 8 then
    raise exception 'Expected 8 active reading records';
  end if;
  if (select count(*) from public.pride_value_annotations where book_id=v_book_id and status='teacher_reviewed') <> 2 then
    raise exception 'Expected 2 active PRIDE records';
  end if;
  if (select count(*) from public.inquiry_lens_annotations where book_id=v_book_id and status='teacher_reviewed') <> 2 then
    raise exception 'Expected 2 active inquiry records';
  end if;
  if (select count(*) from public.teaching_ideas where book_id=v_book_id and status='teacher_reviewed') <> 8 then
    raise exception 'Expected 8 active teaching ideas';
  end if;
end $block$;

commit;
