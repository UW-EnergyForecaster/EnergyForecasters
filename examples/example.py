import sys

# Required to import packages from other directory
sys.path.insert(1, "./energyforecaster/")

import energyforecast

'''
    Available Locations:
        1. BMS: NREL Solar Radiation Research Laboratory - located in
            Golden, Colorado
        2. STAC: Solar Technology Acceleration Center - located in
            Aurora, Colorado
        3. UOSMRL: University of Oregon - located in Eugene, Oregon
        4. VTIF: NREL Vehicle Testing and Integration Facility - located in
            Arvada, Colorado

    Available Machine Learning Algorithms:
        1. MLR: Multilinear Regression
        2. LR: Lasso Regression
        3. RR: Ridge Regression
        4. RF: RandomForest Regressor
        5. NN: Neural Network
'''

capacity = 1
for location in ["BMS", "STAC", "UOSMRL", "VTIF"]:
    for ML in ["MLR", "LR", "RR", "RF", "NN"]:
        print(energyforecast.live_predict(location, capacity, ML))
