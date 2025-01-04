try:
    age = int(input("How old are you ? "))
except ValueError:
    print("You have typed Invalied, Please Type something Numarical .")
    age = int(input("How old are you ? "))


if age >= 18:
        print(f"You can Drive Car in this {age} age")
else:
        print(f"You can't Drive car in this {age} age ")
