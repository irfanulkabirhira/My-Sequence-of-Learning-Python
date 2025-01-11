"""
this Code will approved a man that he can Ride on Roller Coaster or not !! Based on his Height , Age

(1st if-else Condition )
  if height >= 120 then --> he can ride roller coaster
  else No ways of riding on roller Coaster
(2nd if_else Condition)
   if age < 12 --> then His Bill would be = 5 Taka
   elif age <=18 --> then his Bill would be = 7 Taka
   elif age 45 <= age <=55 --> these people ride free in cost
   else---> then Bill = 12

(3rd if-else Condition )
    if want to take photo -->then bill add = 3 taka
"""


print("********Welcome to the Roller Coaster **********")
height = int(input("Enter You height in Cm "))

#initialy Bill = 0
bill = 0

if height >= 120:
    print("yes ..sir <3 . You can ride the Roller Coaster! ")
    # age
    age = int(input("What is Your age ?"))
    if age < 12:
        bill = 5
        print("Child Ticket are 5 taka.")
    elif age <=18:
        bill = 7
        print("Teen Ticket are 7 taka.")
    elif 45 <= age <= 55:
        print("Sir you can Ride on Roller Coaster in free of cost , Thank You <3")
    else:
        bill = 12
        print("Adult ticket are 12 Taka.")


    wants_photo = input("Do you want a photo taken ? Y or N ").strip().upper()
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is {bill} Taka")

else:
    print("Sorry sir , You need to taller to ride , Hope for the best Sir !!")
