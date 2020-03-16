import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import KFold

def kfold_CV(x_columns):
    dataset = pd.read_csv('./energyforecaster/data/no_0_solar_with_interpolation.csv')
    labels = np.array(dataset['Normalized_Solar_lin'])
    X_columns_all=dataset[x_columns]
    y=labels
    kf = KFold(n_splits=10, shuffle=True)# Define the split - into 10 folds 
    kf.get_n_splits(X_columns_all, y)# returns the number of splitting iterations in the cross-validator
    print(kf) 
    fig, ax = plt.subplots(figsize=(8,6))

    mse = np.zeros((12, 10))
    j = 0
    #creat train and test vars 
    for train_index, test_index in kf.split(X_columns_all, y):
        print("TRAIN:", train_index, "TEST:", test_index)
        #print("x-train[X_train.columns[0:2]]: ", X_train[X_train.columns[0:2].values])
        #print (X_train.shape, y_train.shape)
        #print (X_test.shape, y_test.shape)
        X_train, X_test = dataset[columns_all].iloc[train_index], dataset[columns_all].iloc[test_index]
        y_train, y_test = y[train_index], y[test_index]

        for i in range(1, 13):
            rf = RandomForestRegressor(n_estimators = 100, random_state = 42)#change estimator
            # Train the model on training data
            reg = rf.fit(X_train[X_train.columns[0:i].values], y_train)#use first i features train 
            y_pred = rf.predict(X_test[X_test.columns[0:i].values])

            mse[i-1, j] = metrics.mean_squared_error(y_test, y_pred)


        ax.plot(np.linspace(1, 11, 12), mse[:, j], linewidth=4, color='b', alpha=0.09)
        ax.set_ylabel('Mean Squared Error')
        ax.set_xlabel('Degree of Polynomial')
        j += 1

    avg_mse = mse.mean(axis=1)
    ax.plot(np.linspace(1, 11, 12), avg_mse, color='purple')
    