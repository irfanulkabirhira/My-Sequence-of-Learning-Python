"""
4 ! ==> 4*3*2*1 =24
Take a number from the User -->
initially Fact = 1
while Number > 0 --> Then ==> fact * Number
                     # As it's Decreasing with the 4 -> 3 -> 2 -> 1 => 4*3*2*1
                      So , Number -=1
"""

Number = int(input("Enter ay Number which is greater than Zero : "))
# Initially fact = 1
fact = 1
while Number > 0:
    fact *= Number
    Number -= 1
    print(f"The Factorial is {fact} ")

