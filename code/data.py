import pandas as pd


text = "An engineer had to plan the construction of an artificial lake to produce electric energy. To feed the lake he thought to build a unique wide canal collecting water coming from a near valley. However, a mason pointed out that during the flood periods the stream of water flowing along the canal might be too strong and might damage the surrounding areas; by contrast, during the drought periods a unique stream of water might be insufficient to feed the lake. In order to avoid these mishaps, the mason suggested to build, instead of a unique wide canal, four small canals whose total flow was the same as the unique wide canal previously planned. These small canals were placed around the lake so that they conveyed water coming from four different valleys. In this way only small amounts of water could flow in each canal and thus during flood periods dangerous overflowing might not occur. At the same time, the lake was fed by water from various belts, so that also during drought periods it was sufficiency that the fed."

# import sentence file.
candidate_sentences = pd.read_csv("/Users/awenc/NUIM/CS440/KG_NLPSystem/code/eng_lake.csv")

# TODO: przekrztalcic w plik csv dla pandas.
# dodac nazwe kolumny w tym przypadku sentence
# kazde zdanie powinno byc zamkniete w cudzyslowie.
# zdania sa oddzielone znakami nowej lini
