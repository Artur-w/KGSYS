# Importing libraries
from Triple import knowledge_graph
from Triple import Triple
from tqdm import tqdm
import pandas as pd
import os.path
# Read in data into dataframe
path_to_csv = input("Enter path to csv file")
path_to_csv = str(path_to_csv)
# "data/csv/sentences_psychology.csv"
df = pd.read_csv(path_to_csv)
print(f"Data corpus {len(df['sentence'])} sentences")
file_name = os.path.split(path_to_csv)[1][:-4]
# def _test():
#     percy = "Percy the mockingbird spent the whole warm season chirping and twittering"
#     Triple(percy).tree('dep_tree')
#     Triple(percy).graph('dep')


def main():
    # store triples in list
    triples = []

    # for each sentence extract Triple
    for i, sent in enumerate(tqdm(df['sentence'])):
        triples.append(Triple(sent).get_triple())

        # # Graphs (uncomment to save artefacts on disk)
        # Triple(sent).tree('tree1'+str(i))
        # Triple(sent).graph('tree1'+str(i))

    df['triples'] = triples
    df.to_csv('data/out/'+file_name+'.csv')

    knowledge_graph(list(df['triples'].tail()))
    print("DONE!")


if __name__ == "__main__":
    main()
