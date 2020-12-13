import spacy
nlp = spacy.load('en_core_web_sm')
with open('/Users/awenc/NUIM/CS440/spacy-tutorial/01 Antonet - Four-Canals-Carocci.txt') as f:
    text = f.read()
    # doc = nlp(text)

    # print(text)
# doc = nlp(text)
# print(sents_list[3]) # get sentence of text bit.
# dir(doc)
 # gives list of sentences.
# for token in doc:
#     # Get the token text, part-of-speech tag and dependency label
#     token_text = token.text
#     token_pos = token.pos_
#     token_dep = token.dep_
# print(f"{token_pos}\n{token_dep}\n{token_text}")
nouns = []
verbs = []
for token in doc:
    print(token,token.pos_)
    if(token.pos_ == 'NOUN'):
        nouns.append(token.text)
    if(token.pos_ == 'VERB'):
        verbs.append(token.text)

nouns
verbs


def brk_sent(sentence):
    """
    Break sentence for analysis.
    """
    doc = nlp(sentence)
    for token in doc:
        # Get the token text, part-of-speech tag and dependency label
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_
        # This is for formatting only
        print('{:<12}{:<10}{:<10}'.format(token_text, token_pos, token_dep))
        return token_pos

# [sent for sent in brk_sent(sentence)
# for sent in sentence:
#     brk_sent(sent)


for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # This is for formatting only
    print('{:<12}{:<10}{:<10}'.format(token_text, token_pos, token_dep))



# [chunk.text for chunk in doc.verb_chunks]
# for i in range(len(doc)):

# [chunk.text for chunk in doc.sents]
# [span for span in doc.count_by]
# [chunk.text for chunk in doc.count_by]
[chunk.text for chunk in doc.sents] # get sentence
[chunk.text for chunk in doc.noun_chunks] # ######
x = [chunk for chunk in doc.noun_chunks] # ######


def check_verb(token):
    """Check verb type given spacy token"""
    if token.pos_ == 'VERB':
        indirect_object = False
        direct_object = False
        for item in token.children:
            if(item.dep_ == "iobj" or item.dep_ == "pobj"):
                indirect_object = True
            if (item.dep_ == "dobj" or item.dep_ == "dative"):
                direct_object = True
        if indirect_object and direct_object:
            return 'DITRANVERB'
        elif direct_object and not indirect_object:
            return 'TRANVERB'
        elif not direct_object and not indirect_object:
            return 'INTRANVERB'
        else:
            return 'VERB'
    else:
        return token.pos_
[check_verb(t) for t in doc]