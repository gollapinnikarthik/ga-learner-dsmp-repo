### Project Overview

 ## Probability of the Loan Defaulters

For this project, we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

## Problem Statement

What is the probability that the borrower paid back their loan in full?


### Learnings from the project

 After completing this project, I have a better understanding of probability. In this project, I have applied the following concepts.

Independency check

Bayes theorem

Visualizing discrete variable

Visualizing continuous variable


### Approach taken to solve the problem

 Load dataset using pandas read_csv api in variable df.

Calculated the probability p(A)for the event that fico credit score is greater than 700.

Calculated the probabilityp(B) for the event that purpose == 'debt_consolation'.

Calculated the probability of purpose == 'debt_consolidation'.

Calculated the probablityp(B|A) for the event purpose == 'debt_consolidation' given 'fico' credit score is greater than 700.

Calculated the probablityp(B|A) for the event paid.back.loan == 'Yes' given credit.policy == 'Yes' to find out the bayes conditional probability. 

Visualize the bar plot for the feature 'purpose'.

Calculated the paid.back.loan == No.

Visualized the bar plot for the feature purpose where paid.back.loan == No

Calculted the median and mean for 'installment' feature.

Plotted the histogram for installment with mean and median being displayed.

Plotted the histogram for log anual income.




