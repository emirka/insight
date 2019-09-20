# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:55:36 2019

@author: emirk

Prepares the dataset for analysis. Works with both classification and anomaly detection algorithms

Inputs:
    
    data = Data frame to be prepared
       
    class_column (default value ='Label') = Name of the column containing the class labels (must be a string)
      
    classes (default value= 'binary')     = If the type of job is classification, how many class to work with. Either 'binary' or 'multi'
    
    neg_class (defualt '') = specificy the negative class (if 'binary)
    
Output (X,y)

    X: The features of the dataset
        
    y: Class labels of the dataset 

"""
import pandas as pd
import numpy as np

def prepare_data(data, class_column='Label',classes='binary', neg_class=''):
    
    y= np.array(data[class_column])
    X= np.array(data.loc[:, data.columns != class_column])

    if classes =='binary':
        y= (y != neg_class)
        y=y.astype(int)
           
    return X,y