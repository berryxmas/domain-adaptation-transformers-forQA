# Domain Adaptation in Transformer models: Question Answering of Dutch Government Policies

This repository contains information and code for the MSc Data Science thesis at the University of Amsterdam.

## Installation and Requirements
```
pip install requirements.txt
```
## Datasets
#### Dutch SQuAD
We use the machine-translated to Dutch version of SQuAD V2.0. Stanford Question Answering Dataset ([SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

#### PolicyQA
We use Question and Answers from [Rijksoverheid.nl](https://www.rijksoverheid.nl/opendata/vac-s) with over 2000 questions asked by Dutch citizens about government policies. The answers are constructed by domain experts.

## Notebooks
1. [eda-policyqa](github.com): This notebook is an EDA on the PolicyQA dataset
2. [eda-squad](github.com): This notebook is an EDA on the SQuAD dataset
3. [modeling-lstm-policyqa](github.com): This notebook contains the LSTM model and is trained/tested on the PolicyQA dataset
4. [modeling-lstm-squad](github.com): This notebook contains the LSTM model and is trained/tested on the SQuAD dataset
5. [modeling-bert-policyqa](github.com): This notebook contains the three Bert-based models and is trained/tested on the PolicyQA dataset
6. [modeling-bert-squad](github.com): This notebook contains the three Bert-based models model and is trained/tested on the SQuAD dataset

## Contact
Please contact via [Linkedin - Berry Blom](https://www.linkedin.com/in/berry-blom/) for help or submit an issue. 

## Disclaimer
This is not an official UvA product. It is the outcome of an intern research project commissioned by consulting firm [Valcon](https://valcon.com/).

## Citation

Please cite:
```
@article{policybert,
author = {Berry Blom},
title = {Domain Adaptation in Transformer models: Question Answering of Dutch Government Policies},
year = {2022},
}

```