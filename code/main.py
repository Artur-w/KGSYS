from sentence_components import *

import re
import pandas as pd
# import bs4
# import requests
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher
from spacy.tokens import Span

import networkx as nx

import matplotlib.pyplot as plt
from tqdm import tqdm
from data import text, candidate_sentences


def get_relation(sent):
    """
    Get relation within input sentence based on pattern provided.
    params: str
    """
    doc = nlp(sent)

    # Matcher class object
    matcher = Matcher(nlp.vocab)

    #define the pattern
    # TODO: look for all possible patterns.
    pattern = [{'DEP':'ROOT'},
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},
            {'POS':'ADJ','OP':"?"}]

    matcher.add("matching_1", None, pattern)

    matches = matcher(doc)
    k = len(matches) - 1

    span = doc[matches[k][1]:matches[k][2]]

    return(span.text)

def print_sentence(text=text):
    for sentence in get_sent(text):
        print("Sentence", sentence)
        sent_(sentence)
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
        # print("Displacy File:",displacy.__file__)


# TODO: chenge name to get_sents if giving back list
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

def noun_component_list(text):
    doc = nlp(text)
    chunks = list(doc.noun_chunks)
    return chunks

def main():
    for sentence in tqdm(get_sent(text)):
        print(get_relation(sentence))
    print(candidate_sentences.shape)
    print(candidate_sentences['sentence'].sample(5))

    # print(n_chunk(get_sent(text)[0]))
    # noun_chunks_sent(get_sent(text)[0])
    # noun_component(get_sent(text)[0])
    # print_sentence(get_sent(text)[0])
    # print(noun_component_list(get_sent(text)[0]))
    # print(get_sent(text))


if __name__ == "__main__":

    main()


    """
    EXPECTED OUTPUT:
    Noun     Aux Noun
    engineer,had,construction
             verb
    engineer,plan,construction
             verb
    engineer,produce,energy

    """