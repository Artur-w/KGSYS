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
from app import get_entities, get_relation, sent_, get_triple


def main():
    with open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt") as file:
        for line in file:
            print(line)
            # print(foosent(line))
            print(get_relation(line))
            print(rule1(line))
            print(ent_extraction(line))
            print(sent_(line))
    # for sentence in get_sents(text):
    #     print(get_relation(sentence))
    # print(candidate_sentences.shape)
    # print(candidate_sentences['sentence'].sample(5))
    # doc = nlp("An engineer had to plan the construction of an artificial lake to produce electric energy.")
    # for tok in doc:
    #     print(tok.text, "...", tok.dep_)
    # print(get_entities("An engineer had to plan the construction of an artificial lake to produce electric energy."))
    # entity_pairs = []
    # # Entity pairs
    # try:
    #     for i in tqdm(candidate_sentences["sentences"]):
    #         entity_pairs.append(ent_extraction(i))
    #     print(entity_pairs[:])
        
    #     print(pd.Series(relations).value_counts()[:])

    #     # extract subject
    #     source = [i[0] for i in entity_pairs]
    #     # Relation
    #     relations = [get_relation(i) for i in tqdm(candidate_sentences['sentences'])]
    #     # extract object
    #     target = [i[1] for i in entity_pairs]

    #     kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relations})
    #     # create a directed-graph from a dataframe
    #     G=nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())
    #     plt.figure(figsize=(12,12))

    #     pos = nx.spring_layout(G)
    #     nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
    #     plt.show()
    # except TypeError as e:
    #     print(e)
    #     pass
    # except:
    #     print("unexprected error ")
    #     pass

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