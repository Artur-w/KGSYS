# import sentence_components
from sentence_components import sent_, get_sent, n_chunk, noun_chunks_sent, text


def main():
    # print(n_chunk(get_sent(text)[0]))
    # noun_chunks_sent(get_sent(text)[0])

    for sentence in get_sent(text):
        print("Sentence", sentence)
        sent_(sentence,True)

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