import numpy as np
import pickle
import streamlit


# loading the saved model
load_model = pickle.load(open('C:/Users/kh/Downloads/Standard Bank/trained_lr.sav', 'rb'))


# create the a function for prediction

def standard_bank(input_data):
    # Convert the input data to a numpy array
    input_data_array = np.array(list(input_data.values())).reshape(1, -1)

# Make predictions
    prediction = load_model.predict(input_data_array)

# Display the prediction
    if prediction[0] == 'Y':
        print('Loan Approved!')
    else:
        print('Loan Not Approved.')


# Create the main function
def main():
    print("Welcome to the Standard Bank Loan Approval Prediction System!")

    # Get user input for prediction
    applicant_income = float(input('Enter Applicant Income: '))
    coapplicant_income = float(input('Enter Coapplicant Income: '))
    loan_amount = float(input('Enter Loan Amount: '))
    loan_amount_term = float(input('Enter Loan Amount Term: '))
    credit_history = float(input('Enter Credit History (0 or 1): '))

    # Create a dictionary with the user input
    user_data = {
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history
    }

    # Get and display the prediction
    prediction_result = standard_bank(user_data)
    print("Prediction Result:", prediction_result)

if __name__ == "__main__":
    main()