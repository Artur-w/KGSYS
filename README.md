# Scispacy for Knowledge Graphs

Created for Final Year Project.

## Installation

1. Create conda environment and install necessary dependencies from file.

    `conda create -n <myenv> -file requirements.txt`

2. Manually create conda environment

    `conda create -n myenvironment`

    Install necessary libraries

    `conda install -c conda-forge spacy`

    `conda install -c conda-forge pandas`

    `conda install -c conda-forge networkx`

    `conda install -c conda-forge scipy`

    `pip install visualise_spacy_tree`

<!-- TODO: add venv instructions -->
<!-- `python -m spacy download en_core_web_lg` -->
    `python -m spacy download en_core_web_sm`

## Run

1. Place your data inside `data/raw/your_dir` direcotry

2. run `data.py` give it a name of your_dir and name of output file(extension is added automacially.)

3. run `main.py` give it name of csv file

Window should open with triples representend in graph form.
File with sentences and triples is saved in `data/out`
<!-- TODO: ways to trigger other artifacts -->
