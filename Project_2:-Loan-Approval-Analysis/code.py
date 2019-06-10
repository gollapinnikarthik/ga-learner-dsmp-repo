# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path, sep=',')
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)




# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'], axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode(axis=0, numeric_only=False)
#As it is mode it will give us series so we cannot directly use fillna to replace it
#instead we have to access the first element by its position 
banks = banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], 
values='LoanAmount', aggfunc='mean')


# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed']=="Yes") & (banks["Loan_Status"]=='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=="No") & (banks["Loan_Status"]=='Y')])
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status) * 100
print(percentage_se)
percentage_nse = (loan_approved_nse/Loan_Status) * 100
print(percentage_nse)
# code ends here


# --------------
# code starts here
print(banks.head())
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12, banks.iloc[8][0])
big_loan_term = len(loan_term[loan_term >= 25])




# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)



# code ends here


