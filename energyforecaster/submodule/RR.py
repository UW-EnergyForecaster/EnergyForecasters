
'''

    The code creates a Ridge regression model using the sklearn library.

    It involves importing the data, choosing the appropriate columns,

    and generating the model.

'''

import pandas as pd

from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split

def model(x_columns):

    '''

        This fuction generates a Ridge Regression model.

        :param x_columns: columns from real-time data source

        :type x_columns: list

        :return: model of the Ridge Regression

        :rtype: Ridge Class

    '''

    dataset = pd.read_csv('./energyforecaster/data/no_0_solar_with_interpolation.csv')

    # Dropping NA values

    dataset.dropna(inplace=True)

    # Dropping Weird column

    dataset.pop("Unnamed: 0")

    y_column = "Normalized_Solar_lin"

    # Splitting the data.

    x_train, x_test, y_train, y_test = train_test_split(

        dataset[x_columns], dataset[y_column], test_size=0.33)

    # The Ridge model

    regr = Ridge(alpha=0.1)

    regr = regr.fit(x_train, y_train)

    return regr