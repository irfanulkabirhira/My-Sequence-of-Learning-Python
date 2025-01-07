"""

Question 3 :
Write a python function that takes a date string in the format "YYYY-MM-DD"
and returns a tuple containing the year , month , and day as integers.

Example Input : "2024-05-28"
Expected Output : (2021,5,28)
"""
#we will use the concept of slicing

def extract_date_parts(date_string):
    year = int(date_string[0:4])
    month = int(date_string[5:7])
    day = int(date_string[8:])
    return (year,month,day)
