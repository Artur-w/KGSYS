# TODO: do need all that imports, probably.
# import re
# import sys
# import random
# import spacy
# import scispacy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# # TODO: use scispacy model.
# from spacy import displacy
# from spacy.matcher import Matcher
# from spacy.tokens import Span
from Triple import Triple
from tqdm import tqdm
# from spacy.util import filter_spans
# import visualise_spacy_tree
# from pathlib import Path

# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/wiki_sentences_v2.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv

path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv"
data_sentences = pd.read_csv(path_to_csv)
print(len(data_sentences['sentence']))
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv"
psychology_data = pd.read_csv(path_to_csv)
# print(len(psychology_data['sentence']))
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/data-covid/sentences_covid_v2.csv"
covid_data = pd.read_csv(path_to_csv)
ptc = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sample_data.csv"
sample_data = pd.read_csv(ptc)
# print(len(sample_data['sentence']))

# TODO: Expand cleaning function.
def clean(text):
    """
    Cleaning text, removing predifiend unwanted
    elements of sentence.

    Parameters
    ----------
        text : str
            Block of text with multiple sentences

    Returns
    -------
        text : str
            Cleaned text
    """
    # removing new line character
    text = re.sub('\n','', str(text))
    text = re.sub('\n ','',str(text))
    # removing apostrophes
    text = re.sub("'s",'',str(text))
    # removing hyphens
    text = re.sub('-',' ',str(text))
    text = re.sub('- ','',str(text))
    # removing quotation marks
    text = re.sub('\"','',str(text))
    # removing this �, guessing it was apostrophe
    text = re.sub('�s','',str(text))
    text = re.sub('\n#','', str(text))
    text = re.sub(' # ',' ', str(text))
    text = re.sub('.#',' ', str(text))
    text = re.sub('[a-z]+�','', str(text))
    # removing paragraph numbers
    text = re.sub('[0-9]+.\t','',str(text))
    # removing new line characters
    text = re.sub('\n ','',str(text))
    text = re.sub('\n',' ',str(text))
    # removing apostrophes
    text = re.sub("'s",'',str(text))
    # removing hyphens
    text = re.sub('-',' ',str(text))
    text = re.sub('- ','',str(text))
    # removing quotation marks
    text = re.sub('\"','',str(text))
    # removing salutations
    text = re.sub('Mr.','Mr',str(text))
    text = re.sub('Mrs.','Mrs',str(text))
    text = re.sub(r'\[',' ',str(text))
    text = re.sub(r'\]',' ',str(text))
    # removing any reference to outside text
    # text = re.sub('[\(\[].*?[\)\]]', '', str(text))
    # removing double space
    text = re.sub(' +',' ',str(text))

    return text

def sent_(text):
    """
    Function prints out attributes of word from spacy.
    Parameters
    ----------
        text : str
            Block of text with multiple sentences

    Returns
    -------
    None
    Prints attributes of token object.
    text: Get the token text.
    POS: part-of-speech tag.
    DEP: dependency label.
    """
    sent = nlp(text)
    print ("TEXT" , "POS", "DEP")
    for token in sent:
        # Get the token text, part-of-speech tag and dependency label
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_
        print('{:<12}{:<10}{:<10}{:<10}'.format(token_text, token_pos, token_dep,spacy.explain(token_pos)))

def printGraph(triples):
    G = nx.Graph()
    for triple in triples:
        G.add_node(triple[0])
        G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edge(triple[0], triple[1])
        G.add_edge(triple[1], triple[2])

    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='seagreen', alpha=0.9,
            labels={node: node for node in G.nodes()})
    plt.axis('off')
    plt.show()

def main():
    # # TODO: PureWindowsPath?
    triples = []

    for sent in tqdm(data_sentences['sentence']):
        triples.append(Triple(sent).get_triple())

    printGraph(triples)

if __name__ == "__main__":

    main()
