'''
    The Random Forest Regressor allows us to get a importance value of various properties.
    We ran this code first to use in feature selection, which then was used in various regression models.
    We tested two different datasets: 1. With 0 solar generation values, 2. without 0 solar generation values.
    We expect the two datasets to yield different results.
    This notebook involves importing the data, generating the model, and plotting the most important features.
'''

import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Importing the data
# The with0 data has 0 solar generation values.
with0_data = pd.read_csv('../data/out_with_interpolation.csv')
# Dropping NA values
with0_data.dropna(inplace=True)
# Dropping weird column
with0_data.pop("Unnamed: 0")

# Importing the data
# The no0 data has no 0 solar generation values.
no0_data = pd.read_csv('../data/no_0_solar_with_interpolation.csv')
# Dropping NA values
no0_data.dropna(inplace=True)
# Dropping weird column
no0_data.pop("Unnamed: 0")

# Selecting all the relevant parameters for feature selection.
x_columns = ['DHI', 'DNI', 'GHI', 'Cloud Type', 'Dew Point',
             'Solar Zenith Angle', 'Surface Albedo', 'Wind Speed',
             'Wind Direction', 'Relative Humidity', 'Temperature', 'Pressure']
y_column = "Normalized_Solar_lin"

# Splitting the data
with0_x_train, with0_x_test, with0_y_train, with0_y_test = train_test_split(
    with0_data[x_columns], with0_data[y_column], test_size=0.33, random_state=42)

# Splitting the data
no0_x_train, no0_x_test, no0_y_train, no0_y_test = train_test_split(
    no0_data[x_columns], no0_data[y_column], test_size=0.33, random_state=42)

# The random forest regressor model
# Regressor is used instead of classifier due to the numerical nature of our properties
with0_forest = RandomForestRegressor(n_estimators=100, random_state=42)
with0_forest.fit(with0_x_train, with0_y_train)

# The random forest regressor model
no0_forest = RandomForestRegressor(n_estimators=100, random_state=42)
no0_forest.fit(no0_x_train, no0_y_train)

# Plotting the feature importance of our dataset
importances = with0_forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in with0_forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(with0_x_train.shape[1]):
    print(x_columns[indices[f]] + " %d. feature %d (%f)" %
          (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(with0_x_train.shape[1]), importances[indices],
        color="r", yerr=std[indices], align="center")
plt.xticks(range(with0_x_train.shape[1]), indices)
plt.xlim([-1, with0_x_train.shape[1]])
plt.show()

importances = no0_forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in no0_forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(no0_x_train.shape[1]):
    print(x_columns[indices[f]] + " %d. feature %d (%f)" %
          (f + 1, indices[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(no0_x_train.shape[1]), importances[indices],
        color="r", yerr=std[indices], align="center")
plt.xticks(range(no0_x_train.shape[1]), indices)
plt.xlim([-1, no0_x_train.shape[1]])
plt.show()

'''
    Conclusion:
    There is difference between with0 and no0 datasets.
    First, there is a difference in feature rankings. The parameters that the model
    considers important is different. Second, the black lines, which represents the
    deviation of the parameters, are smaller in the no0 dataset. This is very
    significant since it represents that the model has confidence in choosing these
    variables as important. Third, the score of the model is higher in the with0
    model compared to no0 model, whic means that the with0 model was more successful
    in predicting the y values. With these observations, we determined that the no0
    model is more suitable for us to use in further regression models. This is
    largely due to the second observation, difference in deviation. Because lower
    deviation means more confidence in the feature importance, the no0 model is more
    reliable than the with0 model despite the lower score. Even the score of 0.76
    is not too bad.
'''
