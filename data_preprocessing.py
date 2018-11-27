#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:09:55 2018

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


# Taking care of missing data
from sklearn.preprocessing import Imputer  
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() #object
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])  #make first column modified encoding 
# Make dummy variables
onehotencoder = OneHotEncoder(categorical_features=[0]) #specify features
X =onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Spliting dataset into train and test set 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature scaling
from sklearn.preprocessing import StandardScaler 
sc_X = StandardScaler() 
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

