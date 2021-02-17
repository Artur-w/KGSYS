from app import sent_, get_relation, ent_extraction, foosent,graph

list_of_sents = [ex0,ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8]
for sent in list_of_sents:
    print(get_relation(sent))
    print(ent_extraction(sent))
    print(sent_(sent))


# Get root of sentence
def n_chunk(sent):
    roots = ''
    doc = nlp(sent)
    for chunk in doc.noun_chunks:
        print(f"\nChunk Text: {chunk.text}\n-> Root: {chunk.root.text}\n-> Arc label:{chunk.root.dep_}\n-> Root head: {chunk.root.head.text}\n")
        roots += chunk.root.text+ ' ' +chunk.root.head.text+' '

    return roots
# print(n_chunk(get_sent(text)[1]))

def noun_chunks_sent(sentence):
    '''
    Take in single sntence and output
    nound chunks
    '''

    sent = nlp(sentence)
    for chunk in sent.noun_chunks:
        print("Chunk: ",chunk)

def noun_component(text):
    doc = nlp(text)
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

def noun_component_list(text):
    doc = nlp(text)
    chunks = list(doc.noun_chunks)
    return chunks