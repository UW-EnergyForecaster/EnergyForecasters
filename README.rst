# EnergyForecasters <img align="center" src='logo.png'>

[![Build Status](https://travis-ci.org/UW-EnergyForecaster/EnergyForecasters.svg?branch=master)](https://travis-ci.org/github/UW-EnergyForecaster)
[![Coverage Status](https://coveralls.io/repos/github/UW-EnergyForecaster/EnergyForecasters/badge.svg?branch=master)](https://coveralls.io/github/UW-EnergyForecaster/EnergyForecasters?branch=master)

This is a class project for University of Washington DIRECT program in Winter 2020.

The objective is to give a real-time feedback of generated solar power based on regression models from historical data. The user must choose one of six weather observation stations, input the capacity, and choose one of five regression methods, which include Random Forest, Neural Network, Multi Linear, Lasso, and Ridge regression.

## Organization

    EnergyForecaster/
        |- doc/
            |- Energy_forecasters_project_proposal.pptx
            |- Project Flow.png
            |- Technology Review.pdf
            |- user_cases.txt
        |- Energyforecaster/
            |- data/
                |- no_0_solar_with_interpolation.csv
                |- ...
            |- submodule/
                |- LR.py
                |- MLR.py
                |- NN.py
                |- RF.py
                |- RR.py
            |- tests/
                |- test_energyforecast.py
            |- energyforecaster.py
        |- examples/
            |- data_cleaning/
                |- ...
            |- fuel_generation_data/
                |- ...
            |- nrel_weather_data/
                |- ...
            |- nrel_weather_webscrape/
                |- ...
            |- regression_methods/
                |- ...
            |- example.py
        |- LICENSE
        |- README.md
        |- environment.yml
        |- .gitignore
        |- .coveragerc
        |- logo.png
        |- setup.py

## Getting Started

### Prerequisites

Windows user: Windows preview, Ubuntu  <a href="https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd">Instructions</a>

Mac OS: Terminal


### Installing

1. git clone https://github.com/UW-EnergyForecaster/EnergyForecasters
2. open energyforecaster file
3. pip install noise

### Module code

We place the module code in a file called `energyforecaster/energyforecaster.py`.

All the regression models are placed under the `submodule` directory.

Test file is called `test_energyforecast.py` is under `energyforecaster/tests`, which can be used as a test for the `energyforecaster.py`.

Examples of using the code can be seen in `examples/example.py`, where a user inputs simple command to test all available combinations.

### Project Data

In this project, the data includes both weather and solar energy data, which are stored in `Energyforecaster/data` folder in csv format. A user may choose to use their own dataset in training the regression methods.

Data used in training the models:
* Historical weather data from Texas state
* Solar energy output from Texas state

Due to the increase in solar capacity over the years, our solar generation data showed significant increase in recent measurements. A linear interpolation of existing data on installed capacity was used to normalize our solar generation data. This process could be seen in the `examples/data_cleaning/data_combining.ipynb`.

## Running the Tests
Tests can be run using the [nosetests](https://nose.readthedocs.io/en/latest/) package.

NOTE: tests must be run in the root directory due to pathing errors in the submodule.

`nosetests energyforecaster/tests/test_energyforecast.py`

### Style Tests
This project is following PEP8 style using the [flake8](https://flake8.pycqa.org/en/latest/) code checker.

### Template




## Built With
* **Google colaboratory** - Jupyter notebook online version
* **sklearn** - Feature selection,Prediction model


## Authors

* **Daniel Chai** - MS, Materials Science
* **Xinyue Wang** - MS, Materials Science
* **Zang Le** - PhD, Chemical Engineering
* **Ruidong Ma** - MS, Mechanical Engineering
