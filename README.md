# EnergyForecasters <img src='logo.png'>

[![Build Status](https://travis-ci.org/UW-EnergyForecaster/EnergyForecasters.svg?branch=master)](https://travis-ci.org/github/UW-EnergyForecaster)
[![Coverage Status](https://coveralls.io/repos/github/UW-EnergyForecaster/EnergyForecasters/badge.svg?branch=master)](https://coveralls.io/github/UW-EnergyForecaster/EnergyForecasters?branch=master)

This is a class project for University of Washington DIRECT program in Winter 2020.

The objective is to give a real-time feedback of generated solar power based on regression models from historical data. By using this project, users are allowed to choose one of six weather observation satations, input the capacity, and choose one of five regession methods, which include RandomForest, NeuralNetwork, Mutilinear, Lasso, Ridge regression.

## File List
database:  
            Teaxs_weather_solar_generation_data_2013-2018.csv
            processed_data.csv

doc:
            Energy_forecasters_project_proposal.pptx
            Technology Review.pdf
            user_cases.txt

Energyforecaster:
            data:  
                    cleaned_solar_generation_data.csv
                    no_0_solar_with_interpolation.csv
                    normalized_by_2000_dtpts.csv
                    out_with_interpolation.csv
            submodule:
                    ANN.py  
                    MLR.py  
                    RFR.py  
                    RF_evaluation.py  
                    setup.py  
             test:  
                    test_energyforecast.py  
             energyforecast.py

examples:
             Fuel_Generation_Data:  
                    IntGenByFuel2007.xls ~ IntGenByFuel2019.xls
                    cleaned_solar_generation_data.csv
             NREL_Weather_Data:  
                    734232_29.77_-95.38_2007.csv ~ 734232_29.77_-95.38_2018.csv
             NREL_weather_webscrape:  
                    NREL_weather_data_webscrape.ipynb
             regression_methods:  
                    Neural_Network.ipynb
             example.py
LICENSE  
README.md  
environment.yml  
logo.png  
setup.py

## Getting Started

By following the below procedures, prediction of real time solar engery output in one of the six location can be given. In order to fast and easy use the codes, please follow the procedure in order.

### Prerequisites

Windos user : Windows preveiw, Ubuntu  
              <p>An <a href="https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd">Instructions</a>.</p>

Mac OS      : Terminal  

### Project Data

In this project, the data includes both weather and soalr energy data, which are stored in database and examples directory in csv format. Thus user can  replace the data if same format and type data can be provided. The data is mounted in google drive, so in order to access the data there will be some command to mount the drive.  

Data        : Weather data from Teaxes state  
              Solar Energy output from Teaxes state

Beside the raw data, pre-cleanning process of data is neccessary since not all the information is valuable and normalization process is also help the project get a better result. In this process, zero value of solar energy output is dropped and be normalized by dividing the capacity.


### Installing  

1. git clone -url
2. open energyforecaster file
3. pip install noise
4.

### Module code

We place the module code in a file called ` energyforecast.py ` in a directory called `Energyforecaster `.

All the function files (.py files) are placed under the `submodule` directory.

Test file is called `test_energyforecast.py` is also under `Energyforecaster/tests`, which can be used as a test for the ` energyforecast.py `.

Examples are aviliabe.

## Running the tests

once you have cloned the directory to your local machine, follow the directions below:  
```
1. cd energyforecaster
2. cd test
3. noisetests test_energyforecast.py
```
Once the test is done, belwoing will be shown if the test run succeess.

### And coding style tests

This project is following   style for


### Template




## Built With

* **Google colaborate** - **Jupyter notebook online version**
* **sklearn** - **Feature selection,Prediction model**


## Authors

* **Daniel Chai** - **MS, Materials Science**
* **Xinyue Wang** - **MS, Materials Science**
* **Zhang Le** - **PhD, Chemical Engineering**
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
