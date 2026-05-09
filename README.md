# Car Price Prediction - Exploratory Data Analysis

This project focuses on analyzing a large used car auction dataset to identify the factors that influence vehicle selling prices. The ultimate goal is to build a machine learning model capable of predicting the selling price of a vehicle based on its characteristics.

## Project Objective

To understand how features such as vehicle age, mileage, market valuation, transmission type, body type, and manufacturer affect the selling price of used cars.

## Dataset

The dataset contains more than 500,000 vehicle auction records with information such as:

- Year
- Make
- Model
- Trim
- Body
- Transmission
- Condition
- Odometer
- Color
- Interior
- MMR (Manheim Market Report)
- Selling Price
- Sale Date

## Exploratory Data Analysis

### Numerical Features vs Selling Price
- Year vs Selling Price
- Odometer vs Selling Price
- MMR vs Selling Price

### Categorical Features vs Selling Price
- Body vs Selling Price
- Transmission vs Selling Price
- Make vs Selling Price

## Data Cleaning

- Removed unnecessary columns such as `vin`, `seller`, and `saledate` (reserved for future feature engineering)
- Identified and removed invalid transmission categories such as `sedan` and `Sedan`
- Handled missing values and inspected data types

## Key Insights

- Newer vehicles generally have higher selling prices.
- Higher mileage is associated with lower resale value.
- MMR has the strongest relationship with selling price.
- Automatic vehicles sell for more on average than manual vehicles.
- Luxury brands and premium body types command higher prices.

## Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Machine Learning (Next Steps)

- Feature Engineering
- Encoding Categorical Variables
- Train-Test Split
- Regression Model Training
- Model Evaluation using MAE, RMSE, and R² Score

## Dataset Download

The dataset used in this project is too large to be included in this repository.

You can download the dataset from Kaggle:
https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data

After downloading, place `car_prices.csv` in the root directory of this project.

## Author

Suban Sharathi K
