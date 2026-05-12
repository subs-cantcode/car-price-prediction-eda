import streamlit as st
import pandas as pd
import joblib

model = joblib.load("car_price_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("Used Car Price Prediction")

year = st.number_input("Manufacturing Year", min_value=1980, max_value=2026, value=2015)
condition = st.number_input("Condition", min_value=1.0, max_value=50.0, value=35.0)
odometer = st.number_input("Odometer", min_value=0, value=50000)
mmr = st.number_input("MMR Value", min_value=0, value=15000)

transmission = st.selectbox("Transmission", ["automatic", "manual"])
body = st.selectbox("Body Type", ["Sedan", "SUV", "Hatchback", "Coupe", "Convertible"])
make = st.selectbox("Car Brand", ["Toyota", "Honda", "BMW", "Ford", "Nissan", "Kia"])

car_age = 2026 - year

input_data = pd.DataFrame({
    "year": [year],
    "condition": [condition],
    "odometer": [odometer],
    "mmr": [mmr],
    "car_age": [car_age],
    "transmission": [transmission],
    "body": [body],
    "make": [make]
})

input_encoded = pd.get_dummies(input_data)

input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

if st.button("Predict Selling Price"):
    prediction = model.predict(input_encoded)[0]
    st.success(f"Predicted Selling Price: ${prediction:,.2f}")