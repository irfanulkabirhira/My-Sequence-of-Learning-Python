"""
Question 1 :
Write a user-defined function to process the exam scores and calculate the following statistics :

->The average exam score .
->the Highest exam Score .
->The lowest exam score .
->The number of students who passed the exam(assuming a passing score is 80 or above ).
->The number of students who failed the exam .

exam_score = [ 85 , 92, 78 , 90 , 88 , 95 , 82 , 79 , 87 , 91 ]
"""

def calculat_exam_statistics(exam_score):
    num_students = len(exam_score)
    avg_score = sum(exam_score)/num_students
    highest_score = max(exam_score)
    lowest_score = min(exam_score)

    # Initially Number of Passed students are 0
    num_passed = 0
    for score in exam_score:
        if score >= 80:
            num_passed += 1
        num_failed = num_students - num_passed
        return avg_score, highest_score, lowest_score, num_failed , num_passed


# Example Uses :
exam_score = [ 85 , 92, 78 , 90 , 88 , 95 , 82 , 79 , 87 , 91 ]
avg_score, highest_score, lowest_score, num_failed,num_passed =calculat_exam_statistics(exam_score)

print("The Average Score is = ", avg_score)
print("The Highest Score is = ",highest_score)
print("The Lowest Score is = ",lowest_score)
print("The Number of Student who Passed = ",num_passed)
print("The Number of Student who Failed = ",num_failed)

