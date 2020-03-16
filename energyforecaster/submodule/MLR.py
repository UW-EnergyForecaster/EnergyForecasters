import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def model(x_columns):
    '''
        This fuction generates a Multiple Linear Regression model.

        :param x_columns: columns from the real-time data source
        :type x_columns: list
        :return: model of the Multiple Linear Regression
        :rtype: Multiple Linear Regression class
    '''

    dataset = pd.read_csv(
        './energyforecaster/data/no_0_solar_with_interpolation.csv')

    # split to train and test data
    X = dataset[x_columns]
    y = dataset['Normalized_Solar_lin']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    # fit train data
    regressor.fit(X_train, y_train)

    return regressor
