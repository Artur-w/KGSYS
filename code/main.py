import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import pytest
from Triple import Triple
from tqdm import tqdm


# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/wiki_sentences_v2.csv
# /Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv
wiki_data = pd.read_csv("/Users/awenc/NUIM/CS440/KG_NLPSystem/data/wiki_sentences_v2.csv")
print(f"wiki_data have: {len(wiki_data)} sentences")
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences.csv"
data_sentences = pd.read_csv(path_to_csv)
# print(len(data_sentences['sentence']))
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sentences_psychology.csv"
psychology_data = pd.read_csv(path_to_csv)
# print(len(psychology_data['sentence']))
path_to_csv = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/data-covid/sentences_covid_v2.csv"
covid_data = pd.read_csv(path_to_csv)
ptc = "/Users/awenc/NUIM/CS440/KG_NLPSystem/data/sample_data.csv"
sample_data = pd.read_csv(ptc)
# print(len(sample_data['sentence']))

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
    triples = []

    for i, sent in enumerate(tqdm(psychology_data['sentence'])):
        triples.append(Triple(sent).get_triple())

    #     # Graphs (uncomment to create artefacts)
    #     # Triple(sent).tree('tree1'+str(i))
    #     # Triple(sent).graph('tree1'+str(i))

    # # Knowleadge Graph
    knowledge_graph(triples)
    percy = "Percy the mockingbird spent the whole warm season chirping and twittering"
    # Triple("George like films").graph('george')

if __name__ == "__main__":

    main()
