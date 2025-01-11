# https://www.youtube.com/watch?v=STcQTjhIKkc&t=219s
# step 1:
""" Take a number from the user,
initially Count = 0
--> while count ! = 0 --> then number // = 10 --> count +=1
             """

number = int(input("Enter a Number to Count a digit !!"))
# initially count = 0
count = 0
while number != 0:
    number //= 10
    count += 1

print(f"The Digit of this {number} is {count}")

