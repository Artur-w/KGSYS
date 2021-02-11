from app import sent_, get_relation, ent_extraction, foosent

txt = "An engineer had to plan the construction of an artificial lake to produce electric energy."
txt2 = "An engineer had to plan the construction of an artificial lake to produce electric energy. To feed the lake he thought to build a unique wide canal collecting water coming from a near valley. However, a mason pointed out that during the flood periods the stream of water flowing along the canal might be too strong and might damage the surrounding areas; by contrast, during the drought periods a unique stream of water might be insufficient to feed the lake. In order to avoid these mishaps, the mason suggested to build, instead of a unique wide canal, four small canals whose total flow was the same as the unique wide canal previously planned. These small canals were placed around the lake so that they conveyed water coming from four different valleys. In this way only small amounts of water could flow in each canal and thus during flood periods dangerous overflowing might not occur. At the same time, the lake was fed by water from various belts, so that also during drought periods it was sufficiency that the fed."
txt3="Because of their wellknown stance as activists, many members of the faculty have been called to testify before Congress."
txt4="As a result, many members of this department have become recognizable faces on television news programs."
txt5="The English department faculty also have excellent reputations as teachers."
txt6="Not only are the faculty in this department extremely bright, they are able to enter the �beginner�s mind� and present material in a clear engaging manner."

# print(get_relation(txt))
# print(ent_extraction(txt))
# print(sent_(txt))
# foosent()
# outfile = open('myout.txt')
with open("/Users/awenc/NUIM/CS440/KG_NLPSystem/workspace/sentences_psychology.txt") as file:
    for line in file:
        print(line)
        # print(foosent(line))
        print(get_relation(line))
        print(ent_extraction(line))
        print(sent_(line))
