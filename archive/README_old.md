# NoSQL Injection Detection

This is a Repository for the Paper titled "NoSQL Injection Query Detection in MongoDB Using Supervised Learning-based Binary Classification Models" By Mr. Shaunak Perni and Ms. Minal Shirodkar

## Index

* `/Dataset` - These are the input datasets for the Notebooks of this Paper
* `/FinalModels` - The finalized models and other notebooks for this paper
* `/No-SQL_Gen` - This directory contains the input data for the paper which was taken from another repository can be found [here](https://github.com/capnmav77/No-SQL_Gen/tree/a85ce3eb202715102438298bbb7b090e243845c2)
* `/NoSQLInjectionDectectionVENV` - The python virtual environment which contains the libraries pre-installed
* `/notebooks` - Contains notebooks initially used in the paper currently depreciated 
* `/scripts` - Contains BASH scripts to extract logs from MonogoDB

## Notes

* The Notebooks under `FinalModels`
  * `DataExploration.ipynb`  Contains the data exploration of the mongoDB log file
  * `FinalModels.ipynb` contains all of the models trained at different configurations
* Notebooks under notebooks
  * `dataProcess.ipynb` contains code to preprocess the raw log file
  * `EDA.ipynb`'s outputs has been partially used in the project, these outputs will be shifted to `FinalModels/DataExploration.ipynb`
  * All other notebooks under this directory are depreciated 
* Dataset Directory contains the raw, cleaned data from the mongoDB server logs
  * `queryLogs.json` is the raw copied server log of the MongoDB server
  * `final.csv` is the cleaned dataset
* `FinalModels/mongoTokens.py` is the custom tokenizer developed to tokenize the mongoDB query filters

## TODO

* Cleaning of the repository and removal of all deprecated files
