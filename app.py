import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="📊 Telecom Churn Prediction App", layout="centered")
st.title("📞 Customer Churn Prediction")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Encoding maps (must match what was used during training)
binary_map = {'Yes': 1, 'No': 0}
gender_map = {'Male': 1, 'Female': 0}
internet_service_map = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
payment_method_map = {
    'Electronic check': 0,
    'Mailed check': 1,
    'Bank transfer (automatic)': 2,
    'Credit card (automatic)': 3
}
multi_map = {'No': 0, 'Yes': 1, 'No phone service': 2, 'No internet service': 2}

# Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.slider("Tenure (months)", 0, 72, 12)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox("Payment Method", list(payment_method_map.keys()))
MonthlyCharges = st.slider("Monthly Charges", 0, 150, 70)
TotalCharges = st.slider("Total Charges", 0, 10000, 2000)

# Predict
if st.button("Predict"):
    input_dict = {
        "gender": gender_map[gender],
        "SeniorCitizen": SeniorCitizen,
        "Partner": binary_map[Partner],
        "Dependents": binary_map[Dependents],
        "tenure": tenure,
        "PhoneService": binary_map[PhoneService],
        "MultipleLines": multi_map[MultipleLines],
        "InternetService": internet_service_map[InternetService],
        "OnlineSecurity": multi_map[OnlineSecurity],
        "OnlineBackup": multi_map[OnlineBackup],
        "DeviceProtection": multi_map[DeviceProtection],
        "TechSupport": multi_map[TechSupport],
        "StreamingTV": multi_map[StreamingTV],
        "StreamingMovies": multi_map[StreamingMovies],
        "Contract": contract_map[Contract],
        "PaperlessBilling": binary_map[PaperlessBilling],
        "PaymentMethod": payment_method_map[PaymentMethod],
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)[0]

    st.success(f"Prediction: {'Churn' if prediction == 1 else 'Not Churn'}")
