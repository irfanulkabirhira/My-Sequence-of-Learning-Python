"""
https://www.youtube.com/watch?v=NCXrRuCthZY
Hira = 3
these three are same [:]
                    [0:3]
                     [::]
these three will print --> Hira
"""
s = input("Enter any Number ")
revstr = s[::-1]
print(f"the reverse string is =  {revstr} ")

print("\n")

# String Palindrome
if s == revstr:
    print("Palindrome")
else:
    print("Not palindrome")