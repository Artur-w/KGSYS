# import spacy
# from sentences import text
# nlp = spacy.load('en_core_web_sm')
from spacy import displacy
from nlp_component import *


def sent_(sent, dep=False):
    """
    Analyse sentence, breaks sentence into text, pos, dep
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
        print(displacy.__file__)



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
    return sents

# Get root of sentence
def n_chunk(sent):
    roots = ''
    doc = nlp(sent)
    for chunk in doc.noun_chunks:
        print(f"Text: {chunk.text}\n-> Root: {chunk.root.text}\n-> Arc label:{chunk.root.dep_}\n-> Root head: {chunk.root.head.text}\n")
        roots += chunk.root.text+ ' ' +chunk.root.head.text+' '


    """
    EXPECTED OUTPUT:
    Noun     Aux Noun
    engineer,had,construction
             verb
    engineer,plan,construction
             verb
    engineer,produce,energy

    """

    return roots
print(n_chunk(get_sent(text)[1]))
def noun_chunks_sent(sentence):
    '''
    Take in single sntence and output
    nound chunks
    '''

    sent = nlp(sentence)
    for chunk in sent.noun_chunks:
        print(chunk)

noun_chunks_sent(get_sent(text)[0])

for sentence in get_sent(text):
    print(sentence)
    sent_(sentence,True)