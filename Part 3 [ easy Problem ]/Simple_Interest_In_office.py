"""
Question 2

In a Finance based organization,The task is to calculate the simple interest
Given the principle amount,interest rate and time period,
->The interest rate is 8%,
->the principal amount is 15,00,000 Rs and
->the time period is 3 years,
calculate the simple interest.
Also,the threshold amount is Rs 1,20,000
Please check, if the calculated interest is greater or less than the threshold Amount.
"""

# Step 1:
principle_amount = 1500000
time_period = 3
interest_rate = 8
simple_interest = (principle_amount * time_period * interest_rate) / 100
print("The Simple Interest Rate is =", simple_interest)

# Step 2:
threshol_amount = 120000
print("The Threshold amount and Simple Interest are equal =", threshol_amount == simple_interest)
print("The Threshold amount is getter than the Simple Interest =", threshol_amount > simple_interest)
print("The Threshold amount is less than the Simple Interest =", threshol_amount < simple_interest)