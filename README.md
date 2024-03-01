# Exploratory Data Analysis 
# Customer Loans in Finance

![alt text](https://github.com/DARREN-LEVENE/exploratory-data-analysis---customer-loans-in-finance908/blob/main/Images/image-1.png)


## Project Description
This is a project looking at the Extract, Transform and Analysis process, focussing on customer loans data from a Financial Services Institution loan book.
Loading up the EDA_customer_loans.py will give the cleaning process and the analytical insight gained from the data for this type of project.


## Installation Instructions
To install this repo onto your local machine and view the scripts, navigate to the directory you would like the project to be cloned into. In a bash terminal, you can use the command `git clone https://github.com/DARREN-LEVENE/exploratory-data-analysis---customer-loans-in-finance908` to clone this repo, then to rename the directory you can use `mv exploratory-data-analysis---customer-loans-in-finance908 --YOUR FILE NAME--`. 

The exact conda enviroment for this project is stored in the enviroment.yaml file, and can be set up onto your local machine as follows:

`conda env create -n <environment_name> -f environment.yaml`

## Dependancies
Developed on Python 3.12.2 Required libraries:
- pandas
- numpy
- matplotlib
- seaborn
- ipykernel
- nbformat
- plotly
- statsmodels
- yaml
- psycopg2
- sqlalchemy
- missingno
- scipy
- scikit-learn


## File Structure
![Tree diagram](https://github.com/DARREN-LEVENE/exploratory-data-analysis---customer-loans-in-finance908/blob/main/tree.png?raw=true)

Data_visualisation.py - contains graphing methods

db_utils.py - contains the extractor class, running it with your own yaml file will create a connection and extract a table from a database storing it as a csv file

df_info.py - contains methods which summarise some key statistics in the dataframe

df_null_imputes.py - handles the imputations for the cleaning of the file

df_transformations.py - contains methods to handle the data type conversions

EDA_customer_loans.ipynb - is the main notebook file which contains the cleaning and analysis

load_credentials.py - contains a loading function for yaml files

loan_payments.csv - is dataset used for this project

tree.png - image used in readme


## License Information
MIT License




