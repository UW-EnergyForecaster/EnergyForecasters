import pandas as pd  
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def model(x_columns):
    '''
    This fuction generates a Random Forest Regression model.
    :param x_columns: columns that are available in the real-time data source
    :type x_columns: list
    :return: model of the Random Forest Regression
    :rtype: Random Forest Regression
    '''
    dataset = pd.read_csv('../energyforecaster/data/no_0_solar_with_interpolation.csv')
    labels = np.array(dataset['normalized_solar'])
    features= dataset[x_columns]
    # Saving feature names for later use
    feature_list = list(features.columns)
    # Convert to numpy array
    features = np.array(features)
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
    # Instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    # Train the model on training data
    rf.fit(train_features, train_labels)
    return rf