import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained model
model = tf.keras.models.load_model("regression_model.h5")

# Load the encoders and scaler
with open("label_encoder_gender.pkl", "rb") as file:
    label_encoder_gender = pickle.load(file)

with open("ohp_geo_regression.pkl", "rb") as file:
    ohp_geo = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


## streamlit app
st.title("Customer Salary Prediction 💵")

st.markdown(
    """
This application uses an **Artificial Neural Network (ANN)** to predict the **Estimated Salary** of a bank customer based on their profile.

### 📊 About the Data
The deep learning model was trained on historical bank customer data, which includes:
- **Demographics:** Country of origin, Gender, and Age.
- **Financial Info:** Credit Score and Account Balance.
- **Activity Profile:** Tenure (years with the bank), Number of Products held, Credit Card ownership, Active Member status, and Exited (churn) status.

### ⚙️ How to Use
Simply adjust the customer profile parameters below. The model will instantly calculate the estimated salary for the customer!
---
"""
)

# User input
geography = st.selectbox("Geography", ohp_geo.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.slider("Age", 18, 92)
balance = st.number_input("Balance")
credit_score = st.number_input("Credit Score")
exited = st.selectbox("Exited", [0, 1])
tenure = st.slider("Tenure", 0, 10)
num_of_products = st.slider("Number of Products", 1, 4)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

# Prepare the input data
input_data = pd.DataFrame(
    {
        "CreditScore": [credit_score],
        "Gender": [label_encoder_gender.transform([gender])[0]],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_of_products],
        "HasCrCard": [has_cr_card],
        "IsActiveMember": [is_active_member],
        "Exited": [exited],
    }
)

# One-hot encode 'Geography'
geo_encoded = ohp_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(
    geo_encoded, columns=ohp_geo.get_feature_names_out(["Geography"])
)

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)


# Predict salary
prediction = model.predict(input_data_scaled)
predicted_salary = prediction[0][0]

st.success(f"Predicted Estimated Salary: ${predicted_salary:,.2f}")
