house_size_1 = float(input("enter the Size of the hosue"))
bedrooms_1 = int(input("Enter the number of bedrooms"))
price_1= float(input("Enter the budget"))

house_size_2 = float(input("enter the Size of the hosue"))
bedrooms_2 = int(input("Enter the number of bedrooms"))
price_2= float(input("Enter the budget"))

house_price_1= house_size_1*5000
print("The price of the house for the user1 ", house_price_1)

house_price_2= house_size_2*5000
print("The price of the house for the user2 ", house_price_2)

threshold_price = 7500000
user1_threshold = house_price_1 >=threshold_price
user2_threshold = house_price_2 >=threshold_price
print (f"user 1 is paying above thresold ", {user1_threshold})
print (f"user 2 is paying above thresold ", {user2_threshold})