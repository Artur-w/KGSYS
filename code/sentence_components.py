from spacy import displacy
from nlp_component import nlp, text


def sent_(sent, dep=False):
    """
    Analyse sentence, breaks sentence into: text, pos, dep
    part of speach
    dependency

    """

    sent = nlp(sent)
    for token in sent:
        # Get the token text, part-of-speech tag and dependency label
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_
        # This is for formatting only
        print('{:<12}{:<10}{:<10}{:<10}'.format(token_text, token_pos, token_dep,spacy.explain(token_pos)))
    if dep==True:
        displacy.render(sent, style='dep')
        print("Displacy File:",displacy.__file__)



def get_sent(text):
    """
    return:     list of sentences for given text,
                you can extract single sentence using
                indexing. It return str object.
    """
    tokens = nlp(text)
    sents = []
    for sent in tokens.sents:
        sents.append(sent.string.strip())
    print(f"We got {len(sent)} sentences")
    return sents

# Get root of sentence
def n_chunk(sent):
    roots = ''
    doc = nlp(sent)
    for chunk in doc.noun_chunks:
        print(f"\nChunk Text: {chunk.text}\n-> Root: {chunk.root.text}\n-> Arc label:{chunk.root.dep_}\n-> Root head: {chunk.root.head.text}\n")
        roots += chunk.root.text+ ' ' +chunk.root.head.text+' '

    return roots
# print(n_chunk(get_sent(text)[1]))

def noun_chunks_sent(sentence):
    '''
    Take in single sntence and output
    nound chunks
    '''

    sent = nlp(sentence)
    for chunk in sent.noun_chunks:
        print("Chunk: ",chunk)

def noun_component(text):
    doc = nlp(text)
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

