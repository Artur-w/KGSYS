def txttocsv():
    """
    Read in direcory. look for files with .txt extension. 
    extract sentences from text. save sentences in one .csv file.

    """
    from pathlib import Path
    p = Path('/path/to/dir')
    for name in p.glob('*.txt'):
        f = open(name, 'r')
        line = f.read()
        print(name)
        print(line)
        x = get_sents(line)
        # len(get_sents(line))
        outfile = open("output.txt",'a')
        # type(x)
        for i in x:
            # print(type(i)) # <class 'spacy.tokens.span.Span'>
            outfile.write(clean(str(i))+"\n")
    """
    Wrap each line in quotes in order to make data digastable by pandas DataFrame
    """
    with open("output.txt",'r') as f:
        x= f.readlines()
        with open('output.csv','w') as fw:
            fw.write("sentences"+"\n")
            # append quotes for csv format
            for line in x:
                fw.write('\"'+line.strip('\n').strip('\r')+'\"\n')