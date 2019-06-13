### Project Overview

 # Summarizing Data with Statistics

Superhero Statistics

The rise of superheroes and supervillains is at an all time high. The 'Academy of Super Beings(ASB)' was formed to bring order to it. We have with us the data of more than 500 super humans but we need your knowledge of descriptive statistics in figuring out the important insights from it.


### Learnings from the project

 After completing this project, I will had a better grip on the applications of descriptive statistics. In this project, I have applied the following concepts:

Bar plotting

Boxplot plotting

Pie-chart plotting

Subplot operations

Feature Correlation

IQR operations


### Approach taken to solve the problem

 Loaded the csv into a dataframe and used replace to replace null values in Gender column. Constructed a box plot for value counts for the gender column to know how many are male and female category.

Constructed a pie chart  for value counts for the alignment column to know how many have 'good', 'bad' and neutral qualities.

Subsetted the data with only 'Strength' , 'Combat' and 'Intelligence' columns. Calcuated covariance between the variables 'Strength' and 'Combat' and 'Intelligence' and 'Combat' and standard deviation for each of the variable. Calcuated Pearson Correlation Coefficient to see which is more correlated to combat. We used Pearsons instead of Spearman as there no much outliers in our data.

Calculated 99 percentile for total points column and subsetted the data only with the created 99% variable to print the list of names of superheros/villans which fall under that category.

Created subplots of boxplots for 'Intelligence', 'Speed' and 'Power' to which among them is the one with the most disperse values i.e. spread across a larger range of values. This made us understand if entire humanity has to fight against any one of these top super beings, improving Speed & Power atributes of a normal human would be our best chance for survival?


