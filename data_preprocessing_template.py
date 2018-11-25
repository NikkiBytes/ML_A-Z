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