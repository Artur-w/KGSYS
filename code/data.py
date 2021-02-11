import pandas as pd
import spacy
import re
# from spacy import displacy
# TODO: use scispacy model.
# TODO: in data file - data related code.
nlp = spacy.load('en_core_web_sm')

from app import sent_
# text = "An engineer had to plan the construction of an artificial lake to produce electric energy. To feed the lake he thought to build a unique wide canal collecting water coming from a near valley. However, a mason pointed out that during the flood periods the stream of water flowing along the canal might be too strong and might damage the surrounding areas; by contrast, during the drought periods a unique stream of water might be insufficient to feed the lake. In order to avoid these mishaps, the mason suggested to build, instead of a unique wide canal, four small canals whose total flow was the same as the unique wide canal previously planned. These small canals were placed around the lake so that they conveyed water coming from four different valleys. In this way only small amounts of water could flow in each canal and thus during flood periods dangerous overflowing might not occur. At the same time, the lake was fed by water from various belts, so that also during drought periods it was sufficiency that the fed."


def get_sents(text):
    """
    return:     list of sentences for given text,
                you can extract single sentence using
                indexing. It return str object.
    """
    tokens = nlp(text)
    sents = []
    for sent in tokens.sents:
        sents.append(sent.string.strip())
    # print(f"We got {len(sent)} sentences")
    return sents

def clean(text):
    # removing new line character
    text = re.sub('\n','', str(text))
    text = re.sub('\n ','',str(text))
    # removing apostrophes
    text = re.sub("'s",'',str(text))
    # removing hyphens
    text = re.sub("-",' ',str(text))
    text = re.sub("- ",'',str(text))
    # removing quotation marks
    text = re.sub('\"','',str(text))
    return text

def fileconvert():
    """
    Read in direcory of files, look for .txt extension, extract sentences from text, save sentences in one file,
    """
    from pathlib import Path
    p = Path('/Users/awenc/NUIM/CS440/KG_NLPSystem/data/Psychology Test Materials')
    for name in p.glob('*.txt'):
        f = open(name, 'r')
        line = f.read()
        print(name)
        print(line)
        x = get_sents(line)
        # len(get_sents(line))
        outfile = open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt",'a')
        # type(x)
        for i in x:
            # print(type(i)) # <class 'spacy.tokens.span.Span'>
            # print(str(i))
            outfile.write(clean(str(i))+"\n")
    """
    Wrap each line in quotes in order to make data digastable by pandas DataFrame
    """
    with open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt",'r') as f:
        x= f.readlines()
        with open('/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.csv','w') as fw:
            fw.write("sentences"+"\n")
            for line in x:
                fw.write('\"'+line.strip('\n').strip('\r')+'\"\n')

# import sentence file.


# TODO: przekrztalcic w plik csv dla pandas.
# dodac nazwe kolumny w tym przypadku sentence
# kazde zdanie powinno byc zamkniete w cudzyslowie.
# zdania sa oddzielone znakami nowej lini
# pobieznie jest to zrobione ale trzeba to zebrac do kupy
# fileconvert()
candidate_sentences = pd.read_csv("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.csv")