num1 = int(input("Enter The First Number "))
num2 = int(input("Enter the Second Number "))
num3 = int(input("Enter the Third Number "))

# Initially Largest Number = num1
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3

print(f"The Largest Number is = {largest}")
