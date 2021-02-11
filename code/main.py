# from sentence_components import *
# TODO: clean up all that code for fuck sake!
# TODO: Look for preposition
import re
import pandas as pd
# import bs4
# import requests
import spacy
from spacy import displacy
# TODO: use scispacy model.
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher
from spacy.tokens import Span

import networkx as nx

import matplotlib.pyplot as plt
from tqdm import tqdm
from data import candidate_sentences, get_sents
from app import ent_extraction, get_relation

# TODO: only getting one relation from sentence why?
# def get_relation(sent):
#     """
#     Get relation within input sentence based on pattern provided.
#     params: str - input of single sentence.
#     """
#     doc = nlp(sent)

#     # Matcher class object
#     matcher = Matcher(nlp.vocab)

#     #define the pattern
#     # TODO: explore matcher

#     """
#     Match 0 or more times / match 0 or 1 time(one relation in sencence?)
#     """
#     pattern = [{'DEP':'ROOT'},
#             {'DEP':'prep','OP':"*"},
#             {'DEP':'agent','OP':"*"},
#             {'POS':'ADJ','OP':"*"}]

#     matcher.add("matching_1", None, pattern)

#     matches = matcher(doc)
#     k = len(matches) - 1

#     span = doc[matches[k][1]:matches[k][2]]

#     return(span.text)

# def print_sentence(text=text):
#     for sentence in get_sent(text):
#         print("Sentence", sentence)
#         sent_(sentence)


# def get_sents(text):
#     """
#     return:     list of sentences for given text,
#                 you can extract single sentence using
#                 indexing. It return str object.
#     """
#     tokens = nlp(text)
#     sents = []
#     for sent in tokens.sents:
#         sents.append(sent.string.strip())
#     # print(f"We got {len(sent)} sentences")
#     return sents

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
    # for sentence in get_sents(text):
    #     print(get_relation(sentence))
    # print(candidate_sentences.shape)
    # print(candidate_sentences['sentence'].sample(5))
    # TODO: parameraterize
    # doc = nlp("An engineer had to plan the construction of an artificial lake to produce electric energy.")
    # for tok in doc:
    #     print(tok.text, "...", tok.dep_)
    # print(get_entities("An engineer had to plan the construction of an artificial lake to produce electric energy."))
    entity_pairs = []
    # Entity pairs
    try:
        for i in tqdm(candidate_sentences["sentences"]):
            entity_pairs.append(ent_extraction(i))
        print(entity_pairs[:])
        relations = [get_relation(i) for i in tqdm(candidate_sentences['sentences'])]
        print(pd.Series(relations).value_counts()[:])

        # extract subject
        source = [i[0] for i in entity_pairs]

        # extract object
        target = [i[1] for i in entity_pairs]

        kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
        # create a directed-graph from a dataframe
        G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())
        plt.figure(figsize=(12,12))

        pos = nx.spring_layout(G)
        nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
        plt.show()
    except TypeError as e:
        print(e)
        pass
    except:
        print("unexprected error ")
        pass

    # print(n_chunk(get_sent(text)[0]))
    # noun_chunks_sent(get_sent(text)[0])
    # noun_component(get_sent(text)[0])
    # print_sentence(get_sent(text)[0])
    # print(noun_component_list(get_sent(text)[0]))
    # print(get_sent(text))
    # n_chunk("It is impossible to operate on the patient, but unless the tumour is destroyed the patient will die.")

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