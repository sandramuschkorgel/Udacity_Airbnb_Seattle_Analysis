# Seattle Airbnb Analysis 🏡 🛌

Airbnb is often considered an alternative to hotels, lodgings, or any other traveller's accommodation. Though this is true, Airbnb listings greatly differ due to their individuality. Each listing has a different host, location, service, amenities and the like - making each of them a unique experience. The underlying notebook tries to shed some light on which features influence listing prices the most.

## Description

The jupyter notebook lays out the entire CRISP-DM (Cross-industry standard process for data mining) for an original Airbnb dataset. Therein are real Airbnb listings in and around Seattle from 2016. By running the notebook you are able to follow along each step in the process. You might as well jump to the modelling section directly, since I added the cleaned csv files to this repository.

The GitHub repository is structured as follows:

* 1 main jupyter notebook *DSND_Write_A_Data_Science_Blog_Post.ipynb*: Here you will find the entire CRISP-DM.
* 1 supplementary jupyter notebook *Airbnb_Boston_Analysis.ipynb*: To compare the Seattle and Boston Airbnb market I added this basic jupyter notebook containing the cleaning code for two of the csv files. These files are now ready to be used for modeling.
* Seattle and Boston Airbnb datasets (under *data*): The cleaned csv files can be downloaded as part of the zi files. Or just run the code inside the jupyter notebooks.

## Dependencies/Pre-requisites

In order to run this project install the following packages:

* [NumPy](https://numpy.org/install/) and [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [matplotlib](https://matplotlib.org/stable/users/installing.html) and [seaborn](https://seaborn.pydata.org/installing.html)  
* [scikit learn](https://scikit-learn.org/stable/install.html), [statsmodels](https://www.statsmodels.org/stable/install.html) and [patsy](https://pypi.org/project/patsy/)

## Installation and Usage

```bash
git clone https://github.com/sandramuschkorgel/Udacity_Airbnb_Seattle_Analysis.git
cd [project root directory]
jupyter notebook
```

## Read more

[Click here for my substack blog post](https://sandramuschkorgel.substack.com/p/why-airbnb-pricing-is-opaque)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Acknowledgments

This project is part of the Udacity [Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025). Thanks to [Airbnb](https://www.airbnb.com/) for providing the original datasets.
