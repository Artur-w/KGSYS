import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

## Accessing entity annotations

doc = nlp("San Francisco considers banning sidewalk delivery robots")
# document level
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)

# token level
ent_san = [doc[0].text, doc[0].ent_iob_, doc[0].ent_type_]
ent_francisco = [doc[1].text, doc[1].ent_iob_, doc[1].ent_type_]
print(ent_san)  # ['San', 'B', 'GPE']
print(ent_francisco)  # ['Francisco', 'I', 'GPE']
print('----- Setting entity annotations ----')
## Setting entity annotations

from spacy.tokens import Span

doc = nlp("fb is hiring a new vice president of global policy")
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print('Before', ents)

fb_ent = Span(doc, 0, 1, label='ORG') # create a Span for the new entity
doc.ents = list(doc.ents) + [fb_ent]

ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print('After', ents)


## Setting entity annotations from array

print('---- Setting entity annotations from array ----')

import numpy

from spacy.attrs import ENT_IOB, ENT_TYPE

doc = nlp.make_doc('London is a big city in the United Kingdom.')
print('Before', doc.ents) # []

header = [ENT_IOB, ENT_TYPE]
attr_array = numpy.zeros((len(doc), len(header)), dtype='uint64')
attr_array[0, 0] = 3 # B
attr_array[0, 1] = doc.vocab.strings['GPE']
doc.from_array(header, attr_array)
print('After', doc.ents) # [London]