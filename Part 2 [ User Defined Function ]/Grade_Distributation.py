"""
Quesiton 1 :
You are given a dataset of students grades and need to determine the grade distribution.

Question : Write a python Funciton
grade_distributin(grades) that takes a list of integer representing
student grades (0-100). Use a loop to count the number of grades in each grade catagory :
'A' ( 90-100) , 'B' (80-89) , 'C' (70-79), 'D' (60-69) , and 'F'(below 60).
Use if_elif_else statements within the loop to categorize the grades.
Return a dictionay with the counts of each grade category .

"""

def grade_distributaaiton(grades):
    for grade in grades:
        if 90 <= grade >=100:
            print("You have Got A+")
        elif 80<= grade <=89:
            print("You have Got B")
        elif 70<=grade<=79:
            print("You have Got C")
        elif 60<=grade<=69:
            print("You have got D")
        else:
            print("You area fail")
    return
grades = [85 , 92 , 74 , 63 , 95 , 70 , 58, 82 , 67 , 73]
grade_distributaaiton(grades)

