"""
Question 2:

As part of your role in a data-driven project, you need to take input from the user for their age , wight ,and height .
However , there's an issue :
the user has entered their age as a negative number .
-> You need to correct the age of the user and after correcting the age ,
calculating their Basal Metabolic Rate (BMR)
using the Harris-Benedict equation for men .
Note that: Ensure that the final answer of BMR is an integer.

Basel Metabolic Rate (BMR) :
Formula ( Harries Benedict equaion for men ) :
BMR = 88.362 + (13.397 * weight in kg ) + ( 4.799*height  in cm ) - ( 5.677 * age in years)

"""


age = int(input("enter the age"))
weight = int(input("enter the weight"))
height = float(input("Enter the Height"))
# The abs function returns the absolute value of a number. The absolute value of a number is its non-negative value,
# regardless of whether it is positive or negative.
correct_age = abs(age)
print("The Correct age of user  = ", correct_age)

BMR = "88.362 + (13.397 * weight ) + ( 4.799*height ) - ( 5.677 * age ) "

# You used eval to dynamically evaluate the string expression stored in BMR as Python code and compute its result
bmr = eval(BMR)
print("Print the BMR of the patient is ",int(bmr))