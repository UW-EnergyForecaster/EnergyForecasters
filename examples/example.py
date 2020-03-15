import sys

# Required to import packages from other directory
sys.path.insert(1, "./energyforecaster/")

import energyforecast

location = "STAC"
capacity = 2
ML = "LR"
print(energyforecast.live_predict(location, capacity, ML))
