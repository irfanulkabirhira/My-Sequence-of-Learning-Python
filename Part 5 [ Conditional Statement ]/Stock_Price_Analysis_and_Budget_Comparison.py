stock_symbol = 'xyz'
current_price = 100
percent_change = 10
new_price = current_price*(1+percent_change/100)
print("the new price of the stock is ", new_price)
user_budget = int(input("enter Your Budget"))
a=user_budget >=new_price
print("User budget is greater than new price ", a)