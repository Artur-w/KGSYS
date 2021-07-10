import sys
from pathlib import Path
import spacy
from tqdm import tqdm
import re

nlp = spacy.load("en_core_sci_lg")

def fileconvert(path_to_folder,path_to_csv_output):
    """
    path_to_folder: Path to folder containing .txt files.
    Read in direcory of files, look for .txt extension,
    extract sentences from text, save sentences in one csv file -
    consolidating all text files in directory into one csv file.
    """
    p = Path(path_to_folder)
    for name in tqdm(p.glob('*.txt')):
        f = open(name, 'r')
        line = f.read()
        get_sent = get_sents(line)
        print(len(get_sents(line)))
        outfile = open('./sentences_temp.txt','w')
        for sent in tqdm(get_sent):
            outfile.write(clean(sent)+"\n")
    """
    Wrap each line in quotes in order to make data digastable by pandas DataFrame
    """
    with open('./sentences_temp.txt','r') as f:
        x = f.readlines()
        with open(path_to_csv_output,'w') as fw:
            fw.write("sentence"+"\n")
            for line in x:
                fw.write('\"'+line.strip('\n').strip('\r')+'\"\n')

def get_sents(text):
    """
    Generating list of sentences from input text.
    Used as helper function in fileconvert.

    Parameters
    ----------
    text : str
            Block of unstructured text.

    Returns:
            sentences (list(str)): list of sentences

    """
    tokens = nlp(text)
    sentences = []
    for sent in tokens.sents:
        sentences.append(sent.text)
    return sentences

def clean(text):
    """
    Cleaning text, removing predifiend unwanted
    elements of sentences.

    Parameters
    ----------
        text : str
            Block of text with multiple sentences.

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
    text = re.sub('\""','', str(text))
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

def main():
    # taking in directory and looking for text files.
    path_to_folder = sys.argv[1]

    # path to csv file we want to save
    path_to_csv_output = sys.argv[2]

    fileconvert(path_to_folder,path_to_csv_output)

if __name__ == "__main__":
    main()
