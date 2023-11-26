import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('C:/Users/kh/Downloads/Standard Bank/logistic_regression_model.pkl', 'rb') as file:
    loaded_models = pickle.load(file)
with open('C:/Users/kh/Downloads/Standard Bank/trained_lr.sav', 'rb') as file:
    loaded_model = pickle.load(file)
def predict_loan_approval(data):
    input_data = np.array(list(data.values())).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return prediction[0]

st.title('Loan Approval Prediction')

# Create input fields in the app
applicant_income = st.slider('Applicant Income', min_value=0, max_value=10000, step=100)
coapplicant_income = st.slider('Coapplicant Income', min_value=0, max_value=10000, step=100)
loan_amount = st.slider('Loan Amount', min_value=0, max_value=500, step=10)
loan_term = st.slider('Loan Amount Term', min_value=0, max_value=500, step=10)
credit_history = st.selectbox('Credit History', [0.0, 1.0])

# Create a dictionary with user input
user_input = {
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_term,
    'Credit_History': credit_history
}

# Get prediction
result = predict_loan_approval(user_input)

# Display the prediction
if result == 'Y':
    st.success('Loan Approved!')
else:
    st.warning('Loan Not Approved.')
