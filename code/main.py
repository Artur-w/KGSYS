# Importing libraries
import networkx as nx
import matplotlib.pyplot as plt
from Triple import Triple
from tqdm import tqdm
from data import psychology_data

# method responsible for creating a graph
# TODO: look for way to improve the graph.
def knowledge_graph(triples):
    G = nx.Graph()
    for triple in triples:
        G.add_node(triple[0])
        G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edge(triple[0], triple[1])
        G.add_edge(triple[1], triple[2])

    pos = nx.spring_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='#09a3d5', alpha=0.9,
            labels={node: node for node in G.nodes()})
    plt.axis('off')
    plt.show()

def main():
    # store triples in list
    triples = []

    # for each sentence extract Triple
    for i, sent in enumerate(tqdm(psychology_data['sentence'])):
        triples.append(Triple(sent).get_triple())

        # Graphs (uncomment to save artefacts on disk)
        # Triple(sent).tree('tree1'+str(i))
        # Triple(sent).graph('tree1'+str(i))

    knowledge_graph(triples)
    print(triples)
    # Tesitng sentence
    # percy = "Percy the mockingbird spent the whole warm season chirping and twittering"
    # Triple(percy).tree('dep_tree')
    # Triple(percy).graph('dep')

if __name__ == "__main__":

    main()
