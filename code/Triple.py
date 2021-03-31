# TODO: Create triple class
import spacy
import sys
import visualise_spacy_tree
from spacy.matcher import Matcher
from spacy import displacy
from spacy.util import filter_spans
from spacy.tokens import Token
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

nlp = spacy.load('en_core_web_sm')
# TODO: Maybe using Path is better?
# Path is better for multiplatform
from pathlib import Path

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
    relation
    entities


    info(additional=""):
        Prints the triple's name and age.
    """
    global entities_list
    global relation_list

    def __init__(self, text):
        """
        Constructs all the necessary attributes for the triple object.

        Parameters
        ----------
            text : str
                sentence or block of text
            entities : str
                subject of the sentence
            relation : str
                relation between subject and object
            object : str
                object or objects of the text or the sentence
        """
        self.text = text
        self.doc = nlp(self.text)
        # self.entities_list = []
        # self.relation_list = []
        # self.triple = []
        # self.entities = entities_list
        # self.entities = Triple(self.text).entities() # RecursionError: maximum recursion depth exceeded

    def relation(self):
        """
        Get relation within input sentenceence based on pattern provided.
        params: str - input of single sentenceence.
        """

        # Matcher class object
        matcher = Matcher(nlp.vocab, validate=True)

        """

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
        pattern2 = [{'DEP':'ROOT'},
                {'DEP':'prep','OP':"?"},
                {'DEP':'agent','OP':"?"},
                {'POS':'ADJ','OP':"?"}]

        matcher.add("Verb phrase", [pattern2])

        # call the matcher to find matches
        matches = matcher(self.doc)
        spans = [self.doc[start:end] for _, start, end in matches]

        relation = filter_spans(spans)
        print(f"REL IN FUN{type(relation)}")
        # self.relation_list.append(relation)
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
        orgs = []

        # ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
        # print('Entities', ents)
        for item in self.doc.ents:
            if item.label_ == 'PERSON':
                # look for person entities.
                persons.append(item.text)
            # TODO: use all entities for something cool?
            if item.label_ == 'ORG':
                orgs.append(item.text)

        for token in self.doc:
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
            # if entity1.strip() == ' ' and len(persons) >= 1:
            #     # print("Persons", persons)
            #     entity1 = persons[0]
            # else:
            #     entity1 = person
            #     # if object not captured use other
            #     if entity2.strip() == '':
            #         if len(persons) > 1:
            #             entity2 = persons[1]
            #         else:
            #             entity2 = modifier + " " + prefix + " " + token.text

        entities = [entity1.strip(), entity2.strip()]
        # self.entities_list.append(entities)
        return entities

    def get_triple(self):
        ents = self.entities()
        rel = self.relation()
        for r in rel:
            return (ents[0], r.text, ents[1])

    def tree(self, outfile):
        '''
        Dependency Tree of the sentence.

        '''
        png = visualise_spacy_tree.create_png(nlp(self.text))

        # Write it to a file
        outfile = outfile+'.png'
        print(outfile)
        with open('./images/'+outfile, 'wb') as f:
            f.write(png)

        # Override node attributes to customise the plot

        Token.set_extension('plot', default={}, force=True)  # Create a token underscore extension
        for token in doc:
            node_label = '{0} [{1}])'.format(token.orth_, token.i)
            token._.plot['label'] = node_label
            if token.dep_ == 'ROOT':
                token._.plot['color'] = 'green'

        # png = open('./images/parse_tree2.png','rb')

        img = mpimg.imread('./images/' + outfile)
        plt.imshow(img)
        plt.show()

    def graph(self,outfile):
        doc = nlp(self.text)
        doc.user_data['title'] = "Dependency graph"
        # spacy.displacy.serve(doc,style='dep')
        options = {"compact": True, "bg": "#09a3d5",
           "color": "white", "font": "Source Sans Pro"}
        svg = displacy.render(doc, style="dep", options=options)

        output_path = Path("./images/" + outfile + '.svg')
        output_path.open("w", encoding="utf-8").write(svg)
        # Optional serve method for live server displaying dependency in browser
        # displacy.serve(doc, style="dep", options=options)

    def set_model(self,model):
        nlp = spacy.load(str(model))
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