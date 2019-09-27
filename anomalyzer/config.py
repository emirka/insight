# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:15:10 2019

@author: emirk




Method: loader(day_of_week,data_type,subtype)

Returns the path of data file to be loaded

Inputs:
    
    day_of_week (default='Tuesday') = Input which day of the week to be loaded
    
    data_type (default='processed') =  Input which data type to be loaded ('processed', 'cleaned' or 'raw')
    
    subtype (default='Normalized) = Input which data subtype to be loaded ('Normalized' or 'Reduced'). WARNING: Only use this if data type is 'processed'


Output: Data file to be loaded. 



Method: novelty_detection_preparation(method)


Prepares the dataset for novelty analysis.  Loads the data and combine BENIGN traffic into a single data frame and ATTACK traffic into different data frames for each day.

Days to consider: 
- Monday (all benign)
- Tuesday (97% benign)
- Wednesday (64% benign)

Inputs:

       
    method (default value ='Anomaly') = Can be either 'Anomaly' or 'Mixed'. If 'Anomaly', all BENIGN traffic will be used for training and all ANOMALY traffic will be used for testing
      
    
Output (train_data, tue_test_data, wed_test_data)

    train_data: The features of the dataset
        
    tue_test_data: Class labels of the dataset 
    
    tue_test_data: Class labels of the dataset 

"""

import os
import pandas as pd
from sklearn.model_selection import train_test_split


def loader(day_of_week='Tuesday',data_type='processed',subtype='Normalized'):

    data_directory='../data/'+data_type+'/'+subtype
    file_name=day_of_week+'_'+data_type+'.pkl'

    return os.path.join(data_directory,file_name)


def novelty_detection_preparation(method='Anomaly'):
    
    data_file = loader(day_of_week='Monday',data_type='processed',subtype='Normalized')
    Mon_data = pd.read_pickle(data_file)

    data_file = loader(day_of_week='Tuesday',data_type='processed',subtype='Normalized')
    Tue_data = pd.read_pickle(data_file)

    data_file = loader(day_of_week='Wednesday',data_type='processed',subtype='Normalized')
    Wed_data = pd.read_pickle(data_file)
    
    if method == 'Anomaly':
    
        mon_benign_data = Mon_data.loc[Mon_data['Label']=='BENIGN']
        tue_benign_data = Tue_data.loc[Tue_data['Label']=='BENIGN']
        wed_benign_data = Wed_data.loc[Wed_data['Label']=='BENIGN']
    
        train_data = pd.concat([mon_benign_data,tue_benign_data,wed_benign_data],axis=0)
        tue_train_data = None
        wed_train_data = None
        
        tue_test_data = Tue_data.loc[Tue_data['Label']!='BENIGN']
        wed_test_data = Wed_data.loc[Wed_data['Label']!='BENIGN']
    
    elif method == 'Mixed':
    
        mon_benign_data = Mon_data.loc[Mon_data['Label']=='BENIGN']  
        tue_benign_data = Tue_data.loc[Tue_data['Label']=='BENIGN']
        wed_benign_data = Wed_data.loc[Wed_data['Label']=='BENIGN']
     
        tue_anomaly_data = Tue_data.loc[Tue_data['Label']!='BENIGN']
        wed_anomaly_data = Wed_data.loc[Wed_data['Label']!='BENIGN']
    
        tue_train_data, tue_test_data = train_test_split(tue_benign_data,test_size=0.1,random_state=42)
        wed_train_data, wed_test_data = train_test_split(wed_benign_data,test_size=0.1,random_state=42)
    
        train_data = pd.concat([mon_benign_data,tue_train_data,wed_train_data],axis=0)
    
        tue_test_data = pd.concat([tue_test_data,tue_anomaly_data],axis=0) 
        wed_test_data = pd.concat([wed_test_data,wed_anomaly_data],axis=0)
    
    else:
        print("Not a valid choice")
        
   
    return train_data, tue_test_data, wed_test_data