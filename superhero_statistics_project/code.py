# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'] = data['Gender'].replace('-', 'Agender')
gender_count = data['Gender'].value_counts()

plt.figure(figsize = (8, 8))
gender_count.plot(kind = 'bar')
plt.title('Value Counts of Gender') 
plt.xlabel('Gender Groups')
plt.ylabel('Values of Genders')
plt.legend()
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
plt.figure(figsize = (8, 8))

plt.pie(alignment, labels = alignment.index, explode = (0.05, 0.02, 0.08))
plt.title('Character Alignment')
plt.legend()
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']]
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std() 
#sc_df.loc[:, 'Strength].mean()
sc_combat = sc_df.loc[:, 'Combat'].std()
sc_pearson = np.divide(sc_covariance, np.multiply(sc_strength, sc_combat))
print('Pearson Correlation Coefficient between Strength & Combat is:, ', sc_pearson)

ic_df = data[['Intelligence', 'Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df.loc[:, 'Intelligence'].std()
ic_combat = ic_df.iloc[:, 1].std()
ic_pearson = np.divide(ic_covariance, np.multiply(ic_intelligence, ic_combat))
print('Pearson Correlation Coefficient between Intelligence & Combat is:, ', ic_pearson)



# --------------
#Code starts here
total_high = data.loc[:, 'Total'].quantile(0.99)
print('99% Quantile for Total is: ', total_high)

super_best = data[data['Total'] > total_high]
super_best_names = list(super_best['Name'])

print('The best superheroes/villans are: ', super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(1, 3, figsize = (10, 10))

#Subplot of boxplot for intelligence
data.loc[:, 'Intelligence'].plot(kind = 'box', ax = ax_1)
ax_1.set_title('Box Plot for Intelligence')

#Subplot for boxplot for Speed
data.loc[:, 'Speed'].plot(kind = 'box', ax = ax_2)
ax_2.set_title('Box Plot for Speed')

#Subplot for boxplot for Power
data.loc[:, 'Power'].plot(kind = 'box', ax = ax_3)
ax_3.set_title('Box Plot for Speed')

plt.show()



