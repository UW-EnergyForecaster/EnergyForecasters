# EnergyForecasters <img src='logo.png'>

[![Build Status](https://travis-ci.org/UW-EnergyForecaster/EnergyForecasters.svg?branch=master)](https://travis-ci.org/github/UW-EnergyForecaster)
[![Coverage Status](https://coveralls.io/repos/github/UW-EnergyForecaster/EnergyForecasters/badge.svg?branch=master)](https://coveralls.io/github/UW-EnergyForecaster/EnergyForecasters?branch=master)

This is a class project for University of Washington DIRECT program in Winter 2020.

The objective is to give a real-time feedback of generated solar power based on regression models from historical data. The user must choose one of six weather observation stations, input the capacity, and choose one of five regression methods, which include Random Forest, Neural Network, Multi Linear, Lasso, and Ridge regression.

## Directory
doc:
* Energy_forecasters_project_proposal.pptx
* Project Flow.png
* Technology Review.pdf
* user_cases.txt

Energyforecaster:
* data:  
    * cleaned_solar_generation_data.csv
    * no_0_solar_with_interpolation.csv
    * normalized_by_2000_dtpts.csv
    * out_with_interpolation.csv
    * processed_data.csv
    * Texas_weather_solar_generation_data_2013-2018.csv
* submodule:
    * LR.py  
    * MLR.py  
    * NN.py  
    * RF.py  
    * RR.py  
* tests:  
    * test_energyforecast.py  
* energyforecast.py

examples:
* data_cleaning:
    * data_combining.ipynb
    * Fuel_Mix_data_cleaning.ipynb
* fuel_generation_data:  
    * IntGenByFuel2007.xls ~ IntGenByFuel2019.xls
    * cleaned_solar_generation_data.csv
* nrel_weather_data:  
    * 734232_29.77_-95.38_2007.csv ~ 734232_29.77_-95.38_2018.csv
* nrel_weather_webscrape:  
    * NREL_weather_data_webscrape.ipynb
* regression_methods:  
    * feature_selection_multilinear_regression_and_kfold.ipynb
    * LassoRegression.ipynb
    * MLR_kfold_CV.py
    * Neural_Network.ipynb
    * RandomForest_Regression.ipynb
    * RF_evaluation.py
    * RF_kfold_CV.py
    * RidgeRegression.ipynb
* example.py

LICENSE

README.md

environment.yml

.gitignore

.coveragerc

logo.png

setup.py

## Getting Started

By following the below procedures, prediction of real time solar energy output in one of the six location can be given. In order to fast and easy use the codes, please follow the procedure in order.

### Prerequisites

Windows user: Windows preview, Ubuntu  <a href="https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd">Instructions</a>

Mac OS: Terminal  

### Project Data

In this project, the data includes both weather and solar energy data, which are stored in database and examples directory in csv format. Thus user can  replace the data if same format and type data can be provided. The data is mounted in google drive, so in order to access the data there will be some command to mount the drive.  

Data        : Weather data from Texas state  
              Solar Energy output from Texas state

Beside the raw data, pre-cleaning process of data is necessary since not all the information is valuable and normalization process is also help the project get a better result. In this process, zero value of solar energy output is dropped and be normalized by dividing the capacity.


### Installing  

1. git clone https://github.com/UW-EnergyForecaster/EnergyForecasters
2. open energyforecaster file
3. pip install noise

### Module code

We place the module code in a file called `energyforecast.py` in a directory called `Energyforecaster `.
All the function files (.py files) are placed under the `submodule` directory.
Test file is called `test_energyforecast.py` is also under `Energyforecaster/tests`, which can be used as a test for the `energyforecast.py`.
Examples are available.

## Running the tests
once you have cloned the directory to your local machine, follow the directions below:  

1. cd energyforecaster
2. cd test
3. nosetests test_energyforecast.py

### And coding style tests
This project is following PEP8 style using the flake8 code checker.

### Template




## Built With
* **Google colaboratory** - **Jupyter notebook online version**
* **sklearn** - **Feature selection,Prediction model**


## Authors

* **Daniel Chai** - **MS, Materials Science**
* **Xinyue Wang** - **MS, Materials Science**
* **Zang Le** - **PhD, Chemical Engineering**
* **Ruidong Ma** - **MS, Mechanical Engineering**


## License

MIT License

Copyright (c) 2020 UW-EnergyForecaster

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Acknowledgements

This is only a class project, any
