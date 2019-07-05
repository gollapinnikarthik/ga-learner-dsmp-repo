# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = np.divide(len(df[df['fico'] > 700]), len(df['fico']))
p_b = np.divide(len(df[df['purpose'] == 'debt_consolidation']), len(df['purpose']))
df1 = len(df[df['purpose'] == 'debt_consolidation'])
p_a_b = np.divide(np.multiply(df1, p_a), p_b)
result = (p_a_b == p_a)
print('If fico score > 700 and (purpose == debt_consolidation) are  independent events or not : ', result)
# code ends here


# --------------
# code starts here
prob_lp = np.divide(len(df[df['paid.back.loan'] == 'Yes']), len(df))
prob_cs = np.divide(len(df[df['credit.policy'] == 'Yes']), len(df))
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = np.divide(new_df[new_df['credit.policy'] == 'Yes'].shape[0], new_df.shape[0])
bayes = np.divide(np.multiply(prob_pd_cs, prob_lp), prob_cs)
print('Bayes theorem : ', bayes)
# code ends here






# --------------
# code starts here
df['purpose'].value_counts().plot(kind = 'bar')
df1 = df[df['paid.back.loan'] == 'No']
df1.plot(kind = 'bar')


# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
print("Installment Median is: ", inst_median)
inst_mean = df['installment'].mean()
print("Installment Mean is: ", inst_mean)

plt.hist(df['installment'], bins=10)
plt.title("Histogram for Installment")
plt.hist(df['log.annual.inc'], bins=10)
plt.title("Histogram for Annual Income")
plt.show()
# code ends here


