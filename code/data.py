
txt = "An engineer had to plan the construction of an artificial lake to produce electric energy."
txt2 = "An engineer had to plan the construction of an artificial lake to produce electric energy. To feed the lake he thought to build a unique wide canal collecting water coming from a near valley. However, a mason pointed out that during the flood periods the stream of water flowing along the canal might be too strong and might damage the surrounding areas; by contrast, during the drought periods a unique stream of water might be insufficient to feed the lake. In order to avoid these mishaps, the mason suggested to build, instead of a unique wide canal, four small canals whose total flow was the same as the unique wide canal previously planned. These small canals were placed around the lake so that they conveyed water coming from four different valleys. In this way only small amounts of water could flow in each canal and thus during flood periods dangerous overflowing might not occur. At the same time, the lake was fed by water from various belts, so that also during drought periods it was sufficiency that the fed."
txt3="Because of their wellknown stance as activists, many members of the faculty have been called to testify before Congress."
txt4="As a result, many members of this department have become recognizable faces on television news programs."
txt5="The English department faculty also have excellent reputations as teachers."
txt6="Not only are the faculty in this department extremely bright, they are able to enter the �beginner�s mind� and present material in a clear engaging manner."

# Arguments: subject-related (Subject Dependency)
# nsubj - (nominal subject)
# advmod
ex0 = "This house is pretty."
ex1 = "She and I came home together"
ex2 = "Earlier was better."
ex3 = "She grew older."
# nsubjpass (passive nominal subject)
ex4 = "I am drawn to her."
ex5 = "We will get married."
ex6 = "She will become nationalized."
ex7 = "The car was bought by John."
# csubj (clausal subject)
ex8 = "Whether she liked me doesn’t matter"
ex9 = "What you have to say is not important."
# csubjpass (clausal passive subject)
ex10 = "Whoever misbehaves will be dismissed"
ex11 = "Whether you come will be recorded."
# agent (agent) - complement of a passive verb
ex12 = "decisions made by those"
ex13 = "this was not carried out by immigrants"
# expl (expletive)
ex14 = "There was an explosion"
ex15 = "There seems to be a mistake."
# dobj (direct object)
ex16 =  "She bought me these books"
ex17 = "Minorities face inequalities."
ex18 = "She gave her a book."
# dative (indirect object)
ex19 = "She bought me these books"
ex20 = "She bought these books for me"
ex21 = "She bought me these books."
ex22 = "She gave her a book."
ex23 = "She gave a book to her."
# attr (attribute)
ex24 = "This product is a global brand"
ex25 = "This is our house."
ex26 = "Beliefs are part of a legacy."
ex27 = "Boys will be boys."
# oprd (object predicate)
ex28 = "She calls me her friend"
ex29 = "I am considered her friend"
ex30 = "She seems tired."
ex31 = "She grows older every day."
# AUX ( auxiliary )
ex32 = "I have been seeing her"
ex33 = "I decided to go home."
ex34 = "Boys will be boys."
ex35 = "I don’t like to be bothered."
# AUXPASS (passive auxiliary)
ex36 = "I am drawn to her."
ex37 = "I am struck by her beauty."
ex38 = "I don’t like to be bothered."
# BIOSCIENCE AND MEDICAL RELATED TEXTS
biosci01 = """Myeloid derived suppressor cells (MDSC) are immature
# myeloid cells with immunosuppressive activity.
# They accumulate in tumor-bearing mice and humans
# with different types of cancer, including hepatocellular
# carcinoma (HCC)."""
example = u"Donald Trump is the worst president of USA, but Hillary is better than him"

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
def get_sentvector():
    sent_vecs = {}
    docs = []

    for title in tqdm(df.title):
        doc = nlp(title)
        docs.append(doc)
        sent_vecs.update({title: doc.vector})

    sentences = list(sent_vecs.keys())
    vectors = list(sent_vecs.values())
    return [sentences, vectors]

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


def fileconvert():
    """
    TODO: PARAMETARIZE!
    X: /Users/awenc/NUIM/CS440/KG_NLPSystem/data/Psychology Test Materials
    Y: /Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt
    Z: /Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.csv

    Read in direcory of files, look for .txt extension,
    extract sentences from text, save sentences in one csv file,
    """
    from pathlib import Path
    p = Path('/Users/awenc/NUIM/CS440/KG_NLPSystem/data/Psychology Test Materials')
    for name in p.glob('*.txt'):
        f = open(name, 'r')
        line = f.read()
        # print(line)
        get_sent = get_sents(clean(line))
        len(get_sents(line))
        outfile = open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt",'a')
        for i in get_sent:
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


def fileconvertBACKOUP():
    """
    TODO: PARAMETARIZE!
    X: /Users/awenc/NUIM/CS440/KG_NLPSystem/data/Psychology Test Materials
    Y: /Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt
    Z: /Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.csv

    Read in direcory of files, look for .txt extension,
    extract sentences from text, save sentences in one csv file,
    """
    from pathlib import Path
    p = Path('/Users/awenc/NUIM/CS440/KG_NLPSystem/data/Psychology Test Materials')
    for name in p.glob('*.txt'):
        f = open(name, 'r')
        line = f.read()
        # print(line)
        get_sent = get_sents(clean(line))
        len(get_sents(line))
        outfile = open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt",'a')
        for i in get_sent:
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