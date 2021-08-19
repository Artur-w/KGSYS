# Importing libraries
from Triple import knowledge_graph
from Triple import Triple
from tqdm import tqdm
import pandas as pd

# Read in data
path_to_csv = "data/csv/sentences_psychology.csv"
psychology_data = pd.read_csv(path_to_csv)
print(f"Psychology data corpus {len(psychology_data['sentence'])} sentences")

def _test():
    percy = "Percy the mockingbird spent the whole warm season chirping and twittering"
    Triple(percy).tree('dep_tree')
    Triple(percy).graph('dep')


def main():
    # store triples in list
    triples = []

    # for each sentence extract Triple
    for i, sent in enumerate(tqdm(psychology_data['sentence'])):
        triples.append(Triple(sent).get_triple())

        # Graphs (uncomment to save artefacts on disk)
        # Triple(sent).tree('tree1'+str(i))
        # Triple(sent).graph('tree1'+str(i))

    # knowledge_graph(triples)
    outf = open('data/out/triples.txt','w')
    for t in triples:
        outf.write(str(t))

    print("DONE!")


if __name__ == "__main__":
    main()
