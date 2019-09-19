# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:06:14 2019

@author: emirk

This function evaluates the performance of a binary classifier.

Inputs:
    
    y= actual labels in the form of np. array
    
    y_pred = predicted labesl in the form of np.array
    
    dec_digits (optional) = number of decimal points to use in displaying scores
    
    pos_label (optional) = the positive class of interest that will be evaluated in the precision, recall and f-1 score metrics
    
    
Outputs:

    Prints the following scores in order

    1. Accuracy
    2. Precision
    3. Recall
    4. f-1 score
    5. AUC score    

"""

import numpy as np
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score

def evaluate_performance(y,y_pred,dec_digits=3,pos_label=-1):
     print("Accuracy: {0}".format(round(accuracy_score(y,y_pred),dec_digits)))
     print("Precision: {0}".format(round(precision_score(y,y_pred,pos_label=pos_label,average='binary'),dec_digits)))
     print("Recall: {0}".format(round(recall_score(y,y_pred,pos_label=pos_label,average='binary'),dec_digits)))
     print("f-1 score: {0}".format(round(f1_score(y,y_pred,pos_label=pos_label,average='binary'),dec_digits)))
     print("AUC score: {0}".format(round(roc_auc_score(y,y_pred),dec_digits)))

def display_scores(scores):
    print("Scores: {0}\nMean: {1:.3f}\nStd: {2:.3f}".format(scores, np.mean(scores), np.std(scores)))