# Scispacy for Knowledge Graphs

## The project is a part of fufilment for final year project on CSSE.


## Installation

### Create env and install deps from file

`conda create -n <myenv> -file requirements.txt`

### or
Create conda environment
`conda create -n myenvironment`
Install necessary libraries
`conda install -c conda-forge spacy`
`conda install -c conda-forge pandas`
`conda install -c conda-forge networkx`
`conda install -c conda-forge scipy`

`pip install visualise_spacy_tree`

`python -m spacy download en_core_web_lg` and
`python -m spacy download en_core_web_sm`

## Run

### Generate Data

From dierectory of textfiles creates sentencized text.
`python generate_data.py`

### Create Knowledge Graph

Run from main folder.
`python code/main.py`