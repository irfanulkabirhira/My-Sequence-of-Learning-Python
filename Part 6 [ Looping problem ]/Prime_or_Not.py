
num = int(input("Enter Any Number"))
for i in range(2, num):
    if num % i == 0:
        print("Not a Prime Number")
        break
    else:
        print("Prime Number")
        break
