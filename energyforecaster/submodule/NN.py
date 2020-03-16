import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.neural_network import MLPRegressor


def model(x_columns):
    '''
    This fuction generates an Artificial Neural Network  Regression model.
    :param x_columns: columns that are available in the real-time data source
    :type x_columns: list
    :return: model of the Neural Network Regression
    :rtype: Neural Network
    '''
    dataset = pd.read_csv('../data/no_0_solar_with_interpolation.csv')
    # Dropping unneccesary column
    for label in ['Unnamed: 0', 'Date', 'hhmm', 'Installed', 'Fill Flag']:
        if label in dataset.columns:
            dataset.drop(label, axis=1, inplace=True)
    y_column = "Normalized_Solar_lin"

    # Data normalization:
    scaler = preprocessing.StandardScaler()
    X_pn = dataset[x_columns]
    y_pn = np.array(dataset[y_column])
    X_normalized = scaler.fit_transform(X_pn)

    # Splitting the data and fit with model:
    X_train, x_test, y_train, y_test = train_test_split(
        X_normalized, y_pn, test_size=0.33)
    regr = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(50, 50))
    regr.fit(X_train, y_train)

    return regr
