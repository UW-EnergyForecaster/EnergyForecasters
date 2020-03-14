'''
    The code creates a Lasso regression model using the sklearn Lasso library.
    It involves importing the data, choosing the appropriate columns,
    and generating the model.
'''

import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

def model(x_columns):
    '''
        This fuction generates a Lasso Regression model.

        :return: model of the Lasso Regression
        :rtype: Lasso Class
    '''
    dataset = pd.read_csv('../energyforecaster/data/no_0_solar_with_interpolation.csv')

    # Dropping NA values
    dataset.dropna(inplace=True)

    # Dropping Weird column
    dataset.pop("Unnamed: 0")

    y_column = "Normalized_Solar_lin"
    # Splitting the data.
    x_train, x_test, y_train, y_test = train_test_split(
        dataset[x_columns], dataset[y_column], test_size=0.33)

    # The Lasso model
    regr = Lasso(alpha=0.1)
    regr = regr.fit(x_train, y_train)
    return regr
