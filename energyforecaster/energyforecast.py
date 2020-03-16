'''
    This is the main python which the user will interact with.
'''

import importlib
import requests
import re
import pandas as pd


def live_predict(location, capacity, ML):
    '''
        A function that outputs the real time generation data predicted from
        a Machine Learning model.

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

        :param location: One of the sites with readily available data
        :param capacity: User's own solar capacity
        :param ML: User's choise of Machine Learning algorithm
        :type location: String
        :type capacity: float/int
        :type ML: String
        :return: real-time solar generation value
        :rtype: float
    '''

    # Checking if the location is valid
    if not isinstance(location, str):
        raise TypeError("location must be a String")
    elif location not in ["BMS", "STAC", "UOSMRL", "VTIF"]:
        raise ValueError("The location value is invalid. Please refer to the\
            available location list.")
    else:
        pass

    # Checking if capacity is valid
    if not (isinstance(capacity, float) or isinstance(capacity, int)):
        raise TypeError("Capacity must be a float or an integer.")
    elif capacity < 0:
        raise ValueError("Capacity cannot be negative.")
    else:
        pass

    # Checking if ML algorithm is valid.
    if not isinstance(ML, str):
        raise TypeError("Machine learning algorithm must be a String")
    elif ML not in ["MLR", "LR", "RR", "NN", "RF"]:
        raise ValueError("The Machine learning algorithm is invalid. Please\
            refer to the available machine learning algorithm list.")
    else:
        pass

    print("Obtaining real-time weather data...")
    # Attempting to receive real-time data
    url = 'https://midcdmz.nrel.gov/apps/daily.pl?site='+location+'&live=1'
    response = requests.get(url)
    # if the download fails, this line will generate an error
    assert response.status_code == 200

    feature_dict = {}

    # Iterating through each lines of the web response to find property values
    # It will only extract the first value that it finds.
    # Splitting the response text by lines
    for line in response.text.splitlines():
        # Searching for the pattern
        result = re.search('<TD nowrap><DIV ALIGN=right>', line)
        if result is not None:
            # Properties that we want
            feature_list = ['Global', 'Direct', 'Diffuse', 'Wind Direction',
                            'Wind Speed', 'Zenith', 'Albedo', 'Relative\
                            Humidity', 'Air Temperature', 'Pressure']
            for feature in feature_list:
                if feature in line:
                    result = re.findall(r"[-+]?\d+\.\d+", line)
                    if feature not in feature_dict:
                        feature_dict[feature] = float(result[0])

    # We need to rename the column names to the database columns
    keys = list(feature_dict)
    for key in keys:
        if key == "Global":
            feature_dict["GHI"] = feature_dict["Global"]
            del feature_dict["Global"]
        elif key == "Direct":
            feature_dict["DNI"] = feature_dict["Direct"]
            del feature_dict["Direct"]
        elif key == "Diffuse":
            feature_dict["DHI"] = feature_dict["Diffuse"]
            del feature_dict["Diffuse"]
        elif key == "Zenith":
            feature_dict["Solar Zenith Angle"] = feature_dict["Zenith"]
            del feature_dict["Zenith"]
        elif key == "Albedo":
            feature_dict["Surface Albedo"] = feature_dict["Albedo"]
            del feature_dict["Albedo"]
        elif key == 'Air Temperature':
            feature_dict["Temperature"] = feature_dict['Air Temperature']
            del feature_dict['Air Temperature']
        else:
            pass

    # Importing Machine Learning Algorithm
    ml_module = importlib.import_module("submodule." + ML)

    # Creating a regression model from only the parameters available to us
    # from the real-time data
    print("Generating regression model...")
    ml_model = ml_module.model(feature_dict.keys())

    # Creating the dataframe out of the real-time weather and predicting our
    # energy generation value
    feature_df = pd.DataFrame([feature_dict])
    predicted_value = ml_model.predict(feature_df)

    print("\nPredicted Value: ")
    return predicted_value * capacity
