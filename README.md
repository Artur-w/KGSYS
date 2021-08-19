# Scispacy for Knowledge Graphs

This project was made for final year project course.

## Installation

**Create env and install deps from file**

`conda create -n <myenv> -file requirements.txt`

**or**
Create conda environment
`conda create -n myenvironment`
Install necessary libraries
`conda install -c conda-forge spacy`
`conda install -c conda-forge pandas`
`conda install -c conda-forge networkx`
`conda install -c conda-forge scipy`

`pip install visualise_spacy_tree`

`python -m spacy download en_core_web_lg`
`python -m spacy download en_core_web_sm`

## Run

### Generate Data

From dierectory of textfiles creates sentencized text.
`python data.py`

### Create Knowledge Graph

Creates Knowledge Graph, Triples and artifacts
Run from main folder.
`python main.py`