import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import r2_score


def separateFeatureTarget(dataset,columns_all):
    '''this function will separate the data into the features and targets
    pre: target is 'normalized_solar' and the databset included that coloumn
    and split data into test and train data
    and return the train and test data
    '''
    labels = np.array(dataset['normalized_solar'])
    features= dataset[columns_all]
    # Saving feature names for later use
    feature_list = list(features.columns)
    # Convert to numpy array
    features = np.array(features)
return train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

def randomForestError(dataset,columns_all):
    '''this function will create randomForest to predict the target data 
    and print the mean absolute error, mean squared error and R squared error
    '''
    train_features, test_features, train_labels, test_labels = separateFeatureTarget(dataset,columns_all)
    # Instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    # Train the model on training data
    rf.fit(train_features, train_labels)
    # Use the forest's predict method on the test data
    predictions = rf.predict(test_features)
    print('Mean absolute Error:', metrics.mean_absolute_error(test_labels, predictions)) 
    print('Mean squared Error:', metrics.mean_squared_error(test_labels, predictions)) 
    print('R Squared Error:', r2_score(test_labels, predictions))
    plt.scatter(predictions,test_labels)
    plt.plot([0,1],[0,1], 'r--')
    