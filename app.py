import streamlit as st

import pandas as pd
import joblib  # To load trained model


# Load your trained Isolation Forest model
model = joblib.load('Anomaly_detection_model.pkl')


# Define all possible categorical values
payment_gateways = ['CRED', 'Google Pay', 'HDFC', 'ICICI UPI', 'IDFC UPI', 'Other', 'Paytm', 'Phonepe']
transaction_locations = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 
                         'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 
                         'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 
                         'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 
                         'Uttarakhand', 'West Bengal']

# Streamlit UI
st.title("Transaction Anomaly Detection")


# User Inputs
transaction_amount = st.number_input("Transaction Amount")
avg_transaction_amount = st.number_input("Average Transaction Amount")
frequency_of_transactions = st.number_input("Frequency of Transactions (Last Month)")

payment_gateway = st.selectbox("Payment Gateway", payment_gateways)
transaction_location = st.selectbox("Transaction Location", transaction_locations)

# Prediction Function
def predict_anomaly(transaction_amount, avg_transaction_amount, freq_of_transactions, 
                    payment_gateway, transaction_location, model):
    # Create input feature dictionary
    input_data = {
        "Transaction_Amount": transaction_amount,
        "Average_Transaction_Amount": avg_transaction_amount,
        "Frequency_of_Transactions": freq_of_transactions,
    }

    # One-hot encode Payment Gateway
    for gateway in payment_gateways:
        input_data[gateway] = 1 if payment_gateway == gateway else 0

    # One-hot encode Transaction Location
    for location in transaction_locations:
        input_data[location] = 1 if transaction_location == location else 0

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Make prediction
    prediction = model.predict(input_df)[0]
    
    return "🟥 **Anomaly Detected**" if prediction == -1 else "🟩 **Normal Transaction**"

# Predict Button
if st.button("🔍 Check Transaction"):
    result = predict_anomaly(transaction_amount, avg_transaction_amount, frequency_of_transactions, 
                             payment_gateway, transaction_location, model)
    st.subheader(result)
