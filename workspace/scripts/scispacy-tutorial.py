import scispacy
import spacy

nlp = spacy.load("en_core_sci_sm")
text = """
Myeloid derived suppressor cells (MDSC) are immature
myeloid cells with immunosuppressive activity.
They accumulate in tumor-bearing mice and humans
with different types of cancer, including hepatocellular
carcinoma (HCC).
"""
doc = nlp(text)

print(list(doc.sents))
# >>> ["Myeloid derived suppressor cells (MDSC) are immature myeloid cells with immunosuppressive activity.",
#      "They accumulate in tumor-bearing mice and humans with different types of cancer, including hepatocellular carcinoma (HCC)."]

# Examine the entities extracted by the mention detector.
# Note that they don't have types like in SpaCy, and they
# are more general (e.g including verbs) - these are any
# spans which might be an entity in UMLS, a large
# biomedical database.
print(doc.ents)
# >>> (Myeloid derived suppressor cells,
#      MDSC,
#      immature,
#      myeloid cells,
#      immunosuppressive activity,
#      accumulate,
#      tumor-bearing mice,
#      humans,
#      cancer,
#      hepatocellular carcinoma,
#      HCC)

# We can also visualise dependency parses
# (This renders automatically inside a jupyter notebook!):
from spacy import displacy
displacy.render(next(doc.sents), style='dep', jupyter=True)

# See below for the generated SVG.
# Zoom your browser in a bit!