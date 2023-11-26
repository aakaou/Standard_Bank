import numpy as np
import pickle

# loading the saved model
load_model = pickle.load(open('C:/Users/kh/Downloads/Standard Bank/trained_lr.sav', 'rb'))

# Assuming 'new_data' is your new data in the form of a dictionary or list
# Make sure to include all the features used during training

new_data = {
    'ApplicantIncome': 5000,
    'CoapplicantIncome': 2000,
    'LoanAmount': 150,
    'Loan_Amount_Term': 360,
    'Credit_History': 1.0
}

# Convert the input data to a numpy array
input_data = np.array(list(new_data.values())).reshape(1, -1)

# Make predictions
prediction = load_model.predict(input_data)

# Display the prediction
if prediction[0] == 'Y':
    print('Loan Approved!')
else:
    print('Loan Not Approved.')

