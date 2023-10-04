import streamlit as st
import pandas as pd
import joblib
import sklearn 
from sklearn.ensemble import RandomForestClassifier 

# Load the pre-trained Random Forest model
model = joblib.load("rf.pkl")

# Streamlit UI elements
st.title("Churn Prediction App")
st.markdown("<br>", unsafe_allow_html=True)  # Add a blank line
st.write("Please input the following data:")

# User input fields
age = st.slider("Age", 18, 100, 30)
tenure = st.slider("Tenure", 0, 20, 5)
balance = st.slider("Balance", 0, 250000, 50000)
num_of_products = st.slider("Number of Products", 1, 4, 2)
is_active_member = st.checkbox("Is Active Member?")
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Female", "Male"])

# Mapping categorical variables to numerical values
geography_mapping = {"France": 0, "Germany": 1, "Spain": 2}
gender_mapping = {"Female": 0, "Male": 1}

# Encoding categorical variables
geography_encoded = geography_mapping.get(geography, 0)
gender_encoded = gender_mapping.get(gender, 0)

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'IsActiveMember': [int(is_active_member)],
    'Geography_France': [1 if geography_encoded == 0 else 0],
    'Geography_Germany': [1 if geography_encoded == 1 else 0],
    'Geography_Spain': [1 if geography_encoded == 2 else 0],
    'Gender_Female': [1 if gender_encoded == 0 else 0],
    'Gender_Male': [1 if gender_encoded == 1 else 0]
})

# Make prediction when the "Predict" button is clicked
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.subheader("Prediction: The customer is likely to churn.")
    else:
        st.subheader("Prediction: The customer is not likely to churn.")
