"""

"""
# Dependency Parsing

## Noun chunks

import spacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load("en_core_web_sm")
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")

# for chunk in doc.noun_chunks:
#     print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
print('--------------------------------')
## Navigateing the parse tree

# for token in doc:
#     print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])

## Finding a verb with a subject from below - good
verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)

## Finding a verb with a subject from above - less good
verbs = []
for possible_verb in doc:
    if possible_verb.pos == VERB:
        for possible_subject in possible_verb.children:
            if possible_subject.dep == nsubj:
                verbs.append(possible_verb)
                break

## Iterating around the local tree

doc = nlp("bright red apples on the tree")
print([token.text for token in doc[2].lefts])  # ['bright', 'red']
print([token.text for token in doc[2].rights])  # ['on']
print(doc[2].n_lefts)  # 2
print(doc[2].n_rights)  # 1


doc = nlp("Credit and mortgage account holders must submit their requests")

root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]
for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
            descendant.n_rights,
            [ancestor.text for ancestor in descendant.ancestors])


## Visualizing dependencies

from spacy import displacy

doc = nlp("Autonomous cars shift insurance liability toward manufacturers")

displacy.render(doc, style='dep')

# disabling the parser

nlp = spacy.load("en_core_web_sm", disable=["parser"])
nlp = English().from_disk("/model", disable=["parser"])
doc = nlp("I don't want parsed", disable=["parser"])