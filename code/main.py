# from sentence_components import *
# TODO: clean up all that code for fuck sake!
# TODO: Look for preposition
# TODO: do need all that imports, probably.
import re
import pandas as pd
import random
# import bs4
# import requests
import spacy
from spacy import displacy
# TODO: use scispacy model.

from spacy.matcher import Matcher
from spacy.tokens import Span
from Triple import Triple
import networkx as nx
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm
# from app import get_entities, get_relation, sent_, get_triple
import pandas as pd

nlp = spacy.load('en_core_web_sm')
# text = user_input
try:
    user_input = sys.argv[1]
    text = user_input
except:
    text = "Because of their wellknown stance as activists, many members of the faculty have been called to testify before Congress."
    pass
if text == "":
    print("no input entered")
else:
    print("User input ->",type(text))


# doc = nlp(text)

def _read_in():
    with open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt") as file:
        for line in file:
            print(line)

# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/wiki_sentences_v2.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv"
candidate_sentences = pd.read_csv(path_to_csv)

def main():

    # print(candidate_sentences.shape)
    # print(candidate_sentences['sentence'].sample(5))
    rand = random.randint(0,len(candidate_sentences['sentence']))
    # some_sent = Triple(candidate_sentences['sentence'][rand])
    trip = Triple(user_input,spacy.load('en_core_web_sm'),nlp(text))
    print(trip.get_entities())
    print(trip.get_relation())
    print(trip.get_triple())
    # relation = Triple.get_relation
    # get_triple()
    # get_entities()
    # displacy.serve(next(doc.sents), style='dep')
    # print(some_sent)







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