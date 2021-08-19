# Importing libraries
from Triple import knowledge_graph
# import matplotlib.pyplot as plt
from Triple import Triple
from tqdm import tqdm
from example_data import psychology_data


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
    print(triples)
    # Tesitng sentence
    # percy = "Percy the mockingbird spent the whole warm season chirping and twittering"
    # Triple(percy).tree('dep_tree')
    # Triple(percy).graph('dep')

if __name__ == "__main__":

    main()
