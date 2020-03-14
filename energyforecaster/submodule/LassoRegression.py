'''
    The code creates a Lasso regression model using the sklearn Lasso library.
    It involves importing the data, choosing the appropriate columns,
    and generating the model.
    Residual plots and "Predicted vs Test values" graphs are also produced.
'''

import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

dataset = pd.read_csv('../data/no_0_solar_with_interpolation.csv')

# Dropping NA values
dataset.dropna(inplace=True)

# Dropping Weird column
dataset.pop("Unnamed: 0")

'''
Feature rankings from the RandomForest
Relative Humidity 1. feature 9 (0.346642)
Solar Zenith Angle 2. feature 5 (0.149772)
GHI 3. feature 2 (0.090975)
Surface Albedo 4. feature 6 (0.083799)
Wind Direction 5. feature 8 (0.078191)
'''

# The columns we care about according to the random forest regressor.
x_columns = ['GHI', 'Solar Zenith Angle', 'Surface Albedo',
             'Wind Direction', 'Relative Humidity']
y_column = "normalized_solar"

# Splitting the train and test data
x_train, x_test, y_train, y_test = train_test_split(
    dataset[x_columns], dataset[y_column], test_size=0.33, random_state=42)

# Lasso Regression model
regr = Lasso(alpha=0.1)

# The predicted y_test value
y_pred = regr.fit(x_train, y_train).predict(x_test)

# R^2 score of the model
r2_score = regr.score(x_test, y_test)

# Residual graph to observe bias in the model.
# No clear pattern shows that there is no bias in the model.
residual = y_pred - y_test

# "i" decides the number of datapoints
# The data points are random since the train_test_split randomly splits the data.
num_data = 20
plt.scatter(range(num_data), residual[:num_data])

# Graph to show the predicted vs test data.
fig = plt.figure(figsize=(20, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(range(num_data), y_pred[:num_data], color='blue', label="predicted")
ax.plot(range(num_data), y_test[:num_data], color='orange', label="test")
ax.legend()

# Lasso is able to remove effects of unimpactful variables.
# Which means that we should be able to put as many properties as I want.
more_x_columns = ['DHI', 'DNI', 'GHI', 'Cloud Type', 'Dew Point',
                  'Solar Zenith Angle', 'Surface Albedo', 'Wind Speed',
                  'Wind Direction', 'Relative Humidity', 'Temperature', 'Pressure']

# Splitting the data.
more_x_train, more_x_test, more_y_train, more_y_test = train_test_split(
    dataset[more_x_columns], dataset[y_column], test_size=0.33, random_state=42)

# The Lasso model
more_regr = Lasso(alpha=0.1)
more_y_pred = more_regr.fit(more_x_train, more_y_train).predict(more_x_test)
more_r2_score = more_regr.score(more_x_test, more_y_test)

# Residual graph to see bias.
# A little bit of a pattern, I am not sure if this is of concern.
more_residual = more_y_pred - more_y_test
plt.scatter(range(num_data), more_residual[:num_data])

# Predicted vs test value
fig = plt.figure(figsize=(20, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(range(num_data), y_pred[:num_data], color='blue', label="predicted")
ax.plot(range(num_data), y_test[:num_data], color='orange', label="test")
ax.legend()
