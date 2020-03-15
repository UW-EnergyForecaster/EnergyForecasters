import sys

# Required to import packages from other directory
sys.path.insert(1, "./energyforecaster/")

import energyforecast

def test_live_predict():
    '''
        Testing the live_predict method from the energyforecast.py
    '''

    # Testing different location inputs
    try:
        energyforecast.live_predict(1, 2, 3)
    except TypeError: # location should be a string
        pass
    else:
        raise Exception("Should be getting TypeError for location type")

    try:
        energyforecast.live_predict("123", 2, 3)
    except ValueError: # location should be one of the available locations
        pass
    else:
        raise Exception("Should be getting ValueError for wrong location")

    # Testing different capacity inputs
    try:
        energyforecast.live_predict("BMS", "1", 3)
    except TypeError: # capacity should be an integer or a float
        pass
    else:
        raise Exception("Should be getting TypeError for wrong capacity type")

    try:
        energyforecast.live_predict("BMS", -1, 3)
    except ValueError: # Capacity cannot be negative
        pass
    else:
        raise Exception("Should be getting ValueError for negative capacity")

    assert energyforecast.live_predict("BMS", 0, "LR") == 0, "0 user capacity\
        should not be able to generate any power."

    # Testing different machine learning inputs
    try:
        energyforecast.live_predict("BMS", 1, 3)
    except TypeError: # ML should be a string
        pass
    else:
        raise Exception("Should be getting TypeError for wrong ML input type")

    try:
        energyforecast.live_predict("BMS", 1, "123123")
    except ValueError: # ML should be a within the list of available methods
        pass
    else:
        raise Exception("Should be getting ValueError for wrong ML input value")
