import spacy
import scispacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import tqdm
import pandas as pd
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load("en_core_sci_sm")

# TODO: need to install large model
# nlp = spacy.load('en_core_web_lg')

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
        # print(line)
        x = get_sent(line)
        len(get_sent(line))
        outfile = open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt",'a')
        type(x)
        for i in clean(x):
            # print(type(i)) # <class 'spacy.tokens.span.Span'>
            # print(str(i))
            outfile.write(str(i)+"\n")
    """
    Wrap each line in quotes in order to make data digastable by pandas DataFrame
    """
    with open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt",'r') as f:
        x= f.readlines()
        with open('/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.csv','w') as fw:
            fw.write("sentences"+"\n")
            for line in x:
                fw.write('\"'+line.strip('\n').strip('\r')+'\"\n')

def foosent():
    sent_vecs = {}
    docs = []

    for title in tqdm(df.title):
        doc = nlp(title)
        docs.append(doc)
        sent_vecs.update({title: doc.vector})

    sentences = list(sent_vecs.keys())
    vectors = list(sent_vecs.values())
    return [sentences, vectors]

def sent_(sentence, dep=False):
    """
    Analyse sentence, breaks sentence into: text, pos, dep
    part of speach
    dependency

    """

    sent = nlp(sentence)
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

def get_relation(sent):
    """
    Get relation within input sentence based on pattern provided.
    params: str - input of single sentence.
    """
    doc = nlp(sent)

    # Matcher class object
    matcher = Matcher(nlp.vocab)

    #define the pattern
    # TODO: explore matcher

    """
    Match 0 or more times / match 0 or 1 time(one relation in sencence?)
    """
    pattern = [{'DEP':'ROOT'},
            {'DEP':'prep','OP':"*"},
            {'DEP':'agent','OP':"*"},
            {'POS':'ADJ','OP':"*"}]

    matcher.add("matching_1", None, pattern)

    matches = matcher(doc)
    k = len(matches) - 1

    span = doc[matches[k][1]:matches[k][2]]

    return(span.text)


def ent_extraction(sentence):
    # store entities in variable - object subject
    ent_1 = ''
    ent_2 = ''
    tok_dep = '' # dependency tag of previous token in the sentence
    tok_txt = '' # previous token in the senetence
    pfx = ''
    mod = ''

    for tok in nlp(sentence):
        if tok.dep_ != 'punct':
            if tok.dep_ == 'compound':
                pfx = tok.text
                if tok.dep_ == 'compound':
                    pfx = tok_txt +" "+tok.text

        if tok.dep_.endswith('mod') == True:
            mod = tok.text
            if tok.dep_ == 'compound':
                mod = tok_txt+" "+tok.text

        if tok.dep_.find("subj") == True:
            ent_1 = mod+" "+pfx+" "+tok.text
            tok_txt =''
            tok_dep=''
            pfx = ''
            mod =''

        if tok.dep_.find("obj") == True:
            ent_2 = mod+" "+pfx+" "+tok.text

        tok_dep = tok.dep_
        tok_txt = tok.text
    return [ent_1.strip(), ent_2.strip()]