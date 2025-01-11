base_salary = float(input("Enter your base salary"))
years_of_service = int(input("Enter Your years of Service"))
if years_of_service>5:
    total_salary =base_salary + (0.08*base_salary)-(0.12*base_salary)
    print("You will get net salary", total_salary)
else:
    net_salary =base_salary - (0.12*base_salary)
    print("your net salary is ", net_salary)