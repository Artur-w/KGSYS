from sentence_components import sent_, get_sent, n_chunk, noun_chunks_sent,noun_component, text

def print_sentence(text=text):
    for sentence in get_sent(text):
        print("Sentence", sentence)
        sent_(sentence,True)

def main():
    # print(n_chunk(get_sent(text)[0]))
    # noun_chunks_sent(get_sent(text)[0])
    noun_component(get_sent(text)[0])
    print_sentence()

if __name__ == "__main__":

    main()


    """
    EXPECTED OUTPUT:
    Noun     Aux Noun
    engineer,had,construction
             verb
    engineer,plan,construction
             verb
    engineer,produce,energy

    """