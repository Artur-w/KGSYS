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
