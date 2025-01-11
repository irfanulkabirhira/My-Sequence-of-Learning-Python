""" Pizza --> 3 parts must be there , Size , You Want pepperoni or not , Extra_Cheese
        if size S -> add bill extra 15 Taka
        if size M -> add bill extra 20 Taka
        if Size L -> add bill extra 25 Taka
    (2nd if-else Condition)
        if pepperoni then add bill extra 2 Taka
    (3rd if-else Condition)
        if Extra_cheese added then bill extra 1 Taka
        -> Have to Find the Bill !!       """


# Welcoming Message From the Restaurant
print("**********Welcome to Pizza Hut !!! sir <3 ********* ")

# initially bill 0
bill = 0
# pizza Type
order = input(
    "Which Pizza would you like to order, Sir? Type Y for Neapolitan Pizza,"
    " G for Greek Pizza, NY for New York Style Pizza: ")


if order == "Y":
    bill += 300
elif order == "G":
    bill += 350
elif order == "NY":
    bill += 400
else:
    print("Invalid selection. Please choose a valid pizza type.")
    exit()

# Pizza size
size = input("What size do you prefer? s, m, or l: ").lower()
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("Invalid size. Please choose s, m, or l.")
    exit()

# Pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Yes or No: ").lower()
if pepperoni == "yes":
    bill += 2

# Extra cheese
extra_cheese = input("Do you want extra cheese? Yes or No: ").lower()
if extra_cheese == "yes":
    bill += 1

# Final Print
print(f"Final Bill is : {bill} Taka .")


