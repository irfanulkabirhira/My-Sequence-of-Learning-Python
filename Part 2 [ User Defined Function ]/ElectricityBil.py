""" Suppose per unit Electricity fine Bill is about 10 TK for every Deadline ,
And you spent 300W electricity per month , So what would be the fine ?.  """


def details_bill():
    print("The Last Date of the bill payment is on next Week Sunday")
    print("After Deadline , you have to pay fine")
    print("Pay Your Bill Soon")

for i in range (3):
    a = input("Enter Your Name ")
    b = int(input("Enter the Unit of last Electricity you have paid Sunday = "))
    bill =b*10
    print("Total Amount of Bill is = ", bill)
    details_bill()