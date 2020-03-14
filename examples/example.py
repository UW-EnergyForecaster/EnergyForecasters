

import sys

sys.path.insert(1,"../energyforecaster/")
import energyforecast

location = "BMS"
capacity = 2
ML = "LR"
print(energyforecast.live_predict(location, capacity, ML))
