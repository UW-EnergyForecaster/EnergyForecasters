'''
    This notebook involves importing the data, generating the model,
    and plotting the most important features.
'''

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def model(x_columns):
    '''
        This fuction generates a RandomForestRegressor model.

        :param x_columns: columns from the real-time data source
        :type x_columns: list
        :return: model of the Lasso Regression
        :rtype: RandomForestRegressor class
    '''
    # Importing the data
    # The no0 data has no 0 solar generation values.
    no0_data = pd.read_csv('../energyforecaster/data/no_0_solar_with_interpolation.csv')

    # Dropping NA values
    no0_data.dropna(inplace=True)

    # Dropping weird column
    no0_data.pop("Unnamed: 0")

    # Selecting the relevant parameters for feature selection.
    y_column = "Normalized_Solar_lin"

    # Splitting the data
    no0_x_train, no0_x_test, no0_y_train, no0_y_test = train_test_split(
        no0_data[x_columns], no0_data[y_column], test_size=0.33)

    # The random forest regressor model
    no0_forest = RandomForestRegressor(n_estimators=100)
    no0_forest.fit(no0_x_train, no0_y_train)
    return no0_forest
