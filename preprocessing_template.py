#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:21:40 2018

@author: nikkibytes
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

dataset = pd.read_csv("/Users/nikkibytes/Documents/ML_A-Z/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/Data_Preprocessing/Data.csv")
# Matrix of features (independent)
X = dataset.iloc[:, :-1].values
# -- here we said take all lines, then take all columns except the last column
# Variable vector (dependent)
y = dataset.iloc[:, 3].values
## --here we take all lines, from column 3

# Spliting dataset into train and test set 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


"""
# Feature scaling
from sklearn.preprocessing import StandardScaler 
sc_X = StandardScaler() 
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""