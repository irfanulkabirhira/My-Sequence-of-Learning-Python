# https://www.youtube.com/watch?v=Ib1bSQdXBZ0
Number = int(input("Enter any Number "))
n1, n2 = 0, 1
sum = 0
if Number <= 0:
    print("Enter a Number which is greater than Zero ")

print("The Fibonaci Series is : ")
for i in range(0, Number):
    print(sum, end=" ")
    n1 = n2
    n2 = sum
    sum = n1+n2





