#  'BBB' : i.lower_,'CCC' : i.lemma_, 'lefts' : i.n_lefts, 'rights' : i.n_rights, 'rights N' : i.n_rights, 'rights' : i.rights, 'noun_chunk' : i.noun_chunks}
# cookbook_df = pd.DataFrame()
for i in doc.noun_chunks:
    cookbook_df = pd.DataFrame({'chunk' : i})
    # print(i)
    # print()
    # print()
    # print()
    # print()
    # print()
    print()
    # print(i.subtree) generator
    # print(i.vocab) generator
    print("\n")



produce_dict = {'veggies': ['potatoes', 'onions', 'peppers', 'carrots'],
                'fruits': ['apples', 'bananas', 'pineapple', 'berries']}
produce_dict