# Predicting NASDAQ Stock Prices Through Sentiment Analysis of U.S. President’s Social Media Posts
This project investigates the influence of U.S. President Donald Trump's social media posts on the NASDAQ Composite Index by leveraging sentiment analysis and deep learning-based time series prediction models. The code in this repository supports the experiments described in the draft paper, which aims to empirically validate how political sentiment impacts financial markets.

Using sentiment analysis tools like VADER and RoBERTa, the project extracts positive, neutral, and negative sentiment from the President's posts. The extracted sentiment data, along with historical NASDAQ index values, are used as inputs to Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) models to predict stock market trends.

This repository includes scripts for data preprocessing, model training, performance evaluation, and results visualization, providing a reproducible framework for the experiments presented in the draft paper.

## Disclaimer
This repository contains code related to a draft paper that is currently under review. The details and results are subject to change. If you have any questions, please feel free to contact us.

---

## Table of Contents
- [Introduction](#introduction)
- [Code Overview](#code-overview)
- [Dataset](#dataset)

---

## Introduction
This repository accompanies a draft paper titled:  
**"Draft Paper Title"**  
*(Currently under review, preprint not yet available)*

The repository provides code for reproducing the core experiments described in the draft paper. Once the paper is finalized and published, the README will be updated to include a formal citation.

---

## Code Overview
Below is a breakdown of the code files and their intended purposes, along with their relationship to the draft paper:

| Code File           | Paper Section               | Description                                                                 |
|---------------------|-----------------------------|-----------------------------------------------------------------------------|
| `data_preprocessing.py` | Section 2.1: Data Preprocessing | Code for preparing and cleaning the dataset before analysis.                |
| `model_training.py`    | Section 3.2: Model Training     | Implementation of the model described in the draft, including key algorithms.|
| `evaluation.py`        | Section 4.1: Evaluation Results | Evaluates model performance and generates results described in the draft.   |
| `visualization.py`     | Section 5: Results Visualization | Produces plots and visualizations used in the draft figures.                |

## Dataset
