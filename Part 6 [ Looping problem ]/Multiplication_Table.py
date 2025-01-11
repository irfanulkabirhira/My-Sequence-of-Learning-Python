"""
Question 1: 
Implement a python program to generate the multiplication table of a given numbers using a for loop

Step 1 : 
Take a Number from The User --> Then , Apply Loop 
"""""
number = int(input("Enter a number to generate its Multiplication table"))
print("The Multiplication of = ", number)

for i in range(1, 11):
    print(f"{number}x{i} = {number * i}")



