import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import r2_score
import RandomForest_Regression as rfr


dataset = pd.read_csv('/Users/xinyuewang/Downloads/normalized_by_2000_dtpts.csv')
# Labels are the values we want to predict
# Remove the labels from the features
# axis 1 refers to the columns
columns_all= ['DHI', 'DNI', 'GHI', 'Cloud Type', 'Dew Point', 
             'Solar Zenith Angle', 'Surface Albedo', 'Wind Speed', 
             'Wind Direction', 'Relative Humidity', 'Temperature', 'Pressure']
RFcolumns=['Relative Humidity','Solar Zenith Angle','GHI','Surface Albedo','Wind Direction']
multilinearColumns=['Surface Albedo','Temperature','Relative Humidity','Solar Zenith Angle','Pressure']
def test_separateFeatureTarget():
    rfr.separateFeatureTarget(dataset,columns_all)
    assert features.shape == (51469, 12), "wrong shape for feature data"
    assert train_features.shape == (38601, 12), "wrong shape for train_features data"
    assert train_labels.shape == (38601,),  "wrong shape for train_labels data"
    assert test_features.shape == (12868, 12),  "wrong shape for test_features data"
    assert test_labels.shape == (12868,),  "wrong shape for test_labels data"
    
def test_randomForestError():
    rfr.randomForestError(dataset,columns_all)
    assert round(metrics.mean_absolute_error(test_labels, predictions), 2) == 0.11, "wrong mean absolute error"