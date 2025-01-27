# Predicting NASDAQ Stock Prices Through Sentiment Analysis of U.S. President’s Social Media Posts
This project investigates the influence of U.S. President Donald Trump's social media posts on the NASDAQ Composite Index by leveraging sentiment analysis and deep learning-based time series prediction models. The code in this repository supports the experiments described in the draft paper, which aims to empirically validate how political sentiment impacts financial markets.

Using sentiment analysis tools like VADER and RoBERTa, the project extracts positive, neutral, and negative sentiment from the President's posts. The extracted sentiment data, along with historical NASDAQ index values, are used as inputs to Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) models to predict stock market trends.

This repository includes scripts for data preprocessing, model training, performance evaluation, and results visualization, providing a reproducible framework for the experiments presented in the draft paper.

## Disclaimer
This repository contains code related to a draft paper that is currently under review. The details and results are subject to change. If you have any questions, please feel free to contact us.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Code Overview](#code-overview)

## Introduction
This repository accompanies a draft paper titled:  
**"Predicting NASDAQ Stock Prices Through Sentiment Analysis of U.S. President’s Social Media Posts"**  
*(Currently under review, preprint not yet available)*

The repository provides code for reproducing the core experiments described in the draft paper. Once the paper is finalized and published, the README will be updated to include a formal citation.

## Dataset
The dataset used in this project is located in the `data` directory.
| Data File                | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `text_and_sentiment.csv` | Dataset with sentiment scores calculated using VADER and RoBERTa based on the `text` column. |
| `sentiment_and_nasdaq.csv` | Dataset created by performing an inner join with NASDAQ data based on the `date` column.     |


## Code Overview
Below is a breakdown of the code files and their intended purposes, along with their relationship to the draft paper:

| Code File                                   | Paper Section                               | Description                                                                                     |
|--------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------|
| `01_TrumpCrawling.py`                      | Section 4.1.2: Data Collection              | Crawls Truth Social data using Beautiful Soup 4.                                               |
| `02_nasdaq.ipynb`                          | Section 4.1.2: Data Collection              | Collects NASDAQ data using the Finance Data Reader library.                                     |
| `03_preprocess.ipynb`                      | Section 4.1.3: Data Preprocessing           | Performs data preprocessing, such as converting dates to EST, removing URLs, and handling missing values. |
| `04_EDA.ipynb`                             | Section 4.1.3: Data Preprocessing           | Conducts basic exploratory data analysis (EDA) on preprocessed data.                           |
| `05_VADER and RoBERTa sentiment analysis.ipynb` | Section 4.2.2: Utilizing Sentiment Analysis Results | Conducts sentiment scoring using VADER and RoBERTa.                                            |
| `06_data join.ipynb`                       | Section 4.2.3: Time Series Prediction Model | Merges Trump data with NASDAQ data.                                                            |
| `07_LSTM.ipynb`                            | Section 5.1: LSTM                           | Trains and evaluates the performance of the LSTM model.                                         |
| `08_GRU.ipynb`                             | Section 5.2: GRU                            | Trains and evaluates the performance of the GRU model.                                          |
