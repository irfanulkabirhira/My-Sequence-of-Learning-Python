"""
Quesiton 1:
you are taked with validating user input for emial address .
Write a python program that promts the user to enter an emial address .
Use a while loop to iterate through the input and check if the email address contains and '@' and '.' symbol.
If the email address does not meet this criteria , print "Invalid emial address format. please try again ".
Otherwise , Print emial address validation passed
"""

email = input("Please enter your mail Address")
#Initilization a flag track validation status
valid_email = False

#start the loop
while not valid_email:
    #check if emial contains "a" and "."
    if "@"in email and "." in email:
        print ("Emial Address validation passed")
        valid_email=True
    else:
        print("Invalid email Address , please try again")
        email=input("please enter your Mail address")