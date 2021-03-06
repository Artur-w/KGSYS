import spacy
import tqdm
import re
import pandas as pd
import logging
import scispacy
# import neuralcoref
import networkx
from spacy import displacy
from spacy.tokens import Span
from spacy.matcher import Matcher
from spacy.lang.en import English
# nlp = spacy.load('en_core_web_lg')
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load("en_core_sci_sm")
# TODO: need to install large model

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
    for token in sent:
        # Get the token text, part-of-speech tag and dependency label
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_
        print('{:<12}{:<10}{:<10}{:<10}'.format(token_text, token_pos, token_dep,spacy.explain(token_pos)))


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
    # removing any reference to outside text
    # text = re.sub('[\(\[].*?[\)\]]', '', str(text))
    # removing double space
    text = re.sub(' +',' ',str(text))

    return text


# TODO: copy to data maybe
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

# get sent using pandas
# TODO: needs pandas
def get_sent2():
    sent_vecs = {}
    docs = []

    for title in tqdm(df.title):
        doc = nlp(title)
        docs.append(doc)
        sent_vecs.update({title: doc.vector})

    sentences = list(sent_vecs.keys())
    vectors = list(sent_vecs.values())
    return [sentences, vectors]

# function: noun(subject), verb, noun(object)
def get_triple(text):

    doc = nlp(text)
    sent = []

    for token in doc:
        # if the token is a verb
        if (token.pos_ in ['VERB','ROOT']):
            phrase =''
            # only extract noun or pronoun subjects
            for sub_tok in token.lefts:
                if (sub_tok.dep_ in ['nsubj','nsubjpass']) and (sub_tok.pos_ in ['NOUN','PROPN','PRON']):
                    # add subject to the phrase
                    phrase += sub_tok.text
                    # save the root of the verb in phrase
                    phrase += ' '+token.lemma_
                    # check for noun or pronoun direct objects
                    for sub_tok in token.rights:
                        # save the object in the phrase
                        if (sub_tok.dep_ in ['dobj']) and (sub_tok.pos_ in ['NOUN','PROPN']):
                            phrase += ' '+sub_tok.text
                            sent.append(phrase)

    return sent



# TODO: WHY IT IS NOT DISPLAYED?
def graph(sent):
    doc = nlp(sent)
    displacy.render(doc, style='dep')

def get_relation(sent):
    """
    Get relation within input sentence based on pattern provided.
    params: str - input of single sentence.
    """
    doc = nlp(sent)

    # Matcher class object
    matcher = Matcher(nlp.vocab, validate=True)

    #define the pattern
    # TODO: explore matcher

    """
    Match 0 or more times / match 0 or 1 time(one relation in sencence?)
    Dodałem PROPN ale jeszcze nie przetestowałem.
    """
    pattern = [{'DEP':'ROOT'},
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},
            {'POS':'PROPN','OP':'?'},
            {'POS':'ADJ','OP':"?"}]
    # TODO Add verb matcher?

    matcher.add("matching_1", None, pattern)

    matches = matcher(doc)
    k = len(matches) - 1

    span = doc[matches[k][1]:matches[k][2]]

    return(span.text)


def get_entities(sentence):
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


def sentencize(text):
    """
    Take in text and break it into sentences
    """
    nlp = English()
    nlp.add_pipe(nlp.create_pipe('sentencizer')) # updated
    doc = nlp(text)
    sentences = [sent.string.strip() for sent in doc.sents]
    # sentences = nlp(text)
    # for i, sentence in enumerate(sentences.sents):
    #     print(i, sentence)
    #     return sentence
    logging.info('Sentencize'+type(sentences))
    return sentences