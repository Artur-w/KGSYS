# TODO: do need all that imports, probably.
# import re
# import sys
# import random
# import spacy
# import scispacy
import pandas as pd
# import networkx as nx
# import matplotlib.pyplot as plt
# # TODO: use scispacy model.
# from spacy import displacy
# from spacy.matcher import Matcher
# from spacy.tokens import Span
from Triple import Triple
# from tqdm import tqdm
# from spacy.util import filter_spans
# import visualise_spacy_tree
# from pathlib import Path

# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/wiki_sentences_v2.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv

# path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv"
# data_sentences = pd.read_csv(path_to_csv)
# print(len(data_sentences['sentences']))
# path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv"
# psycho_sentences = pd.read_csv(path_to_csv)
# print(len(psycho_sentences['sentences']))
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/data-covid/sentences_covid_v2.csv"
covid_sentences = pd.read_csv(path_to_csv)
ptc = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sample_data.csv"
sample_data = pd.read_csv(ptc)
print(len(sample_data['sentences']))

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


def main():
    # # TODO: PureWindowsPath?
    # triples = []
    # entity_pairs = []
    # relations = []

    # # output_folder = Path('./output/')
    # # top_relations_file = output_folder / "toprelations.txt"

    # for i in tqdm(covid_sentences['sentence']):
    #     entity_pairs.append(Triple(str(i)).entities())
    #     relations.append(Triple(str(i)).relation())

    # # entities()
    # object_ = [i[0] for i in tqdm(entity_pairs)]
    # subject_ = [i[1] for i in entity_pairs]
    # relations_ = [i for i in relations]
    # print(f"{len(object_)} {len(subject_)} {len(relations_)}")

    myT = Triple("London is the capital and largest city of England and the United Kingdom. Standing on the River ").get_triple()
    # covid_sentences['sentence'][0]
    # print(myT)
    text = "London is the capital and largest city of England and the United Kingdom. Standing on the River " \
           "Thames in the south-east of England, at the head of its 50-mile (80 km) estuary leading to " \
           "the North Sea, London has been a major settlement for two millennia. " \
           "Londinium was founded by the Romans. The City of London, " \
           "London's ancient core − an area of just 1.12 square miles (2.9 km2) and colloquially known as " \
           "the Square Mile − retains boundaries that follow closely its medieval limits." \
           "The City of Westminster is also an Inner London borough holding city status. " \
           "Greater London is governed by the Mayor of London and the London Assembly." \
           "London is located in the southeast of England." \
           "Westminster is located in London." \
           "London is the biggest city in Britain. London has a population of 7,172,036."









if __name__ == "__main__":

    main()
