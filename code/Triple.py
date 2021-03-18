# TODO: Create triple class
import spacy
import sys
from spacy.matcher import Matcher
from data import ex0
from spacy import displacy
class Triple:
    """
    A class to combine all components of pipeline
    for extracting triple from sentence, but probably it doesnt make
    sense to use class for that, but well why the hell not?

    ...

    Attributes
    ----------
    attr0 : str
        first name of the triple
    attr1 : str
        family name of the triple
    attr2 : int
        age of the triple

    Methods
    -------
    get_relation
    get_entities
    get_triple()
    info(additional=""):
        Prints the triple's name and age.
    """

    def __init__(self, text):
        """
        Constructs all the necessary attributes for the triple object.

        Parameters
        ----------
        SVO - Subject - verb - object
            text : str
                sentence or block of text
            subject : str
                subject of the sentence
            relation : str
                relation between subject and object
            object : str
                object or objects of the text or the sentence
        """
        self.text = text
        global nlp
        global doc
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(self.text)

    # TODO: CHYBA DZIALA BEZ SETUP
    # def setup(self):
        # global nlp
        # global doc
        # nlp = spacy.load('en_core_web_sm')
        # doc = nlp(self.text)

    def get_relation(self):
        """
        Get relation within input sentence based on pattern provided.
        params: str - input of single sentence.
        """
        # doc = nlp(text)
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

        matcher.add("matching_1", [pattern])

        matches = matcher(doc)
        k = len(matches) - 1

        span = doc[matches[k][1]:matches[k][2]]

        # print(span.text)
        return(span.text)

    def get_triple(self):
        doc = nlp(self.text)
        sent = []
        # TODO: change doc to nlp()
        for token in doc:
            # if the token is a verb
            if (token.pos_ in ['VERB','ROOT']):
                phrase = ''
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

        # print(sent)
        return sent

    def get_entities(self):

        # store entities in variable - object subject
        ent_1 = ''
        ent_2 = ''
        tok_dep = '' # dependency tag of previous token in the sentence
        tok_txt = '' # previous token in the senetence
        pfx = ''
        mod = ''

        for tok in doc:
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

        xx = [ent_1.strip(), ent_2.strip()]
        # print(xx)
        return [ent_1.strip(), ent_2.strip()]

    def graph0():
        doc = nlp(sent)
        displacy.render(doc, style='dep')

    def graph1():
        pass
    def graph2():
        pass

    def set_doc(self,text):
        doc = nlp(self.text)
        return doc

    def set_model(self,model):
        nlp = spacy.load(model)
        return nlp

    def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """

        # print(f'My name is {self.text} {self.nlp}. I am {self.age} years old.' + additional)

    # get_relation()
    # get_triple()
    # get_entities()
    # displacy.serve(next(doc.sents), style='dep')


def exampledocString(text, file, path):
    """
    This function sole pourpose is to represent look
    of example docstring.

    Parameters
    ----------
        text : str
            Block of text with multiple sentences
        file : str
            Path to file
        path : int
            some additional parameter with type int
    """
# Tags I've chosen for relations
deps = ["ROOT", "adj", "attr", "agent", "amod"]

# Tags I've chosen for entities(subjects and objects)
deps = ["compound", "prep", "conj", "mod"]