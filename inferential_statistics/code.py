# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data = pd.read_csv(path)
data_sample = data.sample(n = sample_size, random_state=0)
#Code starts here
sample_mean = data_sample.iloc[:,4].mean()
print("Mean of installment is: ", sample_mean)
sample_std = data_sample.iloc[:, 4].std()
print("Standard deviation of installment is: ", sample_std)


margin_of_error = round(np.multiply(z_critical, np.divide(sample_std, math.sqrt(sample_size))), 2)
print('The margin of error is', margin_of_error)

confidence_interval = (np.subtract(sample_mean, margin_of_error), np.add(sample_mean, margin_of_error))
true_mean = data.iloc[:, 4].mean()

if true_mean in confidence_interval:
    print('True mean falls in the confidence interval region')
else:
    print('True mean does not fall in the confidence interval region')











# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3, 1, figsize = (20, 10))
for i in range(len(sample_size)):
    m = []
    for j in range(1000):
        sample_installment_data = data.iloc[:,4].sample(n = sample_size[i])
        #sample_installment_mean = sample_installment_data.mean()
        m.append(sample_installment_data.mean())
    mean_series = pd.Series(m) 


for i in range(len(sample_size)):
        axes[i] = plt.hist(mean_series)


# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data.iloc[:,3] = data.iloc[:,3].astype(str)
data.iloc[:,3] = np.divide(data.iloc[:,3].apply(lambda x:x.replace("%", "")).astype(float), 100)

z_statistic, p_value = ztest(data[data['purpose'] == 'small_business']['int.rate'], value = data['int.rate'].mean(), alternative = 'larger')

if p_value > 0.05:
    print("The null hypothesis is rejected")
else:
    print("The null hypothesis is not rejected")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1 = data[data['paid.back.loan'] == 'No']['installment'], x2 = data[data['paid.back.loan'] == 'Yes']['installment'])

if p_value < 0.05:
    print('We reject the null hypothesis')
else:
    print('We cannot reject the  null hypothesis')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
print(yes)
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])

chi2, p, dof, ex = chi2_contingency(observed)
if chi2 > critical_value:
    print("NUll hypothesis is rejected")
else:
    print('Null hypothesis cannot be rejected')



