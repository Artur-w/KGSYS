# TODO: Create triple class
import spacy
import sys
from spacy.matcher import Matcher
from spacy import displacy
from spacy.util import filter_spans

# this is invisible for class?
nlp = spacy.load('en_core_web_sm')
# TODO: rework get entitirs

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
        doc = nlp(self.text)

    def relation(self):
        """
        Get relation within input sentenceence based on pattern provided.
        params: str - input of single sentenceence.
        """
        doc = nlp(self.text)

        # Matcher class object
        matcher = Matcher(nlp.vocab, validate=True)

        """
        Match 0 or more times / match 0 or 1 time(one relation in sencence?)
        Dodałem PROPN ale jeszcze nie przetestowałem.


        OP	DESCRIPTION
        !	Negate the pattern, by requiring it to match exactly 0 times.
        ?	Make the pattern optional, by allowing it to match 0 or 1 times.
        +	Require the pattern to match 1 or more times.
        *	Allow the pattern to match zero or more times.
        """
        # in some cases pattern0 matches too many words.
        pattern0=[{'POS': 'VERB', 'OP': '?'},
                {'POS': 'ADV', 'OP': '*'},
                {'OP': '*'}, # additional wildcard - match any text in between
                {'POS': 'VERB', 'OP': '+'}]
        pattern1 = [{'DEP':'ROOT'},
                {'DEP':'prep','OP':"?"},
                {'DEP':'agent','OP':"?"},
                {'POS':'PROPN','OP':'?'},
                {'POS':'ADJ','OP':"?"}]
        pattern = [{'POS': 'VERB', 'OP': '?'},
                {'POS': 'ADV', 'OP': '?'},
                {'POS': 'AUX', 'OP': '?'},
                {'POS': 'VERB', 'OP': '?'}]
        pattern2 = [{'DEP':'ROOT'}, 
                {'DEP':'prep','OP':"?"},
                {'DEP':'agent','OP':"?"},  
                {'POS':'ADJ','OP':"?"}] 

        matcher.add("Verb phrase", [pattern2])

        # call the matcher to find matches 
        matches = matcher(doc)
        spans = [doc[start:end] for _, start, end in matches]

        relation = filter_spans(spans)
        return relation

    def entities(self):
        entity1 = ""
        entity2 = ""

        prv_tok_dep = ""    # dependency tag of previous token in the sentence
        prv_tok_text = ""   # previous token in the sentence

        prefix = ""
        modifier = ""
        person = ""
        persons = []

        doc = nlp(self.text)
        ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
        print('Entities', ents)
        for item in doc.ents:
            print(len(doc.ents))
            if item.label_ == 'PERSON':
                # look for person entities.
                persons.append(str(item.text))
        print(persons)
        for token in doc:
            # igonre punctuation
            if token.dep_ != 'punkt':
                # include compoound words
                if token.dep_ == 'compound':
                    prefix = token.text
                    if prv_tok_dep == 'compound':
                        prefix = prv_tok_text + " " + token.text
                # check if token is a modifier
                if token.dep_.endswith('mod') == True:
                    modifier = token.text
                    if prv_tok_dep == 'compound':
                        modifier = prv_tok_text + " " + token.text
                # find any form/kind of subject
                if token.dep_.find('subj') == True:
                    # create entity1, subject
                    entity1 = modifier + " " + prefix + " " + token.text
                    # reset variables
                    prefix = ""
                    modifier = ""
                    prv_tok_dep = ""
                    prv_tok_text = ""
                # find potential object in the sentence.
                if token.dep_.find('obj') == True:
                    entity2 = modifier + " " + prefix + " " + token.text

                # update variables
                prv_tok_dep = token.dep_
                prv_tok_text = token.text
            #TODO: something wrong with this ifs
            # If subject not captured use person entity
            if entity1.strip() == '' and len(persons) > 1:
                entity1 = persons[0]
            else: 
                entity1 = person
                # if object not captured use other
                if entity2.strip() == '':
                    if len(persons) > 1:
                        entity2 = persons[1]
                    else:
                        entity2 = modifier + " " + prefix + " " + token.text
        print("my persons ",persons)
        return [entity1, entity2.strip()]

    def dependency_graph(self):
        doc = nlp(self.text)
        displacy.render(doc, style='dep')

    def graph(self):
        # TODO: add networkx graph genration function
        pass
    
    def tree_graph(self):
        # TODO: add visualise spacy tree function here.
        pass

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
