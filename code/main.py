# from sentence_components import *
# TODO: clean up all that code for fuck sake!
# TODO: Look for preposition
# TODO: do need all that imports, probably.
import re
import sys
import random
import spacy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
# TODO: use scispacy model.
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from Triple import Triple
from tqdm import tqdm


nlp = spacy.load('en_core_web_sm')


def _read_in():
    with open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt") as file:
        for line in file:
            print(line)

# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/wiki_sentences_v2.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv"
candidate_sentences = pd.read_csv(path_to_csv)

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
    # text = re.sub('[',' ',str(text))
    # text = re.sub(']',' ',str(text))
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


# # TODO: copy to data maybe
def get_sents(text):
    """
    This function sole pourpose is to represent look
    of example docstring.

    Parameters
    ----------
    text : str
            Block of text with multiple sentences

    Returns:
            sentences (list(str)): list of sentences

    """
    tokens = nlp(text)
    sentences = []
    for sent in tokens.sents:
        sentences.append(sent.text)
    # print(f"We got {len(sent)} sentences")
    return sentences

def fileconvert(path_to_folder,path_to_csv_output):
    """
    path_to_folder: Path to folder containing .txt files we want to use.
    Read in direcory of files, look for .txt extension,
    extract sentences from text, save sentences in one csv file,
    """
    # path_to_folder = '/Users/awenc/NUIM/CS440/KG_NLPSystem/data/Psychology Test Materials'
    # path_to_csv_output = '/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.csv'

    from pathlib import Path
    p = Path(path_to_folder)
    for name in p.glob('*.txt'):
        f = open(name, 'r')
        line = f.read()
        line = clean(line)
        # print(line)
        get_sent = get_sents(line)
        len(get_sents(line))
        outfile = open('./sentences_temp.txt','a')
        for i in get_sent:
            # print(type(i)) # <class 'spacy.tokens.span.Span'>
            # print(str(i))
            outfile.write(str(i)+"\n")
    """
    Wrap each line in quotes in order to make data digastable by pandas DataFrame
    """
    with open('./sentences_temp.txt','r') as f:
        x= f.readlines()
        with open(path_to_csv_output,'w') as fw:
            fw.write("sentences"+"\n")
            for line in x:
                fw.write('\"'+line.strip('\n').strip('\r')+'\"\n')

def main():
    # print(candidate_sentences.shape)
    # print(candidate_sentences['sentence'].sample(5))
    rand = random.randint(0,len(candidate_sentences['sentence']))
    # some_sent = Triple(candidate_sentences['sentence'][rand])
    # trip = Triple(user_input,spacy.load('en_core_web_sm'),nlp(text))
    mytrip = Triple("John bought new car and drove it.")
    print(mytrip.get_entities())
    print(mytrip.get_relation())
    print(mytrip.get_triple())
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