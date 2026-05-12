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

---

# 🚗 Used Car Price Prediction (Building the Machine Learning Model)

An end-to-end Machine Learning project that predicts used car selling prices based on vehicle features such as manufacturing year, condition, mileage, transmission type, body type, and market value (MMR).

The project covers the complete data science workflow:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training using Linear Regression
- Model Evaluation
- Model Serialization with Joblib
- Deployment with Streamlit

---

## 📊 Model Performance

| Metric | Value |
|------|------:|
| R² Score | 0.9704 |
| Mean Absolute Error (MAE) | 1,042.71 |
| Root Mean Squared Error (RMSE) | 1,623.06 |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📁 Project Structure

```text
used-car-price-prediction/
├── car_prices_eda.ipynb
├── car_prices_ml_model.ipynb
├── app.py
├── car_price_model.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md

## Dataset Download

Due to GitHub file size limitations, the original dataset is not included in this repository. Please download it from Kaggle and place it in the project directory before running the notebook.

You can download the dataset from Kaggle:
https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data

After downloading, place `car_prices.csv` in the root directory of this project.

## Author

Suban Sharathi K
