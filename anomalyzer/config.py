# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 14:15:10 2019

@author: emirk

Returns the path of data file to be loaded

Inputs:
    
    day_of_week (default='Tuesday') = Input which day of the week to be loaded
    
    data_type (default='processed') =  Input which data type to be loaded ('processed', 'cleaned' or 'raw')
    
    subtype (default='Normalized) = Input which data subtype to be loaded ('Normalized' or 'Reduced'). WARNING: Only use this if data type is 'processed'


Output: Data file to be loaded. 

"""

#config.py 

import os

def loader(day_of_week='Tuesday',data_type='processed',subtype='Normalized'):

    data_directory='../data/'+data_type+'/'+subtype
    file_name=day_of_week+'_'+data_type+'.pkl'

    return os.path.join(data_directory,file_name)